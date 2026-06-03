# Design System Inspired by Crimea is Ukraine

## 1. Visual Theme & Atmosphere

This design system embodies a solemn yet compelling archival experience, rooted in historical documentation and national remembrance. The aesthetic combines dark, authoritative backgrounds with crisp white typography and strategic blue accents, creating a sense of gravitas and trustworthiness. The visual language emphasizes clarity and accessibility across extensive content repositories, using minimal decoration to ensure information hierarchy remains paramount. Geometric restraint and generous whitespace reflect institutional authority while maintaining emotional resonance around cultural preservation and political significance.

**Key Characteristics**

- Dark-dominant color scheme with high-contrast white type for readability and emphasis
- Minimal border radius and shadow effects—mostly sharp edges reflecting archival precision
- Generous vertical spacing between content sections for mental breathing room
- Blue accent palette suggesting official, institutional trust
- Large, bold typography at hero scale for impact on landing moments
- Card-based content organization for modular information architecture
- Subtle gradient overlays on hero imagery for text legibility
- Navigation anchored to dark header with white text for persistent orientation

## 2. Color Palette & Roles

### Primary

- **Hyperlink Blue** (`#0000EE`): Primary interactive element, links, and secondary CTAs; most frequently used accent across the interface
- **Official Blue** (`#4287FF`): Secondary blue for button states and elevated interactive focus
- **Deep Blue** (`#303FA1`): Tertiary blue for hover states and deeper interactive feedback
- **Slate Blue** (`#526CFE`): Tertiary accent for decorative elements and auxiliary interactive states
- **Muted Blue** (`#5D6CC0`): Soft blue for secondary UI elements and reduced-emphasis interactions

### Neutral Scale

- **Off-Black** (`#141414`): Primary text color; dominant background for hero and navigation sections; highest contrast base
- **Pure Black** (`#000000`): Intense text emphasis and borders where maximum contrast is required
- **Deep Charcoal** (`#0F0F0F`): Secondary background tint; near-black for subtle differentiation
- **Dark Gray** (`#212736`): Secondary text and muted interface elements
- **Medium Gray** (`#676767`): Tertiary text, disabled states, and secondary copy
- **Light Gray** (`#D8D8D8`): Subtle dividers and light borders
- **Off-White** (`#ECECEC`): Card backgrounds and light surface tints
- **Pure White** (`#FFFFFF`): Primary background, card surfaces, and maximum contrast overlays
- **Whisper White** (`#F5F5F5`): Minimal surface lift for very subtle layering

### Surface & Borders

- **Card Border** (`#D8D8D8`): Thin borders separating white card content from light backgrounds
- **Light Surface** (`#ECECEC`): Soft background for card containers and subtle surface elevation

### Semantic / Status

- **Error Red** (`#D52A2A`): Critical alerts, error messages, and destructive actions requiring immediate attention
- **Warning Yellow** (`#FFFF00`): Caution indicators and warning states demanding user awareness

## 3. Typography Rules

### Font Family

**Primary:** Roboto (300, 400, 700 weights) with fallback stack: `Roboto, system-ui, -apple-system, sans-serif`

**Monospace:** Roboto Mono (400, 700 weights) for code blocks and technical content with fallback: `Roboto Mono, 'Courier New', monospace`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|---|---|---|---|---|---|---|
| Display / H1 | Roboto | 104px | 700 | 115px | 0px | Hero headlines; maximum impact for page titles |
| Heading / H2 | Roboto | 36px | 700 | 44px | 0px | Section headings; moderate emphasis |
| Heading / H3 | Roboto | 24px | 700 | 28px | 0px | Subsection titles and card titles |
| Heading / H4 | Roboto | 20px | 700 | 24px | 0px | Minor headings and prominent labels |
| Body / P | Roboto | 20px | 300 | 28px | 0px | Primary running text; generously sized for readability |
| Secondary / Caption | Roboto | 15px | 300 | 19.5px | 0px | Metadata, list items, and supporting text |
| Link / Inline | Roboto | 12.8px | 300 | 24px | 0px | Hyperlinked text within body content |
| Button / CTA | Roboto | 20px | 400 | normal | 0px | Call-to-action labels; semi-bold for prominence |
| Input / Form | Roboto | 13.3333px | 400 | normal | 0px | Form field placeholders and input text |
| Code / Monospace | Roboto Mono | 14px | 400 | 20px | 0px | Technical content and code samples |

