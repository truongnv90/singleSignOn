import os
import sys

import django

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../singleSignOn"))


def boot_django():
    """Run administrative tasks."""
    from singleSignOn.settings import INSTALLED_APPS
    print(f"INSTALLED_APPS: {INSTALLED_APPS}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singleSignOn.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', 'runserver'])


if __name__ == '__main__':
    boot_django()
