# ivyzhao.ca — Portfolio Site Design Spec

## Overview
Personal portfolio site for Ivy Zhao, a marketing & communications student at the University of Waterloo graduating in 2026. The site lives at `ivyzhao.ca`, hosted on GitHub Pages. The single file to build is `index.html` (with all CSS and JS inline). A separate `mobile.css` or media query block should handle mobile layout.

---

## Aesthetic Direction

**Core vibe:** Soft pixel-OS. A personal desktop operating system aesthetic inspired by *NEEDY STREAMER OVERLOAD* — pixel accents and chunky borders on a soft, warm, frosted base. Think: cozy Windows-meets-dreamy-pastel, not harsh retro.

**Key references:**
- *NEEDY STREAMER OVERLOAD* UI (pixel borders, OS window chrome, desktop metaphor)
- Helen Huang's portfolio at uses a notes-app sidebar layout (sidebar + main panel)
- Ivy's existing Carrd site: pink/green gradient, sparkle and heart motifs, frosted translucent cards, soft serif headings

**Palette:**
- Background: diagonal gradient `135deg`, from `#a8e6a3` (mint green, top-left) → `#c9e8c5` → `#e8ddd5` (warm neutral centre) → `#f2c4ce` → `#f4a8b8` (soft pink, bottom-right)
- Frosted card/panel: `rgba(255,255,255,0.42)` background, `backdrop-filter: blur(10px)`, `border: 2px solid rgba(255,255,255,0.68)`
- Accent pink: `#e07090`
- Accent green: `#5aaa6a`
- Heading colour: `#8b3a5a`
- Body text: `#4a3a42`
- Muted/secondary text: `#a09098`
- Pixel label colour: `#b05a7a`

**Typography:**
- Headings: `Lora` (Google Fonts), serif, italic, `font-size: 17–20px`, colour `#8b3a5a`
- Pixel labels / section headings / titlebar text: `Press Start 2P` (Google Fonts), `font-size: 6–8px`, colour `#b05a7a` or `#c07090`
- Body: system sans-serif, `font-size: 11.5–13px`, colour `#4a3a42`, `line-height: 1.7`

**Decorative details:**
- Scattered sparkles (`✦` `✧`) and hearts (`♡`) positioned absolutely across the gradient background, `pointer-events: none`, white at ~55–70% opacity
- Pixel corners: small `5×5px` white squares at the four corners of each panel (`position: absolute`, offset `-2px`)
- All custom icons are pixel-block style SVGs (see Icon Spec section below)

---

## Layout — Desktop

### Top Bar
- Full-width, `height: 28px`
- Background: `rgba(255,255,255,0.55)`, `backdrop-filter: blur(10px)`, `border-bottom: 2px solid rgba(255,255,255,0.7)`
- Left: site title `ivyzhao.ca` in Press Start 2P, `font-size: 6px`, colour `#b05a7a`
- Centre: tag pill `marketing & comms | available april 2026` in Press Start 2P, `font-size: 5px`, colour `#a09098`, with subtle border
- Right: three pixel-style window buttons (`_` `□` `✕`), `14×14px` each, bordered, non-functional decorative

### Sidebar
- `width: 210px`, fixed, does not scroll with main area
- Background: `rgba(255,255,255,0.42)`, `backdrop-filter: blur(12px)`, `border-right: 2px solid rgba(255,255,255,0.6)`
- **Header block** (top of sidebar, bordered bottom):
  - `ivy zhao` in Press Start 2P, `7px`, colour `#b05a7a`, line-height 1.7
  - `marketing & comms | available april 2026` in italic sans, `9px`, colour `#7a6b72`
- **Scrollable nav list** below header (thin custom scrollbar, pink-toned)
- Section labels (`pinned`, `more`, `archive`) in Press Start 2P `7px`, colour `#c07090`, padding `7px 12px 3px`
- Nav items: `padding: 6px 10px`, `font-size: 11px`, colour `#5a4a52`, `border-left: 3px solid transparent`
  - Hover/active: `background: rgba(255,255,255,0.5)`, `border-left: 3px solid #e07090`, text `#3a2a32`
  - Each item has an 18×18px custom SVG pixel icon (see below) + label

**Sidebar nav items (in order):**

*Pinned:*
1. 📓 `about me (work)` — pink journal icon
2. 🌿 `about me (personal)` — green pixel leaf icon
3. 📁 `work & projects` — white/grey pixel folder icon
4. 🍓 `in the now` — pixel heart-strawberry icon

