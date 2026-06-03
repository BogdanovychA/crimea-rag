# Design System Inspired by Crimea is Ukraine

## 1. Visual Theme & Atmosphere

This design system embodies a solemn, archival aesthetic rooted in historical documentation and national identity. The atmosphere balances gravitas with clarity—evoking the weight of historical records while maintaining accessibility through clean typography and deliberate whitespace. Deep darks and pure whites create stark contrast, reflecting the documentary nature of the platform. The occasional accent of teal introduces a contemporary flourish, humanizing the otherwise formal archive. The overall mood is serious yet inviting, designed to present historical evidence with transparency and respect. Typography-forward layouts emphasize text hierarchy, and minimal ornamentation allows historical imagery and primary sources to remain the focal point.

**Key Characteristics**
- High-contrast monochromatic palette with selective accent color
- Archival, documentary visual language
- Elegant, restrained typography hierarchy
- Emphasis on historical authenticity and credibility
- Clean, linear layout with deliberate negative space
- Minimalist approach to decoration and embellishment

## 2. Color Palette & Roles

### Primary
- **Primary Interactive** (`#0000EE`): Hyperlinks, primary call-to-action elements, and interactive states (used extensively throughout navigation and content)

### Accent Colors
- **Accent Teal** (`#50E3C2`): Supporting highlights, subtle UI accents, and secondary interactive states

### Interactive
- **Text Link Dark** (`#0F0F0F`): Link text on light backgrounds, highest contrast interactive content
- **Button Text Light** (`#FFFFFF`): Text color for buttons on dark backgrounds

### Neutral Scale
- **Dark Charcoal** (`#141414`): Primary text, headings, and dark UI backgrounds (highest usage)
- **Off-Black** (`#000000`): Deep shadows, borders, and maximum contrast elements
- **Very Dark Gray** (`#0F0F0F`): Secondary text, subtle UI elements
- **Medium Gray** (`#676767`): Tertiary text, disabled states, and muted content
- **Light Gray** (`#D8D8D8`): Borders, dividers, and subtle backgrounds
- **Very Light Gray** (`#ECECEC`): Background tints, secondary surface color
- **Dark Blue-Gray** (`#212736`): Navigation backgrounds, sidebar fill, secondary surfaces
- **Charcoal Tone** (`#333232`): Border accents and fine details

### Surface & Borders
- **Pure White** (`#FFFFFF`): Primary background, card surfaces, content containers
- **Off-White Gray** (`#ECECEC`): Secondary background tint, inactive states
- **Light Border** (`#D8D8D8`): Subtle dividers and component borders

## 3. Typography Rules

### Font Family
- **Primary**: Roboto, sans-serif
- **Fallback Stack**: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|---|---|
| Display / Hero | Roboto | 104px | 700 | 124.8px | 0px | Page titles, major headings |
| Body Paragraph | Roboto | 20px | 300 | 24px | 0px | Primary content text, descriptive copy |
| UI Text / Span | Roboto | 15px | 400 | normal | 0px | Button labels, labels, captions |
| Navigation Link | Roboto | 15px | 300 | 22.5px | 0px | Menu items, secondary navigation |
| Link / Anchor | Roboto | 15px | 300 | normal | 0px | Inline links, reference text |

### Principles
- **Contrast Through Weight**: Bold (700) for emphasis; light (300) for supporting content
- **Generous Line Height**: Enhances readability in longer-form archival content
- **No Letter Spacing**: Maintains the clean, compact aesthetic
- **Size Restraint**: Limited palette of 3 sizes ensures visual coherence
- **Roboto Consistency**: Single family used throughout for unified, modern professionalism

## 4. Component Stylings

### Buttons

**Default Button (Dark Text)**
- `background-color`: `rgba(0, 0, 0, 0)` (transparent)
- `color`: `#141414`
- `font-size`: `15px`
- `font-weight`: `400`
- `font-family`: `Roboto`
- `padding`: `12px 8px`
- `border-radius`: `0px`
- `border`: `0px none`
- `box-shadow`: `none`
- `line-height`: `normal`
- **Hover**: Opacity to `0.7`, maintains text color `#141414`
- **Active**: Opacity to `0.5`

**Default Button (Light Text)**
- `background-color`: `rgba(0, 0, 0, 0)` (transparent)
- `color`: `#FFFFFF`
- `font-size`: `15px`
- `font-weight`: `400`
- `font-family`: `Roboto`
- `padding`: `12px 8px`
- `border-radius`: `0px`
- `border`: `0px none`
- `box-shadow`: `none`
- `line-height`: `normal`
- **Hover**: Opacity to `0.8`
- **Active**: Opacity to `0.6`

### Links

