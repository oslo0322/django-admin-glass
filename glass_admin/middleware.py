from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


VALID_THEMES = {"ai", "liquidglass", "auto"}
DEFAULT_THEME = "liquidglass"


def get_theme():
    """Return the configured theme, falling back to default."""
    theme = getattr(settings, "GLASS_ADMIN_THEME", DEFAULT_THEME)
    if theme not in VALID_THEMES:
        return DEFAULT_THEME
    return theme


class GlassAdminMiddleware(MiddlewareMixin):
    """Middleware that injects the glass_admin theme into request."""

    def process_request(self, request):
        request.glass_admin_theme = get_theme()
