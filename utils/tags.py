# Author:Yi Sun(Tim) 2022-08-05

"""unittest has no markers; this tiny decorator replaces pytest's @pytest.mark.smoke etc.
Select with:  python run_tests.py --tags smoke,regression"""


def tag(*names):
    def decorator(func):
        func.tags = set(names) | getattr(func, "tags", set())
        return func
    return decorator
