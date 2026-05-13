# Diagram Style Library

Conventions extracted from three reference diagrams the user has shipped
in real papers:

| File | What it diagrams |
|---|---|
| `SSL-overview.xml` | Mirrored speech-vs-music SSL pipeline overview (2-stage, 2-column) |
| `mertfinal.xml` | MERT pre-training pipeline (2-stage, multi-target acoustic-unit discovery) |
| `cpc.xml` | CPC contrastive predictive coding figure (CNN encoder + AR + future-frame predictions) |

All three are `.drawio` XML and edited in **draw.io desktop**
(`/Applications/draw.io.app`). This file is the source of truth for the
`diagram-specialist` agent — when generating a new diagram, the agent must
mirror these conventions unless the project's `.claude/CLAUDE.md` overrides.

---

## 1. Page setup

```xml
<mxGraphModel dx="2054" dy="1151" grid="1" gridSize="10"
              guides="1" tooltips="1" connect="1" arrows="1"
              fold="1" page="1" pageScale="1"
              pageWidth="850" pageHeight="1100"
              math="1" shadow="0">
```

- **`math="1"` is mandatory** — enables `$$...$$` LaTeX rendering inside
  labels. Every reference diagram uses it.
- `pageWidth=850 pageHeight=1100` (letter-portrait). For wide diagrams
  the user opens the file in draw.io and adjusts; do not pre-emptively
  rotate to landscape.
- `gridSize=10` always. Snap everything to multiples of 10.

## 2. Colour palette (verified from 50+ cells across the three files)

| Purpose | Fill | Stroke | Notes |
|---|---|---|---|
| **Encoder / model / pipeline block** (primary) | `#dae8fc` | `#6c8ebf` | Blue — most common box style for "Speech upstream model", "Music upstream model" container blocks |
| **Acoustic / K-means / primary target** | `#D5E8D4` | `#82B366` | Green — used for K-means clustering blocks and `a_1...a_T` token rows |
| **Alternative path / EnCodec / secondary target** | `#E1D5E7` | `#9673A6` | Purple — used for EnCodec, alternative units, merged output |
| **Source / Input A** | `#F8CECC` | `#B85450` | Red — used when contrasting two pipelines |
| **Continuous-representation tile** | `#fff2cc` | `#d6b656` | Yellow — small tilted chips representing a continuous-feature sequence (24 occurrences, the most-used colour) |
| **Loss / objective block** | `#ffe6cc` | `#d79b00` | Orange — "Pre-training loss", "Contrastive loss" framings |
| **Raw data corpus / dataset (small)** | `#f5f5f5` | `#666666` | Grey — paired with `shape=datastore` for "Unlabeled speech (e.g., LibriSpeech)" |
| **Frozen module (downstream stage)** | `#dae8fc` | `#6c8ebf` + `dashed=1` | Same blue, but dashed border to mark "frozen" |
| **Inner-content panel** | `#ffffff` | `#6c8ebf` | White panel inside a blue container — used for "Low-level representations (e.g., CNN encoder)" sub-blocks |

Pair the lighter fill with the darker stroke (e.g. `#dae8fc` with
`#6c8ebf`). The user often mixes uppercase and lowercase hex codes
(`#D5E8D4` vs `#d5e8d4`) — drawio accepts both; the agent should pick
one and be consistent within a single diagram.

### Text fontColor accents

| Purpose | fontColor |
|---|---|
| Section sub-header (primary target) | `#2D7D2D` (green) |
| Section sub-header (alternative target) | `#6D28D9` (purple) |
| Tertiary / muted / parenthetical note | `#666666` (grey) |
| Default body label | (none — inherit black) |

## 3. Font sizes (modal values from the samples)