### Principles

- **Generous sizing:** Base body text at `20px` ensures accessibility for long-form historical content and older user demographics
- **Light-weight body:** 300-weight Roboto on body text reduces visual density and creates elegant, approachable reading experience
- **Bold headings:** 700-weight headings provide clear information hierarchy and visual anchors
- **Line height priority:** 1.4x–1.5x multipliers ensure ample vertical rhythm, critical for dense archival text
- **Minimal letter-spacing:** Default spacing maintains Roboto's inherent legibility; custom spacing avoided except where brand requires
- **Scale relationships:** Heading sizes follow a consistent 1.44–1.67x multiplier for harmonious visual progression

## 4. Component Stylings

### Buttons

#### Primary Button

- **Background:** `#141414`
- **Text Color:** `#FFFFFF`
- **Font Size:** `15px`
- **Font Weight:** `700`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `16px 32px`
- **Border Radius:** `0px`
- **Border:** `1px solid #141414`
- **Box Shadow:** `none`
- **Height:** `58px`
- **Line Height:** `24px`
- **Hover State:** Background `#0F0F0F`, Border `1px solid #0F0F0F`
- **Active State:** Background `#000000`, Border `1px solid #000000`
- **Disabled State:** Background `#676767`, Border `1px solid #676767`, Text `#ECECEC`, Cursor `not-allowed`

#### Secondary Button (Ghost)

- **Background:** `transparent`
- **Text Color:** `rgba(0, 0, 0, 0.54)`
- **Font Size:** `14px`
- **Font Weight:** `400`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `8px 16px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `rgba(0, 0, 0, 0.1) 0px 4px 10px 0px, rgba(0, 0, 0, 0.25) 0px 0px 1px 0px`
- **Height:** `40px`
- **Line Height:** `normal`
- **Hover State:** Background `#ECECEC`, Text Color `rgba(0, 0, 0, 0.87)`
- **Active State:** Background `#D8D8D8`, Text Color `#000000`

#### Icon Button

- **Background:** `transparent`
- **Text Color:** `rgba(0, 0, 0, 0.54)`
- **Font Size:** `20px`
- **Font Weight:** `400`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `0px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `none`
- **Height:** `24px`
- **Width:** `24px`
- **Line Height:** `normal`
- **Hover State:** Text Color `rgba(0, 0, 0, 0.87)`

### Cards & Containers

#### White Card with Border

- **Background:** `#FFFFFF`
- **Text Color:** `#141414`
- **Font Size:** `20px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `32px`
- **Border Radius:** `0px`
- **Border:** `1px solid #D8D8D8`
- **Box Shadow:** `none`
- **Min Height:** `530px`
- **Line Height:** `28px`
- **Hover State:** Border `1px solid #ECECEC`, Shadow `rgba(0, 0, 0, 0.08) 0px 2px 6px 0px`

#### Light Gray Card

- **Background:** `#ECECEC`
- **Text Color:** `#141414`
- **Font Size:** `20px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `0px`
- **Border Radius:** `0px`
- **Border:** `1px solid #ECECEC`
- **Box Shadow:** `none`
- **Height:** `180px`
- **Line Height:** `24px`

#### Content Container

