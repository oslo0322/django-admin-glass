# Changelog

All notable changes to django-glass will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-21

### Added
- Initial release of django-glass
- **Liquid Glass theme**: Apple WWDC 2025-inspired glassmorphism with animated pastel gradient background, true glass effect, iridescent borders, and specular highlights
- **AI Dark theme**: Deep space aesthetic with dark blue/purple background, dot-grid texture, glassmorphism cards, and electric blue accent glows
- **Auto theme**: Automatically selects AI Dark on dark OS preference, Liquid Glass on light
- Zero-config setup — just add `glass_admin` to `INSTALLED_APPS`
- `GLASS_ADMIN_THEME` setting for manual theme selection
- Template override system using Django's APP_DIRS template loading
- `glass_admin_tags` template tag library with `glass_theme_css`, `glass_theme_name`, `glass_js`
- `GlassAdminMiddleware` for per-request theme detection
- Ripple effects on buttons
- Auto-dismissing toast notifications
- Smooth nav hover transitions