| Element | Size | Style |
|---|---|---|
| Top section banner (SPEECH / MUSIC) | 17 | bold (`fontStyle=1`) |
| Stage label ("Stage 1: Pre-training") | 14 | italic (`fontStyle=2`) |
| Box title (inside encoder block) | 12 | bold or plain |
| Box content / sub-label | 12 | plain |
| Token chip (`a_1`, `e_t`) | 9 | plain |
| Arrow label | 10 | plain |
| Parenthetical italic note ("(e.g., CNN encoder)") | 12 | italic via `<i>` tag inside the value |

## 4. Recurrent visual patterns

### 4.1 Mirror-pair (left/right side-by-side comparison)

The SSL-overview lays out two parallel pipelines: speech on the left
(x ≈ 130–400) and music on the right (x ≈ 630–890), with identical
internal structure. Use this pattern when comparing **two contrasting
domains** (e.g. HuBERT vs MERT, clean vs noisy, baseline vs proposed).

- Place the SPEECH / MUSIC banner at the very top, centred over each
  column (`fontSize=17;fontStyle=1`).
- Stage labels go just below (`fontStyle=2;fontSize=14`).
- The two columns are exact mirrors in their internal layout; only the
  banner text and a few module names differ.

### 4.2 Stage divider (horizontal dashed line)

A full-width dashed grey line separates Stage 1 (pre-training / training)
from Stage 2 (downstream / inference):

```xml
<mxCell id="..." edge="1" parent="1"
        style="endArrow=none;startArrow=none;html=1;rounded=0;
               dashed=1;strokeColor=#999999;strokeWidth=1.5;">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="12" y="414" as="sourcePoint"/>
    <mxPoint x="1022" y="414" as="targetPoint"/>
  </mxGeometry>
</mxCell>
```

The Stage 2 label appears immediately below the divider on each column.

### 4.3 Datastore icon + caption for corpora

For "Unlabeled speech (e.g., LibriSpeech)" type elements, use three small
`shape=datastore` cylinders side-by-side (each 28×26, x-spaced 34 px
apart) with a free-floating italic caption below:

```xml
<mxCell id="6" parent="1"
        style="shape=datastore;whiteSpace=wrap;html=1;
               fillColor=#f5f5f5;fontColor=#333333;strokeColor=#666666;"
        value="" vertex="1">
  <mxGeometry height="26" width="28" x="211" y="52" as="geometry"/>
</mxCell>
<!-- ... two more cylinders at x=245 and x=279 ... -->
<mxCell id="9" parent="1"
        style="text;html=1;align=center;verticalAlign=middle;
               fontSize=13;strokeColor=none;fillColor=none;"
        value="Unlabeled speech (e.g., LibriSpeech)" vertex="1">
  <mxGeometry height="30" width="240" x="142" y="73" as="geometry"/>
</mxCell>
```

### 4.4 Continuous-representation tile sequence

A row of small (~13×30) **rotated** yellow chips represents a continuous
feature sequence. The rotation is 1° — just enough to suggest motion /
sampling — wrapped in an invisible `group` parent for easy GUI nudging:

```xml
<mxCell id="30" connectable="0" parent="1" style="group" value="" vertex="1">
  <mxGeometry height="32" width="160" x="191" y="346" as="geometry"/>
</mxCell>
<mxCell id="31" parent="30"
        style="rounded=1;whiteSpace=wrap;html=1;rotation=1;container=0;
               fillColor=#fff2cc;strokeColor=#d6b656;"
        value="" vertex="1">
  <mxGeometry height="30" width="13" y="2" as="geometry"/>
</mxCell>
<!-- repeat 6-7 more chips at x=20, 40, 60, 80, 100, 120 -->
<mxCell id="38" parent="1"
        style="text;html=1;align=center;fontSize=12;fontStyle=2;
               strokeColor=none;fillColor=none;"
        value="continuous representations" vertex="1">
  <mxGeometry height="30" width="170" x="177" y="371" as="geometry"/>
</mxCell>
```

### 4.5 Discrete-token chip row

