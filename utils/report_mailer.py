"""Send the HTML test report by e-mail (replaces send_mail_ui in the old send_report.py).

Mail account settings come from the [mail] section of Config/config.ini
(see ReadConfig.get_mail_settings); environment variables override them if set.

Flow, called from run_tests.py after the tests have finished:
    run tests -> HTML report file -> send_report(report) -> log in to SMTP -> send with attachment
"""
import logging
import smtplib
import ssl
import subprocess
from email.message import EmailMessage
from pathlib import Path
from CommonModule.read_config import ReadConfig

log = logging.getLogger(__name__)

DEFAULT_SUBJECT = "UI Automation Test Report for EGD Dev"
DEFAULT_BODY = ("Automation tests start at 18:00 every day. This report is sent automatically; "
                "please do not reply. You can find more details in the attachment. Thank you!")


def send_report(report_path, subject: str = DEFAULT_SUBJECT, body: str = DEFAULT_BODY) -> None:
    """Send the given HTML report file as an attachment."""
    report_path = Path(report_path)
    mail = ReadConfig().get_mail_settings()          # host, port, user, password, sender, receivers

    # 1. build the message (body + HTML attachment)
    msg = EmailMessage()
    msg["From"] = mail.sender
    msg["To"] = ", ".join(mail.receivers)
    msg["Subject"] = subject
    msg.set_content(body)
    msg.add_attachment(report_path.read_bytes(), maintype="text", subtype="html",
                       filename=report_path.name)

    # 2. connect, log in, send
    log.info("Connecting to SMTP server %s:%s", mail.host, mail.port)
    with smtplib.SMTP(mail.host, mail.port, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls(context=ssl.create_default_context())
        smtp.ehlo()
        smtp.login(mail.user, mail.password)
        log.info("Logged in, sending report %s", report_path.name)
        smtp.send_message(msg)
    log.info("Report mailed to %s", mail.receivers)


def disconnect_wifi() -> None:
    """Optional, Windows only (same as the old disconnect_wifi)."""
    try:
        subprocess.run(["netsh", "wlan", "disconnect"], check=True)
        log.info("WiFi disconnected")
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        log.warning("Could not disconnect WiFi: %s", exc)

# def disconnect_wifi(interface: str = None) -> None:
#     """Optional, Windows only. interface e.g. 'Wi-Fi' (see: netsh wlan show interfaces)."""
#     cmd = ["netsh", "wlan", "disconnect"]
#     if interface:
#         cmd.append(f"interface={interface}")
#     try:
#         result = subprocess.run(cmd, capture_output=True, text=True, errors="replace", check=False)
#     except FileNotFoundError:
#         log.warning("netsh not found (Windows only)")
#         return
#     output = (result.stdout or result.stderr).strip()
#     if result.returncode == 0:
#         log.info("netsh: %s", output)
#     else:
#         log.warning("netsh failed (code %s): %s", result.returncode, output)