*More:*
5. 📄 `resume` — white pixel document icon
6. ✉️ `contact` — pink pixel envelope icon

*Archive:*
- `now archive` — grey pixel archive box icon, functions as a **dropdown toggle**
- Dropdown reveals: `march 2026`, `feb 2026` (sub-items, indented, muted style)

### Main Area (Desktop)
- Takes remaining width after sidebar
- Padding: `12px` on all sides
- Gradient background shows through (no additional background)
- **Panels open here as floating draggable windows**

---

## Panel / Window Behaviour (Desktop)

Each sidebar item opens a **floating panel** in the main area. Rules:

- **All panels open at the same fixed starting position**: `top: 12px`, `left: 12px`, `width: calc(100% - 24px)` — snug with equal margins left and right, flush near top
- **Default height:** `320px`
- **Draggable:** user can drag via the titlebar to reposition anywhere in the main area
- **Resizable vertically only:** a resize handle at the bottom of each panel (`cursor: ns-resize`), styled as a dashed line with `···` dots. No horizontal resize.
- **Closable:** `✕` button in each panel's titlebar closes it (removes `.open` class)
- **Multiple panels can be open simultaneously** and stacked. Clicking a titlebar brings it to front (`z-index` management).
- Opening a panel always resets it to the top-left starting position and increments z-index to bring it to front.

**Panel structure:**
```
[ pixel corner TL ]                          [ pixel corner TR ]
[ titlebar: Press Start 2P label | ✕ button ]
[ scrollable body content                    ]
[ resize handle ··· ]
[ pixel corner BL ]                          [ pixel corner BR ]
```

**Titlebar:** `height: 22px`, `background: rgba(255,255,255,0.55)`, `border-bottom: 2px solid rgba(255,255,255,0.6)`, `cursor: grab`
**Panel border:** `2px solid rgba(255,255,255,0.68)`
**Panel background:** `rgba(255,255,255,0.42)`, `backdrop-filter: blur(10px)`

---

## Layout — Mobile

On screens `≤768px`:
- Top bar remains (simplified if needed)
- Sidebar becomes a **full-width stacked list** of nav items (no floating panels)
- Tapping a nav item navigates to a **new full-page view** showing just that panel's content (no sidebar visible)
- A back button / back arrow returns to the nav list
- No dragging, no floating windows — simple vertical scroll per section
- Archive dropdown still works as a toggle

---

## Panel Content

### `about me (work)`
Titlebar label: `about me (work version)`

```
[Lora italic heading] about me (work)
[pixel date] UW 2026 · available from april 2026

hi, I'm Ivy! Communications grad from Waterloo with a background in content,
marketing, and making things clear for the people reading them.

[section] currently:
– finishing my BA at Waterloo, exams done early April
– based in Markham, ON — open to remote roles
– looking for work in marketing, communications, or content

[section] experience:
– Content Marketing Coordinator @ Digital Extremes (Warframe) — player-facing content across web, social, and in-game channels
– HR Communications Co-op @ Toronto Police Service — internal comms, newsletters, onboarding materials, feedback tools
– National Education Specialist @ Manulife — retirement education materials, large-scale system transitions, training documentation

[dashed divider]
[pixel button] resume (general) ↗
[pixel button] resume (games) ↗
```

### `about me (personal)`
Titlebar label: `about me (personal)`

```
[Lora italic heading] about me (personal)
[pixel date] hi! (or berry, if we met on discord)

[section] games:
– 957 hours in Warframe, which I also got to work on!
– honourable mentions: Helldivers 2, BG3, Disco Elysium, Project Zomboid, Lethal Company, Sims, Spore
– Disco Elysium deserved better

[section] music:
– depends entirely on the day — somewhere between Laufey and late 90s kpop,
  with detours into vocaloid, mandopop, and Sabrina Carpenter

[section] other things:
– AAPI and intersectional feminist advocacy
– Sanrio, stuffed animals, cats, and cute things generally
– salmon sashimi and grapes with complete and unwavering devotion
– reading when the right thing finds me: bell hooks, game lore deep dives, the occasional isekai romance novel
```

### `work & projects`
Titlebar label: `work & projects`

```
[Lora italic heading] work & projects
[pixel date] things I've made and done

[section] digital extremes (warframe):
– player-facing content across web, social, and in-game channels
[project cards — placeholder for now, to be filled in later]

[section] other projects:
– this website (meta, I know)

[italic hint] more coming soon!
```

### `in the now`
Titlebar label: `in the now`