**Primary Link**
- `background-color`: `rgba(0, 0, 0, 0)` (transparent)
- `color`: `#0F0F0F`
- `font-size`: `15px`
- `font-weight`: `300`
- `font-family`: `Roboto`
- `padding`: `0px 0px`
- `border-radius`: `0px`
- `border`: `0px none`
- `box-shadow`: `none`
- `line-height`: `normal`
- **Hover**: Underline applied, color remains `#0F0F0F`
- **Visited**: Color to `#676767`
- **Active**: Color to `#0000EE`

**Interactive Link (Blue)**
- `background-color`: `rgba(0, 0, 0, 0)` (transparent)
- `color`: `#0000EE`
- `font-size`: `15px`
- `font-weight`: `300`
- `font-family`: `Roboto`
- `padding`: `0px 0px`
- `border-radius`: `0px`
- `border`: `0px none`
- `box-shadow`: `none`
- `line-height`: `normal`
- **Hover**: Opacity to `0.8`, underline applied
- **Active**: Opacity to `0.6`

### Navigation

**Navigation Default**
- `background-color`: `rgba(0, 0, 0, 0)` (transparent)
- `color`: `#141414`
- `font-size`: `15px`
- `font-weight`: `300`
- `font-family`: `Roboto`
- `padding`: `0px 0px`
- `border-radius`: `0px`
- `border`: `0px none`
- `box-shadow`: `none`
- `width`: `100%`
- `line-height`: `22.5px`
- **Hover**: Color to `#0000EE`, text underline
- **Active**: Color to `#0000EE`, font-weight to `400`

**Navigation Container**
- `background-color`: `#212736`
- `padding`: `20px 40px`
- `display`: `flex`
- `gap`: `32px`
- `width`: `100%`

### Cards & Containers

**Archive Card**
- `background-color`: `#FFFFFF`
- `border`: `1px solid #D8D8D8`
- `border-radius`: `0px`
- `padding`: `32px 32px`
- `box-shadow`: `none`
- **Hover**: Border color to `#141414`, slight opacity shift

**Section Container**
- `background-color`: `#FFFFFF`
- `padding`: `40px 40px`
- `margin-bottom`: `52px`
- `width`: `100%`

**Dark Background Container**
- `background-color`: `#141414`
- `color`: `#FFFFFF`
- `padding`: `100px 40px`

## 5. Layout Principles

### Spacing System

Base unit: **4px**

**Scale with contexts:**
- `8px`: Micro spacing, internal padding
- `12px`: Button padding, small gaps
- `16px`: Standard padding, tight spacing
- `20px`: Medium padding, section gaps
- `32px`: Card padding, component spacing
- `40px`: Container padding, section sides
- `52px`: Significant gaps between sections
- `100px`: Major section separation
- `120px`: Hero section vertical spacing
- `200px`: Full-width padding edge cases

### Grid & Container

- **Max Width**: No explicit max-width constraint; full-width sections with internal padding
- **Column Strategy**: Flexible grid using CSS Grid or Flexbox; typically 1–3 columns depending on content type
- **Section Pattern**: Full-width containers with `40px` horizontal padding on desktop; archive cards use `32px` internal padding
- **Hero Section**: Full viewport height with centered text, `120px` vertical rhythm

### Whitespace Philosophy

Whitespace is treated as a design element, not mere emptiness. Generous padding around text blocks and cards ensures content breathes. Vertical rhythm is established through consistent `52px` section breaks. Margins are used to separate distinct content blocks; padding creates internal breathing room. This approach creates a calm, archival aesthetic appropriate to historical documentation.

### Border Radius Scale

- `0px`: All components (buttons, cards, inputs, containers)
- **Philosophy**: Sharp, rectilinear edges reinforce documentary and archival aesthetic; clean lines evoke formal records and official documentation

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Ground | No shadow | Card backgrounds, default surfaces |
| Raised (Hover) | `0px 2px 8px rgba(0, 0, 0, 0.12)` | Interactive cards on hover, lifted buttons |
| Elevated | `0px 4px 16px rgba(0, 0, 0, 0.15)` | Modals, overlays, dropdown menus |
| High | `0px 8px 24px rgba(0, 0, 0, 0.20)` | Floating elements, emphasized modals |

**Shadow Philosophy**: Minimal elevation is used sparingly. Most surfaces are flat with `box-shadow: none`. Shadows appear only on interactive hover states or temporary overlays to indicate depth and interactivity. This restraint maintains the serious, archival character while providing subtle affordance cues for interactive elements.

## 7. Do's and Don'ts

