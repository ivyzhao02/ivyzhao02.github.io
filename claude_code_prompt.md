# Claude Code prompt — next round of changes for ivyzhao.ca

Please make the following changes to index.html:

---

## 1. Global font/size increase

Increase all font sizes across the entire site by one notch:
- Sidebar nav item labels: from 11px to 13px
- Sidebar section labels (Press Start 2P): from 7px to 8px
- Sidebar name (Press Start 2P): from 7px to 8px
- Sidebar tagline: from 9px to 11px
- Panel body text: from 11.5px to 13px
- Panel section headings (Press Start 2P): from 7px to 8px
- Panel bullet items: from 11.5px to 13px
- Panel title (Lora): from 17px to 20px
- Panel date stamp: from 6px to 7px (Press Start 2P)
- Pixel buttons: from 10px to 12px
- Nav icons: from 18x18px to 20x20px
- Sidebar width: increase from 210px to 240px to accommodate larger text

---

## 2. Fix "about me (work)" opening copy

Remove the "hi, I'm Ivy!" sentence from the opening of the "about me (work)" panel. Replace the opening paragraph with:

"Communications grad from the University of Waterloo with a background in content production, publishing workflows, and cross-functional marketing. I like making things clear, well-timed, and actually useful for the people reading them."

(Keep everything else in this panel the same.)

---

## 3. Replace "work & projects" panel content entirely

Replace the current content of the work & projects panel with the following. Use the same section heading style (Press Start 2P, pink) for category headers, the same bullet/dash style for items, and include hyperlinks where URLs are provided (all links open in new tab):

---

Panel title: work & projects
Panel date: last updated march 2026
Opening line (italic, muted): "doing stuff and helping people is fun"

---

### web content @ digital extremes (warframe)

Player-facing content written and published on warframe.com during my co-op term (June–August 2025). Coordinated across development, art, community, and marketing teams to hit tight release windows.

– Countdown to TennoCon 2025 — multi-channel hype piece coordinating Twitch Drop logistics across three event days, community artist credits, and partner giveaways for a global playerbase
   Link: https://www.warframe.com/en/news/countdown-to-tennocon-2025-en

– TennoGen Isleweaver Available Now — community cosmetics spotlight cataloguing items across multiple creators with individual artist credits and storefront descriptions
   Link: https://www.warframe.com/en/news/tennogen-isleweaver-coming-soon

– Dog Days 2025 — seasonal event launch post bridging marketing and game comms: balance change communication, new reward breakdowns, accessibility improvements, and community artist credits
   Link: https://www.warframe.com/en/news/dog-days-2025

---

### social & game capture @ digital extremes (warframe)

Game capture and in-game content creation for @playwarframe on Instagram and TikTok (June–August 2025). Involved in shooting, staging, and producing short-form video and photo content.

– Fridgeframe — 444K views on Instagram · 258.3K on TikTok
   Link: https://www.instagram.com/reel/DMS9J63MTum/

– Qorvex x Plague Star — 351K views on Instagram · 236.5K on TikTok (released after my term ended, but this one was mine 🩷)
   Link: https://www.instagram.com/reel/DOHG6pqgtnk/

– Merulina Prime — 210K views on Instagram · 49.8K on TikTok
   Link: https://www.instagram.com/reel/DKc8d_OCHtd/

– Operator Hairstyles (Flare, Minerva, Velimir, Kaya) — my operator was used! · 143K views on Instagram · 21K on TikTok
   Link: https://www.instagram.com/reel/DLkir2LiGXC/

– TennoCon 2025 VA Collab — 155K views on Instagram · 103.1K on TikTok
   Link: https://www.instagram.com/reel/DMQPmvoCVpI/

– Qorvex x Pride Month — 85.2K views on Instagram · 31.4K on TikTok · gained real experience moderating comments sections on sensitive content
   Link: https://www.instagram.com/reel/DK2k_ScikGY/

– Valkyr Heirloom (TikTok exclusive) — 100.9K views on TikTok · no Instagram link available

– TennoCon 2025 Writing on the Wall — Instagram Story; that's my hand 🙂

---

### other

– this site — designed and built ivyzhao.ca from scratch (with a little help from Claude)

---

## 5. Inline video embeds

For the Valkyr Heirloom entry in the social & game capture section, embed the video file `valkyr-heirloom.mp4` as an inline `<video>` element directly below the entry text. Settings: autoplay off, controls on, muted off, max-width 100%, styled consistently with the panel aesthetic (subtle border, small border-radius matching pixel corner style).

For the TennoCon Writing on the Wall entry, embed `tennocon-writing-on-wall.mp4` the same way.

---

## 4. Remaining small fixes (carry these over from the previous batch)

- In "about me (personal)", change opening line from "hi! (or berry, if we met on discord)" to "hi, I'm Ivy! (or berry, if we met on discord)"
- In "resume" panel (under "more"), add resume PDF links: "resume (general)" links to "Ivy Zhao Resume.pdf" and "resume (games)" links to "Ivy Zhao Resume GI.pdf", both open in new tab (same as in the "about me (work)" panel)
