import pytest
from django.apps import apps


@pytest.mark.django_db
def test_glass_admin_app_installed():
    """glass_admin app should be installed and accessible."""
    assert apps.is_installed("glass_admin")


def test_glass_admin_app_config():
    """GlassAdminConfig should have correct metadata."""
    from glass_admin.apps import GlassAdminConfig
    config = apps.get_app_config("glass_admin")
    assert config.name == "glass_admin"
    assert config.verbose_name == "Glass Admin"


def test_glass_admin_before_django_admin():
    """glass_admin must appear before django.contrib.admin in INSTALLED_APPS."""
    from django.conf import settings
    app_list = list(settings.INSTALLED_APPS)
    glass_idx = app_list.index("glass_admin")
    admin_idx = app_list.index("django.contrib.admin")
    assert glass_idx < admin_idx, (
        "glass_admin must be listed before django.contrib.admin in INSTALLED_APPS"
    )


def test_version():
    """Package version should be accessible."""
    import glass_admin
    assert hasattr(glass_admin, "__version__")
    assert glass_admin.__version__ == "0.1.0"
