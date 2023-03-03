import os
import django

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../singleSignOn"))


def boot_django():
    from singleSignOn import settings

    django.setup()
