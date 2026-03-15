# Claude Code prompt 2 — polish and fixes for ivyzhao.ca

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

## 2. Topbar size increases

- Increase topbar height from 28px to 34px
- Increase `© ivy zhao 2026` text from 6px to 8px (Press Start 2P)
- Increase the `marketing & comms | available april 2026` pill text from 5px to 7px (Press Start 2P)
- Increase the three topbar window buttons from 14×14px to 16×16px
- Increase panel titlebar height from 22px to 26px
- Increase panel titlebar label text from 6px to 8px (Press Start 2P)

---

## 3. Fix video sizing

The video files `valkyr-heirloom.mp4` and `tennocon-writing-on-wall.mp4` are already embedded in the work & projects panel but displaying too large. Fix their sizing:
- Cap video width at 320px max
- Centre them within the panel
- Keep controls on, autoplay off, muted off
- Add a subtle border and small border-radius consistent with the panel aesthetic
- Display inline below their respective entry text

---

## 4. Fix resume PDF link encoding

The resume links currently have spaces in the filenames which can cause broken links. Update both instances (in "about me (work)" and "resume" panels) to use URL-encoded filenames:
- `Ivy%20Zhao%20Resume.pdf` instead of `Ivy Zhao Resume.pdf`
- `Ivy%20Zhao%20Resume%20GI.pdf` instead of `Ivy Zhao Resume GI.pdf`

---

## 5. Remove redundant line in "about me (work)"

The panel currently shows "UW 2026 · available from april 2026" as a standalone line after the date stamp. Remove this line — the information is already covered in the bio paragraph and the topbar.

---

## 6. Add selfie photo to hero panel

Add a circular profile photo to the "hello :)" hero panel. The image file is called `ivy-photo.png` and is in the repo root.

- Display it as a circle (border-radius: 50%), approximately 120px wide
- Centre it horizontally in the panel
- Place it above the "ivy zhao" Lora heading
- Add a subtle border: `2px solid rgba(255,255,255,0.6)` to match the frosted panel aesthetic
- No drop shadow
