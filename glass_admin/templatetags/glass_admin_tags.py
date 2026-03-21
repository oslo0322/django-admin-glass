from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

VALID_THEMES = {"ai", "liquidglass", "auto"}
DEFAULT_THEME = "liquidglass"


def _get_theme():
    theme = getattr(settings, "GLASS_ADMIN_THEME", DEFAULT_THEME)
    if theme not in VALID_THEMES:
        return DEFAULT_THEME
    return theme


@register.simple_tag
def glass_theme_name():
    """Return the active theme name."""
    return _get_theme()


@register.simple_tag
def glass_theme_css():
    """Return HTML link tags for the active theme's CSS."""
    from django.utils.safestring import mark_safe
    theme = _get_theme()
    if theme == "auto":
        ai_url = static("glass_admin/css/ai.css")
        lg_url = static("glass_admin/css/liquidglass.css")
        return mark_safe(
            f'<link rel="stylesheet" href="{lg_url}" id="glass-theme-light" media="(prefers-color-scheme: light)">\n'
            f'<link rel="stylesheet" href="{ai_url}" id="glass-theme-dark" media="(prefers-color-scheme: dark)">'
        )
    css_file = "ai.css" if theme == "ai" else "liquidglass.css"
    url = static(f"glass_admin/css/{css_file}")
    return mark_safe(f'<link rel="stylesheet" href="{url}" id="glass-theme-css">')


@register.simple_tag
def glass_js():
    """Return HTML script tag for glass_admin JS."""
    from django.utils.safestring import mark_safe
    url = static("glass_admin/js/glass_admin.js")
    return mark_safe(f'<script src="{url}" defer></script>')
