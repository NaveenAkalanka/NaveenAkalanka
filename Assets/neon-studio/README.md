# Neon Studio profile assets

The profile uses a dark canvas with cyan, violet, pink, and amber accents. All artwork in this folder is repository-owned and loads without an external image-generation service.

## Motion

- `hero-v1.gif` and `hero-mobile-v1.gif`: 48-frame loops with orbital lights, stars, and flowing color ribbons. Text is visible throughout the animation.
- Matching `*-still.png` images are selected for visitors who prefer reduced motion.
- `divider.svg`, `lab.svg`, and `lab-mobile.svg` use CSS animation for flowing paths. `stack.svg` and its mobile variant use slow opacity pulses. The footer has an animated wave.
- SVG animations stop when `prefers-reduced-motion: reduce` is enabled. If animation is unavailable, the default SVG content remains visible.

## Layout

Mobile variants are selected at viewport widths of 600px or less. The six WebP project illustrations are optimized derivatives of the existing originals in `Assets/Banners/`; the original files are preserved.

The lab diagram illustrates areas of work. It is not a live infrastructure monitor. The contribution snake is the data-driven element: the existing scheduled workflow refreshes it on the repository’s `output` branch.

## Maintenance

Core colors: background `#080D19`, cyan `#42E8E0`, violet `#A88BFF`, pink `#FF78B6`, amber `#FFD17B`, text `#F1F5FF`.

Keep meaningful descriptions and project links in Markdown. When changing a published GIF, use a new versioned filename and update both its still-image fallback and README references.
