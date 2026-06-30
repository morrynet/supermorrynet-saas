---
name: Obsidian Aegis
colors:
  surface: '#111318'
  surface-dim: '#111318'
  surface-bright: '#37393e'
  surface-container-lowest: '#0c0e12'
  surface-container-low: '#1a1c20'
  surface-container: '#1e2024'
  surface-container-high: '#282a2e'
  surface-container-highest: '#333539'
  on-surface: '#e2e2e8'
  on-surface-variant: '#b9cbbd'
  inverse-surface: '#e2e2e8'
  inverse-on-surface: '#2f3035'
  outline: '#849588'
  outline-variant: '#3a4a3f'
  surface-tint: '#00e290'
  primary: '#f5fff5'
  on-primary: '#003920'
  primary-container: '#00ffa3'
  on-primary-container: '#007146'
  inverse-primary: '#006d43'
  secondary: '#b9f1ff'
  on-secondary: '#00363f'
  secondary-container: '#00e0ff'
  on-secondary-container: '#005f6d'
  tertiary: '#fffbff'
  on-tertiary: '#621100'
  tertiary-container: '#ffd7cd'
  on-tertiary-container: '#bc2b00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#52ffac'
  primary-fixed-dim: '#00e290'
  on-primary-fixed: '#002111'
  on-primary-fixed-variant: '#005231'
  secondary-fixed: '#a5eeff'
  secondary-fixed-dim: '#00daf8'
  on-secondary-fixed: '#001f25'
  on-secondary-fixed-variant: '#004e5a'
  tertiary-fixed: '#ffdad2'
  tertiary-fixed-dim: '#ffb4a2'
  on-tertiary-fixed: '#3c0700'
  on-tertiary-fixed-variant: '#8a1d00'
  background: '#111318'
  on-background: '#e2e2e8'
  surface-variant: '#333539'
typography:
  display-secure:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  code-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
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
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-stakes institutional security and cryptographic precision. It targets security analysts, DevOps engineers, and digital sovereign entities who require immediate visual confirmation of system integrity. 

The visual style is a fusion of **Glassmorphism** and **High-Contrast Bold**. It utilizes a deep, multi-layered obsidian environment where high-visibility neon accents slice through the darkness to signal status. The emotional response is one of total control, impenetrable defense, and technical superiority. Every element is designed to feel like a hardened tactical interface—heavy, intentional, and crystalline.

## Colors

The palette is anchored by a "Deep Obsidian" (`#0A0C10`) base to maximize contrast and reduce eye strain during extended surveillance. 

- **Protected (Primary):** A piercing Neon Mint used for healthy states and successful encryption.
- **Encrypted:** A deep Electric Violet used for specialized data-at-rest indicators.
- **Alert:** A high-visibility Cyber Yellow for non-critical warnings and policy violations.
- **Locked (Tertiary):** A pure Radiation Red for active threats and system lockdowns.

All accents must maintain a high luminosity to "glow" against the dark background, simulating an active terminal display.

## Typography

This design system uses a triple-font hierarchy to balance futuristic aesthetics with technical utility. 

**Space Grotesk** is used for primary headings to give the interface a geometric, cutting-edge feel. **Geist** handles all body copy, providing a clean, minimal, and highly legible experience for data-dense environments. **JetBrains Mono** is reserved for status labels, hashes, and security metadata, reinforcing the developer-centric, "hardened" nature of the product. All labels should be uppercase with increased tracking for maximum readability in low-light conditions.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to ensure that technical data points remain in predictable screen locations. We utilize a 12-column grid on desktop with generous 24px gutters to prevent information density from becoming overwhelming.

Spacing is strictly derived from a 4px base unit. Component internal padding should be expansive (typically 16px or 24px) to create "breathing room" around critical security metrics. On mobile, the grid collapses to 4 columns, and margins shrink to 16px to prioritize the central "Secure Container" view.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and **Tonal Layering**. Instead of traditional shadows, we use:

1.  **Backdrop Blurs:** High-elevation surfaces (like modals or Data Shields) use a 20px blur with a 10% white tint to pull away from the obsidian base.
2.  **Inner Glows:** Rather than drop shadows, components use subtle 1px inner borders (strokes) in a low-opacity version of the state color (e.g., 20% Neon Mint) to define edges.
3.  **Z-Axis Stacking:** 
    *   *Level 0:* Obsidian Base (`#0A0C10`).
    *   *Level 1:* Surface Layer (1px border, 5% lighter than base).
    *   *Level 2:* Secure Container (Backdrop blur, frosted effect).

## Shapes

The design system utilizes **Soft** geometry (0.25rem / 4px base radius). This specific corner radius is chosen to feel more "engineered" and architectural than fully rounded "consumer" apps, while avoiding the aggressive harshness of pure sharp corners. 

Buttons and input fields maintain this 4px radius. The "Secure Container" can scale up to `rounded-lg` (8px) for a slightly more framed, protective appearance.

## Components

### Secure Container
The signature component of this design system. It features a deep frosted-glass background (Backdrop Blur: 24px) and a 1px solid border using the `Protected` neon color at 30% opacity. It acts as the primary housing for sensitive data.

### Buttons
- **Primary:** Solid `Protected` mint background with black text. No shadows; instead, use a 4px outer "glow" on hover using the primary color at 50% opacity.
- **Ghost:** Transparent background with a 1px `Secondary` border.

### Data Shield Icons
A custom set of monolinear icons with a 2px stroke width. Icons representing active security (locks, shields, eyes) should utilize a "duotone" glow effect, where the primary stroke is white and a secondary "echo" stroke sits behind it in the state color (e.g., Alert Yellow).

### Input Fields
Dark backgrounds (`#000000`) with a bottom-only border in `Secondary` cyan. Upon focus, the border transitions to the `Protected` mint color, and the "Code Label" above the field pulses once.

### Security Chips
Small, high-contrast badges used to indicate encryption protocols (e.g., AES-256). These use the `jetbrainsMono` font in all-caps, with a background color matching the security state at 15% opacity and a text color at 100% opacity.