- **Background:** `transparent`
- **Text Color:** `#141414`
- **Font Size:** `20px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `0px 0px 52px 0px`
- **Border Radius:** `0px`
- **Border:** `none`
- **Box Shadow:** `none`
- **Line Height:** `28px`

### Inputs & Forms

#### Text Input

- **Background:** `transparent`
- **Text Color:** `#FFFFFF`
- **Font Size:** `15px`
- **Font Weight:** `400`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `1px 44px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `none`
- **Height:** `36px`
- **Line Height:** `normal`
- **Placeholder Color:** `rgba(255, 255, 255, 0.6)`
- **Focus State:** Border `1px solid #4287FF`, Box Shadow `0px 0px 0px 2px rgba(66, 135, 255, 0.2)`
- **Error State:** Border `1px solid #D52A2A`, Box Shadow `0px 0px 0px 2px rgba(213, 42, 42, 0.15)`

### Navigation

#### Header Navigation

- **Background:** `transparent`
- **Text Color:** `#FFFFFF`
- **Font Size:** `20px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `0px 4px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `rgba(0, 0, 0, 0.1) 0px 0px 4px 0px, rgba(0, 0, 0, 0.2) 0px 4px 8px 0px`
- **Height:** `48px`
- **Line Height:** `28px`
- **Hover State:** Text Color `#4287FF`
- **Active State:** Text Color `#0000EE`, Border Bottom `2px solid #0000EE`

#### Link Buttons in Nav

- **Background:** `rgba(0, 0, 0, 0.87)`
- **Text Color:** `#FFFFFF`
- **Font Size:** `12.8px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `6px 10px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `none`
- **Height:** `36px`
- **Line Height:** `24px`
- **Hover State:** Background `rgba(0, 0, 0, 1)`, Text Color `#4287FF`

#### Text Link (Inline)

- **Background:** `transparent`
- **Text Color:** `#FFFFFF`
- **Font Size:** `20px`
- **Font Weight:** `300`
- **Font Family:** `Roboto, system-ui, sans-serif`
- **Padding:** `8px 8px`
- **Border Radius:** `0px`
- **Border:** `0px none`
- **Box Shadow:** `none`
- **Height:** `40px`
- **Width:** `40px`
- **Line Height:** `24px`
- **Hover State:** Color `#0000EE`, Text Decoration `underline`
- **Focus State:** Outline `2px solid #4287FF`, Outline Offset `2px`

## 5. Layout Principles

### Spacing System

**Base unit:** `4px`

**Spacing scale:**
- `4px`: Minimal internal padding, icon spacing
- `8px`: Compact component gaps, small margins
- `12px`: Button internal spacing, small card padding
- `16px`: Standard button padding, form field spacing
- `20px`: Primary body padding, content margins
- `24px`: Component gap, moderate section spacing
- `32px`: Card padding, substantial section margins
- `40px`: Large container padding
- `44px`: Extra large spacing between major sections
- `52px`: Significant vertical rhythm between content blocks
- `112px`: Large gap between section groups
- `160px`: Maximum breathing room between major layout sections

**Usage contexts:**
- **Compact:** `4px`–`8px` for icon containers, nested element spacing
- **Standard:** `16px`–`24px` for buttons, form fields, card margins
- **Generous:** `32px`–`52px` for card padding, section separation
- **Expansive:** `112px`–`160px` for hero sections, major content divisions

### Grid & Container

**Max width:** `1220px` (navigation container observed width)

**Column strategy:** Flexible 3-column layout for card grids on larger screens, with cards responsive to `278px` minimum width at medium breakpoints. Hero spans full width with centered text overlay.

**Section patterns:**
- Hero section: Full viewport width with centered overlay text and image background
- Content grid: 3-column card layout at desktop, transitioning to 2-column at tablet, 1-column at mobile
- Navigation: Fixed or sticky header spanning full width with horizontal menu items
- Footer: Full-width dark bar with centered content

### Whitespace Philosophy

Generous, intentional whitespace defines the experience. Large margins between sections (52px–160px) prevent content fatigue and create visual breathing room for dense historical materials. Card-based architecture uses 32px internal padding to ensure content doesn't feel cramped. Vertical rhythm adheres to multiples of 4px, creating a consistent visual grid beneath all layouts.

