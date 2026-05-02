# Aiken Camellia Society Website

A Jekyll-based static website for the Aiken Camellia Society, hosted on GitHub Pages.

**Live site**: [https://aikencamellias.org](https://aikencamellias.org)

## Structure

```
_config.yml          # Site configuration
_data/
  navigation.yml     # Main navigation menu
_pages/
  about.md           # About the organization
  board.md               # Leadership listing
  calendar.md        # Events calendar (supports embedded calendars)
  announcements.md   # News and announcements
  links.md           # Useful external links
assets/css/
  main.scss          # Custom color scheme
index.md             # Home page
CNAME                # Custom domain configuration
```

## Local Development

### Prerequisites

- [Homebrew](https://brew.sh/) (macOS)
- [rbenv](https://github.com/rbenv/rbenv) for managing Ruby versions

### Setup

1. Install rbenv and ruby-build:
   ```bash
   brew install rbenv ruby-build
   ```

2. Add rbenv to your shell (add to `~/.zshrc`):
   ```bash
   eval "$(rbenv init - zsh)"
   ```

3. Install the required Ruby version (specified in `.ruby-version`):
   ```bash
   rbenv install
   ```

4. Install dependencies:
   ```bash
   gem install bundler
   bundle install
   ```

5. Start the local server:
   ```bash
   bundle exec jekyll serve
   ```

6. Visit `http://localhost:4000`

## Customization

### Color Scheme

Edit `assets/css/main.scss` to change the color scheme. Key variables:
- `$primary-color` - Main accent color (default: camellia red)
- `$secondary-color` - Secondary color (default: foliage green)

### Theme

This site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme. The skin is set to "mint" in `_config.yml` but can be changed to: air, aqua, contrast, dark, default, dirt, neon, mint, plum, or sunrise.

## Deployment

Push to the `main` branch to automatically deploy via GitHub Pages.
