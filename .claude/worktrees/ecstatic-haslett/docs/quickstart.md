# Quick Start Guide

## Requirements

- Python 3.10+
- Django 4.2, 5.0, or 5.1

## Installation

Install from PyPI:

```bash
pip install django-glass
```

Or install the development version directly from source:

```bash
pip install -e ".[dev]"
```

## Setup

### 1. Add to INSTALLED_APPS

Open your Django project's `settings.py` and add `"glass_admin"` **before** `"django.contrib.admin"`:

```python
INSTALLED_APPS = [
    "glass_admin",                   # <-- Add this FIRST
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ... your other apps
]
```

> **Important:** `glass_admin` must appear before `django.contrib.admin` so that Django's template loader finds `glass_admin`'s `base_site.html` override first.

### 2. Choose a Theme (optional)

Add to `settings.py`:

```python
# Options: "liquidglass" (default), "ai", "auto"
GLASS_ADMIN_THEME = "liquidglass"
```

| Value | Effect |
|-------|--------|
| `liquidglass` | Apple-inspired glass with animated pastel gradients (default) |
| `ai` | Deep space dark theme with dot-grid texture and electric blue glows |
| `auto` | Follows OS dark/light mode preference, switches live |

### 3. Add Middleware (optional)

If you want `request.glass_admin_theme` available in views/middleware:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # ...
    "glass_admin.middleware.GlassAdminMiddleware",  # <-- Add this
]
```

### 4. Collect Static Files (production)

```bash
python manage.py collectstatic
```

### 5. Run the Dev Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/admin/` — you should see your new glass theme.

---

## Template Tags

For advanced customization, you can use the `glass_admin_tags` library directly in your own templates:

```html
{% load glass_admin_tags %}

<!-- Inject CSS for the active theme -->
{% glass_theme_css %}

<!-- Inject the glass_admin JS -->
{% glass_js %}

<!-- Get the theme name as a string -->
<span>Active theme: {% glass_theme_name %}</span>
```

---

## Troubleshooting

**Theme not showing up?**
- Make sure `glass_admin` is listed **before** `django.contrib.admin` in `INSTALLED_APPS`.
- Make sure `APP_DIRS: True` is set in your `TEMPLATES` configuration (it is by default).
- Run `python manage.py collectstatic` in production.

**Invalid theme warning?**
- Check that `GLASS_ADMIN_THEME` is one of `"liquidglass"`, `"ai"`, or `"auto"`. Any other value falls back to `"liquidglass"` with a `UserWarning`.

**Fonts not loading?**
- The themes import Inter from Google Fonts. Make sure your environment has internet access, or serve the font locally by overriding the CSS.
