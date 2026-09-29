# Operations Log

An amber, phosphor-green, and charcoal profile told through five chapters: operator, projects, lab, activity, and the next chapter.

The images are self-contained. Terminal typing, instrument motion, connection paths, graph reveals, and button indicators use SVG CSS animation without scripts or external fonts. Lettering in the static portfolio artwork is outlined to preserve typography across renderers. Every animated SVG has a still variant; the README selects it when reduced motion is preferred.

Six original project banners cover ScanEye, ClusterEye, NuxView, Savit, lookmd, and the Proxmox lab case study. Project artwork illustrates the topic; it is not an application screenshot. Local source generations and build tools are kept outside the published asset set.

## Live data

`.github/profile_activity.py` uses GitHub's public API to generate the activity dashboard. `.github/workflows/snake.yml` publishes it alongside the contribution snake on the `output` branch every 12 hours. The dashboard reports its refresh time and distinguishes sampled public events from commits. Language bars count primary languages per owned non-fork repository, not proficiency or lines of code.

`live/` contains a verified bootstrap snapshot. The workflow copies that snapshot before fetching fresh data, so a temporary API failure leaves timestamped data available. It never invents replacement values.

## Interactions

Navigation images jump to chapters; project banners and source buttons open repositories; native disclosure sections reveal technical notes and terminal case studies. The terminals are animated presentations, not executable shells. The lab graphic illustrates an engineering workflow, not live server telemetry.

## Colors

Background `#090D0A` · Panel `#101810` · Amber `#FFBC57` · Green `#A6ED72` · Text `#E7EAD8` · Secondary text `#9AA88B`.
