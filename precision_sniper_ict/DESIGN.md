---
name: Precision Sniper ICT
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#abd600'
  primary: '#ffffff'
  on-primary: '#283500'
  primary-container: '#c3f400'
  on-primary-container: '#556d00'
  inverse-primary: '#506600'
  secondary: '#ffb4aa'
  on-secondary: '#690003'
  secondary-container: '#c5020b'
  on-secondary-container: '#ffd2cc'
  tertiary: '#ffffff'
  on-tertiary: '#3a3000'
  tertiary-container: '#ffe16d'
  on-tertiary-container: '#776300'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4aa'
  on-secondary-fixed: '#410001'
  on-secondary-fixed-variant: '#930005'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max-width: 1440px
---

## Brand & Style

The design system is engineered for the high-stakes environment of institutional-grade trading signals. The brand personality is **Precise, Institutional, and Technical**, focusing on clarity under pressure and real-time execution. It avoids unnecessary fluff, favoring a sophisticated **Dark Mode** aesthetic that mirrors high-end trading terminals.

The style is a hybrid of **Minimalism and Glassmorphism**. We use deep obsidian voids for the base layer to reduce eye strain during long trading sessions, while active data containers utilize subtle backdrop blurs and micro-borders to appear "floated" above the market data stream. The interface communicates authority through high-contrast accents and technical density.

## Colors

The color strategy is strictly functional. **Neon Lime (#CCFF00)** is the primary action and bullish indicator, providing maximum luminosity against the **Deep Obsidian (#0B0E14)** background. **Electric Red (#FF3B30)** is reserved for bearish signals and critical risks. 

**Gold (#FFD700)** is used exclusively for "A+" institutional signals and premium tier status. Neutral tones are tiered: **Ghost White (#F8F9FA)** for high-priority data and **Slate Gray (#8E9AAF)** for metadata and labels. Interactive surfaces use **Charcoal Navy (#1A1D26)** with 60-80% opacity when glassmorphism effects are applied.

## Typography

This design system utilizes a dual-font approach to separate UI narrative from raw data. 

1.  **Inter** handles all interface copy, navigation, and headings. It provides a clean, neutral canvas that ensures high legibility.
2.  **JetBrains Mono** is used for all "Live Data" (price action, coordinates, timestamps, and trade sizes). The monospaced nature prevents "layout jump" as numbers tick in real-time.

Headlines should use tighter letter spacing for a more "locked-in" professional look. All data labels should use `label-caps` to distinguish them from the actual data values.

## Layout & Spacing

The layout is based on a **12-column fluid grid** for desktop and a **4-column grid** for mobile. We utilize a strict 4px baseline shift to ensure all technical elements align perfectly on the vertical axis.

- **Data Density:** Content should be densely packed but logically grouped. Use 8px (2 units) for related elements and 24px (6 units) for section breaks.
- **Sidebars:** Navigation is housed in a slim, collapsible 64px/240px sidebar to maximize the "Chart Estate."
- **Breakpoints:** Mobile (<768px), Tablet (768px-1199px), Desktop (>1200px). On mobile, data cards stack vertically; on desktop, they utilize a masonry or dashboard-style grid.

## Elevation & Depth

We avoid traditional heavy shadows in favor of **Tonal Layers and Glassmorphism**. 

1.  **Level 0 (Background):** Deep Obsidian (#0B0E14). No elevation.
2.  **Level 1 (Sub-surface):** Charcoal Navy (#1A1D26) with a 1px solid stroke (#2D3139).
3.  **Level 2 (Active Containers):** 60% opacity Charcoal Navy with a 20px Backdrop Blur. A subtle top-down inner glow (0.5px white at 10% opacity) simulates a glass edge.
4.  **Level 3 (Overlays/Modals):** Darker semi-transparent fill with a vibrant 1px border using the primary accent color (Neon Lime) to indicate focus.

Shadows, when used (e.g., on primary buttons), are high-spread, low-opacity "Neon Glows" matching the accent color.

## Shapes

The shape language is **Soft/Technical**. We use a `0.25rem` (4px) radius for most UI components (inputs, small buttons, badges) to maintain a sharp, precise feel. Larger containers and cards use `0.5rem` (8px). 

The goal is to avoid the "playful" look of highly rounded corners, opting instead for a structural, architectural appearance that feels like a piece of high-end hardware.

## Components

### Signal Grade Badges
High-contrast pill shapes. **Grade A+** uses a Gold background with Obsidian text. **Grade B-D** uses Slate Gray outlines with Mono typography.

### Data Cards
Utilize Level 2 elevation (Glassmorphism). The header of the card should feature the asset pair (e.g., XAUUSD) in Inter Bold, with the price in JetBrains Mono. 

### Signal Strength Meters
A horizontal segmented bar (5 segments). Active segments glow with Neon Lime; inactive segments stay at 10% opacity Slate Gray.

### Trade Class Indicators
- **Scalp:** Icon-only (Lightning bolt).
- **Day:** Text + Icon (Sun).
- **Strong:** Bold border weight.
- **Pyramid:** Layered icon stack.

### Buttons
- **Primary:** Solid Neon Lime, Obsidian text, uppercase Inter Bold.
- **Secondary:** Ghost White outline (1px), transparent background.
- **Ghost:** No background, Slate Gray text, appears on hover.

### Market State Tags
- **Trending:** Neon Lime pulse dot + "TRENDING" text.
- **Ranging:** Static Slate Gray dot + "RANGING" text.
- **Slowing:** Electric Red pulse dot + "SLOWING" text.