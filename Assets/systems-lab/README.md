# Systems Lab artwork

Repository-hosted SVG artwork for the profile README. No external fonts, scripts, image services, or build step are required.

## Variants

- `header-{dark,light}.svg`: 1200 × 380 desktop identity banner.
- `header-mobile-{dark,light}.svg`: 600 × 340 compact identity banner.
- `lab-{dark,light}.svg`: 1200 × 220 horizontal lab process illustration.
- `lab-mobile-{dark,light}.svg`: 600 × 410 vertical lab process illustration.

The README selects mobile artwork at viewport widths of 600px or less, and chooses a palette using `prefers-color-scheme`. The final `img` provides a desktop dark fallback. Keep compact sources before desktop sources in each `picture`.

## Palette

| Token | Dark | Light |
| :--- | :--- | :--- |
| Background | #0D1117 | #F6F9FB |
| Main text | #EDF3F8 | #182B3B |
| Accent | #59C7D8 | #087D92 |
| Secondary text | #8DABB9 | #4E6A7A |
| Border | #293846 | #CEDBE3 |

Edit matching light, dark, and mobile variants together. Keep essential profile information in the README text as well as in image alt text. The header network is illustrative; the lab artwork describes a working process, not a measured network topology or live service status.

Existing project icons and the ScanEye banner are reused from `Assets/`. Older GIFs remain available but are no longer embedded in the profile.
