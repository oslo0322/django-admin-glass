from django.apps import AppConfig


class GlassAdminConfig(AppConfig):
    name = "glass_admin"
    verbose_name = "Glass Admin"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        from django.conf import settings
        valid_themes = {"ai", "liquidglass", "auto"}
        theme = getattr(settings, "GLASS_ADMIN_THEME", "liquidglass")
        if theme not in valid_themes:
            import warnings
            warnings.warn(
                f"GLASS_ADMIN_THEME='{theme}' is not valid. "
                f"Choose from: {', '.join(sorted(valid_themes))}. "
                "Falling back to 'liquidglass'.",
                UserWarning,
                stacklevel=2,
            )
