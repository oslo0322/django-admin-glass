import pytest
from unittest.mock import MagicMock
from django.test import RequestFactory, override_settings

from glass_admin.middleware import GlassAdminMiddleware, get_theme, DEFAULT_THEME


@pytest.fixture
def factory():
    return RequestFactory()


@pytest.fixture
def middleware():
    return GlassAdminMiddleware(get_response=lambda r: None)


def test_get_theme_default():
    """get_theme returns liquidglass when GLASS_ADMIN_THEME is not set."""
    from django.conf import settings
    # Remove setting if present
    with override_settings():
        if hasattr(settings, "GLASS_ADMIN_THEME"):
            del settings.GLASS_ADMIN_THEME
        # Override with no GLASS_ADMIN_THEME
        with override_settings(GLASS_ADMIN_THEME=None):
            pass
    assert get_theme() == DEFAULT_THEME


@override_settings(GLASS_ADMIN_THEME="ai")
def test_get_theme_ai():
    assert get_theme() == "ai"


@override_settings(GLASS_ADMIN_THEME="liquidglass")
def test_get_theme_liquidglass():
    assert get_theme() == "liquidglass"


@override_settings(GLASS_ADMIN_THEME="auto")
def test_get_theme_auto():
    assert get_theme() == "auto"


@override_settings(GLASS_ADMIN_THEME="invalid_theme")
def test_get_theme_invalid_falls_back():
    assert get_theme() == DEFAULT_THEME


@override_settings(GLASS_ADMIN_THEME="ai")
def test_middleware_sets_request_theme(factory, middleware):
    request = factory.get("/admin/")
    middleware.process_request(request)
    assert request.glass_admin_theme == "ai"


@override_settings(GLASS_ADMIN_THEME="liquidglass")
def test_middleware_sets_request_theme_liquidglass(factory, middleware):
    request = factory.get("/admin/")
    middleware.process_request(request)
    assert request.glass_admin_theme == "liquidglass"


@override_settings(GLASS_ADMIN_THEME="auto")
def test_middleware_sets_request_theme_auto(factory, middleware):
    request = factory.get("/admin/")
    middleware.process_request(request)
    assert request.glass_admin_theme == "auto"