### Do
- Use `#141414` for primary headings and body text on white backgrounds
- Apply `#0000EE` exclusively to interactive elements (links, active navigation)
- Maintain `0px` border radius on all components for consistency
- Implement generous padding (`32px` to `40px`) around content to create visual breathing room
- Use `15px` font size for UI text and navigation labels
- Stack sections vertically with `52px` margins between major content blocks
- Employ `#FFFFFF` and `#ECECEC` as primary background colors
- Maintain light weight (`300`) in body text for elegant readability
- Reserve bold weight (`700`) for display headings only
- Use `#50E3C2` teal sparingly as accent highlights

### Don't
- Do not use rounded corners; maintain sharp `0px` border radius throughout
- Do not mix multiple typeface families; Roboto is the sole font family
- Do not apply box shadows to standard UI elements; reserve shadows for hover states
- Do not exceed `104px` for heading sizes outside hero sections
- Do not use colors outside the defined palette; no custom or brand colors beyond the 11 specified
- Do not apply letter spacing; maintain `0px` for all typography
- Do not use `#212736` on light backgrounds; reserve for dark UI elements
- Do not create narrow padding below `12px` for interactive elements
- Do not apply opacity changes to text; use color substitution instead
- Do not place interactive elements without sufficient padding (`12px` minimum)

## 8. Responsive Behavior

### Breakpoints

| Breakpoint | Width | Key Changes |
|-----------|-------|-----------|
| Mobile | 320px–599px | Single column, `20px` horizontal padding, `15px` font for body, `52px` h2, touch targets `44px` min |
| Tablet | 600px–1023px | 2-column card layouts, `32px` padding, `80px` h2, stacked navigation |
| Desktop | 1024px+ | 3-column archive layouts, `40px` padding, `104px` h2, full navigation menu |
| Large Desktop | 1440px+ | max-width container at `1400px` center-aligned, increased section spacing to `100px` |

### Touch Targets

- **Minimum Height**: `44px` for all buttons and clickable elements
- **Minimum Width**: `44px` for small buttons
- **Padding Around Targets**: `8px` minimum separation between interactive elements
- **Link Text**: Font size remains `15px` but padded to `44px` total height on mobile

### Collapsing Strategy

- **Hero Section**: Font size scales from `52px` (mobile) → `104px` (desktop); padding reduces from `40px` (mobile) → `200px` (desktop edge-to-edge)
- **Cards**: Full-width single column on mobile; 2-column grid on tablet; 3-column on desktop
- **Navigation**: Vertical stacked menu on mobile with `16px` gaps; horizontal flex layout on desktop with `32px` gaps
- **Body Text**: Remains `20px` on desktop but may reduce to `16px` on mobile for space efficiency
- **Section Padding**: `20px` horizontal on mobile; `40px` on tablet/desktop

## 9. Agent Prompt Guide

### Quick Color Reference

- **Primary CTA / Interactive**: Blue (`#0000EE`)
- **Background (Primary)**: White (`#FFFFFF`)
- **Background (Secondary)**: Very Light Gray (`#ECECEC`)
- **Background (Dark UI)**: Dark Charcoal (`#141414`)
- **Navigation Background**: Dark Blue-Gray (`#212736`)
- **Heading / Primary Text**: Dark Charcoal (`#141414`)
- **Body / Secondary Text**: Dark Charcoal (`#141414`)
- **Tertiary / Muted Text**: Medium Gray (`#676767`)
- **Borders / Dividers**: Light Gray (`#D8D8D8`)
- **Accent Highlight**: Teal (`#50E3C2`)
- **Deep Shadow / Maximum Contrast**: Off-Black (`#000000`)

### Iteration Guide

1. **Every interactive element uses Roboto `15px` weight `400` with transparent background unless explicitly styled as a filled button.**

2. **Primary text headings are Roboto `104px` weight `700` with line-height `124.8px`; body is `20px` weight `300` with line-height `24px`.**

3. **All components have `0px` border-radius; sharp edges are mandatory.**

4. **Links are `#0000EE` for active/primary interactive; `#0F0F0F` for secondary links; underline appears on hover.**

5. **Navigation items are `15px` weight `300` on `#212736` dark background; change color to `#0000EE` on hover and increase weight to `400` when active.**

6. **Card components use `32px` padding, white background (`#FFFFFF`), `1px solid #D8D8D8` border, and no shadow by default.**

7. **Section containers have `40px` horizontal padding and `52px` vertical separation; hero sections use `100px` to `120px` vertical padding.**

8. **Box shadows are applied only to interactive hover states (e.g., `0px 2px 8px rgba(0, 0, 0, 0.12)`) or temporary overlays; default surfaces have `box-shadow: none`.**

9. **Responsive design: mobile breakpoint at `600px` uses `20px` padding and single-column layouts; desktop at `1024px` uses `40px` padding and multi-column grids.**

10. **Accent teal (`#50E3C2`) is used sparingly for highlights or secondary interactive states; never as primary text or background.**