```
[small pixel tag] / now
[Lora italic heading] in the now...
[pixel date] last updated march 2026

[section] where I'm at:
– finishing my last term at Waterloo, exams done early April
– job searching (if you're hiring, hi 🍑)
– listening to Karencici on loop
– taking life day by day

[dashed divider]
[italic hint] inspired by Derek Sivers and the /now movement
```

### `resume`
Titlebar label: `resume`

```
[Lora italic heading] resume
[pixel date] updated 2026

[pixel button] resume (general) ↗   [pixel button] resume (games) ↗
```
*(Buttons link to PDF files — URLs to be added later)*

### `contact`
Titlebar label: `contact`

```
[Lora italic heading] say hi
[pixel date] always happy to chat

[pixel button] email ↗
[pixel button] linkedin ↗
```
*(Links to be added later)*

---

## Icon Spec — Pixel Block Style

All icons are inline SVG, `18×18px viewBox`, built from `2×2px` rounded rectangles (`rx="0.4"`). No strokes on individual blocks — colour variation creates shading/depth.

### Journal (about me — work)
Pink and white journal with a corner tab. Body: `rgba(255,200,215,0.7)` / `#f4a8b8`. Lines inside representing text: `#e07090` at varying opacities. Corner tab top-right: `#e07090`.

### Leaf (about me — personal)
AC New Horizons-style pixel leaf. Rounded pixel blocks in 3 green shades: dark `#5aaa6a`, mid `#7aca7a`, light `#9ade8a`. Diamond/oval leaf shape. Brown stem `#8b6a3a` at bottom.

### Folder (work & projects)
White/grey pixel folder. Tab top-left. Body blocks: `#ede8ea` (light), `#d8d0d4` (border/edge). No colour — purely white-grey tones.

### Heart Strawberry (in the now)
Heart-shaped strawberry in pixel blocks. Body: dark `#e05050`, mid `#f07070`, highlight `#ffaaaa`. Green pixel leaf/stem top: `#5aaa6a`. Heart shape achieved by pixel arrangement (no diagonal pixels — pure grid).

### Resume / Document
White pixel document with folded corner top-right. Body: `#ede8ea`. Corner fold: `#e07090`. Interior lines representing text: `#c07090` (title line, full width) and `#a09098` (body lines, varying widths, lower opacity).

### Envelope (contact)
Pink pixel envelope. Body: `#f4a8b8` outer blocks. V-chevron inside formed by `#e07090` diagonal pixel blocks stepping down toward centre.

### Archive Box (now archive)
Grey pixel archive box with tab/lid. All grey-toned: `#c0b8bc`, `#a8a0a4`, `#d8d4d6`. Slightly muted/faded versus the other icons.

---

## Pixel Buttons

```css
.pixel-btn {
  display: inline-block;
  padding: 5px 11px;
  margin: 3px 3px 0 0;
  font-size: 10px;
  color: #7a3a5a;
  background: rgba(255,255,255,0.6);
  border: 2px solid rgba(200,150,170,0.6);
  cursor: pointer;
  font-family: sans-serif;
  border-radius: 0; /* intentionally square — pixel aesthetic */
}
.pixel-btn:hover {
  background: rgba(255,255,255,0.85);
  border-color: #e07090;
}
```

---

## Section Headings (inside panels)

```css
.section-heading {
  font-family: 'Press Start 2P', monospace;
  font-size: 7px;
  color: #c07090;
  margin: 12px 0 7px;
  letter-spacing: 0.5px;
}
```

## Bullet Items (inside panels)

Each bullet item is a flex row with `–` in `#c07090` as the bullet, followed by body text.

---

## Google Fonts

Load both of these in the `<head>`:
```
https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Lora:ital,wght@0,400;0,500;1,400&display=swap
```

---

## Files

- `index.html` — entire site (HTML + CSS + JS all inline, single file)
- Resume PDFs and any linked assets to be added later

---

## Notes for Claude Code

- Build everything into a single `index.html` with `<style>` and `<script>` tags inline
- Do not use any frameworks (no React, no Vue) — vanilla HTML/CSS/JS only
- Mobile layout uses media queries inside the same file, no separate stylesheet needed
- All SVG icons should be inlined directly in the HTML
- Sparkles and hearts are plain Unicode characters positioned absolutely
- GitHub Pages serves `index.html` at the root — no build step needed
- Resume PDF links and contact links are placeholders for now (`href="#"`)
- The site should look good at 1280px+ wide on desktop
- Test that drag, resize, close, and z-index stacking all work correctly