### Border Radius Scale

- **0px (Sharp edges):** All buttons, cards, inputs, navigation, and borders. Sharp geometry reflects institutional archival design.
- **No rounded corners:** Maintains minimalist, authoritative aesthetic consistent with document-centric information architecture.

## 6. Depth & Elevation

| Level | Treatment | Use |
|---|---|---|
| Flat (None) | `box-shadow: none` | Cards on light backgrounds, primary button states, text-only content |
| Subtle (Small) | `rgba(0, 0, 0, 0.1) 0px 4px 10px 0px, rgba(0, 0, 0, 0.25) 0px 0px 1px 0px` | Secondary buttons, floating action elements, hover card lift |
| Medium (Navigation) | `rgba(0, 0, 0, 0.1) 0px 0px 4px 0px, rgba(0, 0, 0, 0.2) 0px 4px 8px 0px` | Header/navigation fixed positioning, elevated content sections |
| Strong (Modal) | `rgba(0, 0, 0, 0.2) 0px 4px 10px 0px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px` | Modals, overlays, critical notification cards |

**Shadow Philosophy:** Minimal shadow usage reflects the serious, archival nature of the content. Shadows appear primarily on hover states (cards) and elevated UI elements (navigation). The darker shadow values (`0.2`–`0.35` alpha for modal) create distinct layering without excess drama. Sharp edges and restrained shadows together convey institutional authority and trustworthiness appropriate for historical documentation.

## 7. Do's and Don'ts

### Do

- **Use white card backgrounds with `#D8D8D8` borders** for modular content presentation; this pattern dominates the information architecture
- **Apply `#141414` as the primary dark base** for hero sections, navigation headers, and primary button backgrounds
- **Employ generous whitespace:** minimum `32px` padding inside cards, `52px`–`160px` margins between sections
- **Maintain sharp `0px` border radius** across all interactive elements and containers for consistency with institutional design language
- **Use `#0000EE` or `#4287FF` blue for all primary interactive elements:** links, secondary CTAs, and focus states
- **Prioritize typography hierarchy:** Use `104px` H1 for hero impact, `36px` H2 for section dividers, `20px` body for readability
- **Layer content with card-based modular layouts** for dense archival information; use card separation to organize related content groups
- **Include meaningful hover states** on secondary buttons and cards with subtle shadow lift and color shift
- **Test all type sizes at 1.4x–1.5x line height** for optimal readability in long-form historical content

### Don't

- **Don't use rounded corners** (`border-radius > 0px`); maintain sharp edges for institutional authority
- **Don't apply heavy shadows** (`box-shadow` with alpha > 0.35) outside of modal overlays; restraint conveys seriousness
- **Don't reduce font sizes below extracted specifications** for body (`20px`) or buttons (`15px`–`20px`); accessibility demands maintained
- **Don't use colors outside the defined palette** for primary elements; blue and neutral scale are exhaustive by design
- **Don't compress vertical spacing** below `16px` between major content blocks; generous whitespace is essential to the aesthetic
- **Don't place body text on dark backgrounds** without sufficient contrast; prefer white text on dark or dark text on white
- **Don't mix font weights arbitrarily** within body paragraphs; use only 300, 400, or 700 as specified
- **Don't create interactive elements without hover/focus states;** all buttons and links require visual feedback
- **Don't exceed max container width** of `1220px` for standard content layouts; hero can span full viewport
- **Don't underline text links unless hovered;** rely on color differentiation (`#0000EE` or `#4287FF`) for link identification

## 8. Responsive Behavior

### Breakpoints