For discrete tokens (`a_1, a_2, ..., a_T` or `e_1, e_2, ..., e_T`), use
sharp-cornered (not rounded) coloured chips, each 28×22, with LaTeX math
labels and a literal `...` text cell in the middle:

```xml
<mxCell id="10" parent="1"
        style="rounded=0;whiteSpace=wrap;html=1;
               fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9;"
        value="$$a_1$$" vertex="1">
  <mxGeometry height="22" width="28" x="48" y="206" as="geometry"/>
</mxCell>
<!-- $$a_2$$, $$a_3$$, ... separated by a `...` text cell, then $$a_T$$ -->
```

The colour of the chip row matches the section colour (green for
acoustic K-means, purple for EnCodec / alternative units).

### 4.6 Italic inner subtitle inside a coloured box

The blue container "Speech upstream model" has top-left bold title and
inner sub-blocks ("Low-level representations / (e.g., CNN encoder)") that
use `<i>` HTML and a grey colour for the parenthetical:

```xml
<mxCell id="18" parent="1"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;
               strokeColor=#6c8ebf;fontSize=12;align=center;
               verticalAlign=middle;"
        value="Low-level representations&lt;br&gt;&lt;i style=&quot;color: rgb(102, 102, 102);&quot;&gt;(e.g., CNN encoder)&lt;/i&gt;"
        vertex="1">
  <mxGeometry height="36" width="200" x="162" y="144" as="geometry"/>
</mxCell>
```

The `&lt;br&gt;` separates title from subtitle; `<i style="color: rgb(102, 102, 102);">` makes the parenthetical italic and grey.

### 4.7 Math labels via `math="1"`

Inline equations use `$$...$$` directly inside `value=`:

| Pattern | Example value |
|---|---|
| Vector | `$$\boldsymbol{z}_t$$` |
| Indexed | `$$\boldsymbol{z}_{t+1}$$` |
| Function | `$$f_{\text{AR}}$$` |
| Subscripted with text | `$$\text{CNN encoder } f_{\text{enc}}$$` |
| Italic phrase | `$$\textit{receptive field of } \boldsymbol{z}_t$$` |

Use `\boldsymbol{}` for vectors (matches the paper body text style). Use
`\text{}` to mix natural-language descriptors with math inside the same
label.

### 4.8 Section sub-headers in coloured italic

Above each coloured section, use a sub-header with a coloured italic
text label (no fill, no stroke):

```xml
<mxCell id="5" parent="1"
        style="text;html=1;align=center;verticalAlign=middle;
               whiteSpace=wrap;rounded=0;fontStyle=3;fontSize=10;
               fontColor=#2D7D2D;"
        value="Target 1: Acoustic K-means" vertex="1">
```

- Green `#2D7D2D` for the primary target.
- Purple `#6D28D9` for the alternative target.
- `fontStyle=3` = bold + italic.

### 4.9 Concrete downstream-task examples (SUPERB-style)

In SSL-overview, the downstream stage shows concrete tasks with bold
result labels: "action: **buy**", "speaker 7", "genre: **rock**",
"instrument: **guitar**", "pitch: **C4**" — paired with task-name boxes
"ASR / IC / SID / GenreID / InstCls / PitchID". These ground the
abstract pipeline in real outputs the reader can verify against the
text. **Always show concrete labels** when the paper enumerates
downstream tasks individually (per the ES rule in the supervisor-
feedback skill).

### 4.10 Stick-figure speaker icon (base64 SVG)

For "speakers" / "listeners" / "user" iconography, use the small blue
stick-figure SVG embedded as base64 in the `image=` style attribute.
The exact base64 string is preserved at the bottom of this file in
section 7. Don't redraw it from scratch — copy that line.

## 5. Element ID naming convention

