import pytest
from django.test import override_settings
from django.template import Context, Template
from django.test import RequestFactory


@override_settings(GLASS_ADMIN_THEME="ai")
def test_theme_tag_ai():
    """glass_theme_name tag returns 'ai' when configured."""
    from glass_admin.templatetags.glass_admin_tags import _get_theme
    assert _get_theme() == "ai"


@override_settings(GLASS_ADMIN_THEME="liquidglass")
def test_theme_tag_liquidglass():
    from glass_admin.templatetags.glass_admin_tags import _get_theme
    assert _get_theme() == "liquidglass"


@override_settings(GLASS_ADMIN_THEME="auto")
def test_theme_tag_auto():
    from glass_admin.templatetags.glass_admin_tags import _get_theme
    assert _get_theme() == "auto"


@override_settings(GLASS_ADMIN_THEME="bad_value")
def test_theme_tag_invalid_falls_back():
    from glass_admin.templatetags.glass_admin_tags import _get_theme
    assert _get_theme() == "liquidglass"


def test_theme_default_is_liquidglass():
    """Default theme when no setting is configured should be liquidglass."""
    from django.conf import settings
    from glass_admin.templatetags.glass_admin_tags import _get_theme, DEFAULT_THEME
    with override_settings():
        # Temporarily delete setting
        original = getattr(settings, "GLASS_ADMIN_THEME", None)
        try:
            if hasattr(settings, "GLASS_ADMIN_THEME"):
                delattr(settings, "GLASS_ADMIN_THEME")
            assert _get_theme() == "liquidglass"
        finally:
            if original is not None:
                settings.GLASS_ADMIN_THEME = original


@override_settings(GLASS_ADMIN_THEME="ai")
def test_css_tag_ai_returns_ai_css():
    """glass_theme_css tag should return link to ai.css when theme is ai."""
    from glass_admin.templatetags.glass_admin_tags import glass_theme_css
    result = str(glass_theme_css())
    assert "ai.css" in result
    assert 'rel="stylesheet"' in result


@override_settings(GLASS_ADMIN_THEME="liquidglass")
def test_css_tag_liquidglass_returns_liquidglass_css():
    from glass_admin.templatetags.glass_admin_tags import glass_theme_css
    result = str(glass_theme_css())
    assert "liquidglass.css" in result
    assert 'rel="stylesheet"' in result


@override_settings(GLASS_ADMIN_THEME="auto")
def test_css_tag_auto_returns_both():
    from glass_admin.templatetags.glass_admin_tags import glass_theme_css
    result = str(glass_theme_css())
    assert "ai.css" in result
    assert "liquidglass.css" in result
