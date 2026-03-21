# django-glass

[![PyPI version](https://img.shields.io/pypi/v/django-glass.svg)](https://pypi.org/project/django-glass/)
[![Python versions](https://img.shields.io/pypi/pyversions/django-glass.svg)](https://pypi.org/project/django-glass/)
[![Django versions](https://img.shields.io/pypi/djversions/django-glass.svg)](https://pypi.org/project/django-glass/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**django-glass** is a production-ready Django admin theme package that brings modern glassmorphism and AI-inspired aesthetics to the Django admin interface — with zero template changes required.

---

## Themes

| Theme | Description |
|-------|-------------|
| `liquidglass` | Apple WWDC 2025-inspired. Animated pastel gradient wallpaper, true glass surfaces with `backdrop-filter`, iridescent conic-gradient borders, specular inset highlights. Light & airy. |
| `ai` | Deep space AI aesthetic. Dark blue/purple background with dot-grid SVG texture, glassmorphism cards, electric blue accent glows, vibrant purple gradients. |
| `auto` | Automatically uses `liquidglass` on light OS preference, `ai` on dark. Switches live via `prefers-color-scheme`. |

---

## Installation

```bash
pip install django-glass
```

### Quick Start

1. Add `glass_admin` **before** `django.contrib.admin` in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "glass_admin",                   # <-- must be first
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ... your apps
]
```

2. *(Optional)* Add middleware for per-request theme access:

```python
MIDDLEWARE = [
    # ...
    "glass_admin.middleware.GlassAdminMiddleware",
]
```

3. *(Optional)* Set your preferred theme:

```python
GLASS_ADMIN_THEME = "liquidglass"  # default
```

4. Run `collectstatic` for production:

```bash
python manage.py collectstatic
```

That's it — visit `/admin/` and enjoy your new look.

---

## Configuration

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `GLASS_ADMIN_THEME` | `str` | `"liquidglass"` | Active theme. One of `"liquidglass"`, `"ai"`, or `"auto"`. |

### Example configurations

```python
# Liquid Glass (Apple-inspired, light)
GLASS_ADMIN_THEME = "liquidglass"

# AI Dark (deep space, dark)
GLASS_ADMIN_THEME = "ai"

# Auto (follows OS dark/light preference)
GLASS_ADMIN_THEME = "auto"
```

If an invalid value is set, `glass_admin` emits a `UserWarning` at startup and falls back to `"liquidglass"`.

---

## Template Tags

The `glass_admin_tags` library is available for advanced customization:

```html
{% load glass_admin_tags %}

{# Render the active theme's <link> tag(s) #}
{% glass_theme_css %}

{# Render the glass_admin <script> tag #}
{% glass_js %}

{# Get the active theme name as a string #}
{% glass_theme_name %}
```

---

## How It Works

django-glass uses Django's standard `APP_DIRS` template loading. By placing `glass_admin` before `django.contrib.admin` in `INSTALLED_APPS`, the package's `templates/admin/base_site.html` takes precedence and injects the theme CSS/JS into the admin's `{% block extrahead %}` — no modifications to your project's templates needed.

---

## JavaScript Features

- **Auto theme switching** — live `prefers-color-scheme` detection for the `auto` theme
- **Ripple effects** — glass ripple animation on submit buttons and action links
- **Toast auto-dismiss** — admin success/warning/error messages fade out after 5 seconds
- **Smooth transitions** — nav link hover animations

---

## Development

```bash
git clone https://github.com/shaochun/django-glass
cd django-glass
pip install -e ".[dev]"
pytest tests/ -v
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push to the branch and open a PR

---

## License

[MIT](LICENSE) © 2026 SC