The samples use plain integers (`id="2"`, `id="3"`, ...). The
diagram-specialist agent uses **descriptive string IDs**
(`box_hubert`, `arrow_hubert_corr`, `panel_a_group`) for human
editability. This is a deliberate deviation — descriptive IDs make the
XML easier to read and revise by hand. Drawio accepts both.

When importing user-edited files (host=Electron, hashed IDs), the agent
should **preserve the user's IDs**, not rewrite them to descriptive
form.

## 6. Geometry conventions

- Standard box: 200×36 (e.g. "Low-level representations") or 130×40
  (e.g. "K-means Clustering").
- Standard datastore: 28×26.
- Token chip: 28×22 (discrete) or 13×30 (continuous, rotated).
- Column gutter (mirror pair): ~250 px between speech-column right edge
  and music-column left edge.
- Section vertical pitch: ~60 px between adjacent boxes in a vertical
  pipeline.

## 7. Reusable assets

### 7.1 Stick-figure speaker icon

The blue speaker / listener icon used in SSL-overview Stage 2 and in
cpc.xml (as receivers of predictions) is encoded as:

```
style="editableCssRules=.*;html=1;shape=image;
       verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;
       verticalAlign=top;aspect=fixed;imageAspect=0;
       image=data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnY9Imh0dHBzOi8vdmVjdGEuaW8vbmFubyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjIwIiB2aWV3Qm94PSIwIDAgMTggMjAiPiYjeGE7CTxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+JiN4YTsJLnN0MHtmaWxsOiM0Mjg1ZjQ7fSYjeGE7CS5zdDF7ZmlsbDojNjY5ZGY2O30mI3hhOwk8L3N0eWxlPiYjeGE7CTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik04IDBoMnYyMEg4ek00IDZoMnY4SDR6bTggMGgydjhoLTJ6TTAgM2gydjE0SDB6bTE2IDBoMnYxNGgtMnoiLz4mI3hhOwk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNOCAwaDJ2MTBIOHpNNCA2aDJ2NEg0em04IDBoMnY0aC0yek0wIDNoMnY3SDB6bTE2IDBoMnY3aC0yeiIvPiYjeGE7PC9zdmc+;"
```

When a diagram needs this icon, paste this style block verbatim. Do
not regenerate it.

---

## 8. Pattern selection cheatsheet

| The diagram needs to... | Use this pattern |
|---|---|
| Compare two pipelines side-by-side | Mirror-pair (§4.1) + stage divider (§4.2) |
| Show training vs inference / Stage 1 vs Stage 2 | Stage divider (§4.2) |
| Represent unlabeled training data | Datastore triplet (§4.3) |
| Visualise a continuous feature sequence | Tilted-yellow tile row (§4.4) |
| Visualise a discrete token sequence | Coloured-chip row with math labels (§4.5) |
| Show a module with a parenthetical "(e.g., X)" inside | Inner subtitle with `<i>` grey HTML (§4.6) |
| Label a vector / function in the diagram | Math via `$$...$$` (§4.7) |
| Group a list of related downstream tasks | Concrete task-name boxes with bold result labels (§4.9) |
| Show a user / speaker / listener | Stick-figure SVG (§7.1) |

## 9. What NOT to do (inferred from the samples)

- **No chart junk.** No drop shadows. `shadow="0"` on the model. No
  gradients on fills.
- **No solid black strokes for every shape.** Use the semantic stroke
  that matches the fill (e.g. `#6c8ebf` with `#dae8fc`, not `#000000`).
- **No arrow forests.** Each arrow has a clear source and target;
  parallel arrows are bundled vertically with consistent spacing.
- **No unaccompanied symbols.** A bold equation `$$\pi^*$$` always has
  a textual gloss nearby ("permutation that maximises cross-
  correlation").
- **No mixed grid alignment.** Once `gridSize=10` is set, every x and
  y is a multiple of 10. The 0.02 / 0.07 fractional offsets you see in
  cpc.xml are leftovers from arrow auto-routing and should be cleaned
  up when revising.