| Breakpoint Name | Width | Key Changes |
|---|---|---|
| Mobile | 0px–480px | 1-column card grid, full-width cards (`100% - 16px` margin), reduced H1 to `52px`, H2 to `24px`, stacked navigation menu |
| Tablet | 481px–768px | 2-column card grid, H1 to `72px`, H2 to `28px`, horizontal scrolling navigation with overflow |
| Desktop | 769px–1220px | 3-column card grid, full typography scale, fixed navigation header, max container width `1220px` |
| Large Desktop | 1220px+ | Maintain 3-column layout, center content with side margins, max width enforced at `1220px` |

### Touch Targets

- **Minimum touch target size:** `44px × 44px` for all button and link interactive elements
- **Spacing between targets:** Minimum `8px` gap between adjacent interactive elements to prevent mistouch
- **Form field height:** `36px`–`40px` minimum for comfortable mobile interaction
- **Navigation items:** Minimum `48px` height for horizontal nav links; vertical spacing `16px` between stacked items

### Collapsing Strategy

- **Navigation:** Desktop horizontal menu collapses to icon-triggered drawer or hamburger menu below `768px`
- **Cards:** Transition from 3-column to 2-column at `769px`, then to 1-column at `481px`; card width scales to fill container minus margins
- **Typography:** H1 scales from `104px` (desktop) → `72px` (tablet) → `52px` (mobile); H2 scales `36px` → `28px` → `24px`
- **Padding:** Container padding reduces from `40px` (desktop) → `24px` (tablet) → `16px` (mobile)
- **Hero section:** Full-viewport height on desktop; reduced to `60vh` on tablet, `50vh` on mobile; text overlay centers vertically with smaller font
- **Spacing:** Large gaps (`112px`–`160px`) reduce to `52px`–`80px` on tablet, `32px`–`44px` on mobile

## 9. Agent Prompt Guide

### Quick Color Reference

- **Primary CTA Button:** Off-Black (`#141414`), text white
- **Primary Link/Accent:** Hyperlink Blue (`#0000EE`)
- **Secondary Interactive:** Official Blue (`#4287FF`)
- **Primary Text:** Off-Black (`#141414`)
- **Body Background:** Pure White (`#FFFFFF`)
- **Light Surface:** Off-White (`#ECECEC`)
- **Neutral Border:** Light Gray (`#D8D8D8`)
- **Dark Header/Hero:** Off-Black (`#141414`)
- **Header Text:** Pure White (`#FFFFFF`)
- **Disabled/Muted:** Medium Gray (`#676767`)
- **Error State:** Error Red (`#D52A2A`)
- **Warning State:** Warning Yellow (`#FFFF00`)

### Iteration Guide

1. **Set all border-radius to `0px`** across buttons, cards, inputs, and containers; no rounded corners.

2. **Apply generous padding:** Cards receive `32px`, containers `40px`–`44px`, small elements `16px`.

3. **Use sharp color contrasts:** Pair `#141414` backgrounds with `#FFFFFF` text, or `#FFFFFF` backgrounds with `#141414` text; avoid mid-tone combinations.

4. **Maintain typography hierarchy precisely:** H1 at `104px`/`700`, H2 at `36px`/`700`, body at `20px`/`300`; do not deviate without explicit design rationale.

5. **Implement shadow restraint:** Only apply shadows on secondary buttons (`rgba(0, 0, 0, 0.1) 0px 4px 10px 0px...`) and modal overlays; avoid shadows on primary buttons and cards unless hovered.

6. **Space sections generously:** Vertical margins between major content blocks should be `52px` or greater; use the spacing scale multiples.

7. **Use blue intentionally:** `#0000EE` for primary links and hover states, `#4287FF` for secondary interactive elements; reserve blues for interactive-only purposes.

8. **Build card-based layouts:** Organize information in modular white cards with light borders; 3-column grids on desktop, responsive collapsing on smaller screens.

9. **Prioritize accessibility:** Maintain minimum `20px` body font size, line height `1.4x` or greater, color contrast ratios ≥ 4.5:1 for all text.

10. **Establish hover/focus feedback:** Every button and link must shift color, background, or shadow on hover/focus; disabled states use `#676767` with cursor `not-allowed`.
