---
name: create-slide
description: Create professional, interactive web presentations using reveal.js and Chart.js. Includes a modern dark theme and uses Google Sans/Inter fonts. Use when you need to generate high-quality slide decks with embedded charts from JSON data or structured content.
---

# Create Slide Skill

## Overview

This skill allows you to generate professional web-based presentations using **reveal.js** for the slides and **Chart.js** for interactive visualizations. It is optimized for a sleek **dark theme** and uses a premium typography stack (Google Sans, Inter) for maximum legibility and style.

## Resources

- **`scripts/generate_presentation.cjs`**: The primary engine for generating presentations from JSON data.
- **`references/template.html`**: The HTML/CSS/JS base for reveal.js and Chart.js integration.
- **`assets/sample_presentation.json`**: An example data structure for your presentation.

## Workflow

### 1. Structure Your Data
Define your presentation in a JSON file following this structure:
```json
{
  "title": "Presentation Title",
  "slides": [
    { "type": "title", "title": "Welcome", "subtitle": "A short description" },
    { "type": "bullets", "title": "Our Goals", "bullets": ["Growth", "Innovation"] },
    { "type": "chart", "title": "Performance", "chartConfig": { /* Chart.js config */ } },
    { "type": "content", "title": "Summary", "content": "The core message." }
  ]
}
```

### 2. Generate the Presentation
Run the generator script to combine your data with the template:
```bash
node <skill-path>/scripts/generate_presentation.cjs <data-path>.json <output-path>.html
```

### 3. Customize Look & Feel
- **Dark Theme**: Enabled by default using reveal.js 'black' theme.
- **Typography**: Uses 'Google Sans' and 'Inter' as fallback.
- **Charts**: Fully integrated with Chart.js. For a dark theme, use light colors for axes and labels (e.g., `#ffffff` or `rgba(255,255,255,0.7)`).

## Examples

### Generating a Sales Deck
"Create a sales presentation for Q2 2026 using the data from sales_data.json and save it as q2_deck.html."

1. Parse the provided data.
2. Formulate a JSON structure following the pattern.
3. Call the `generate_presentation.cjs` script.
4. Verify the output.

### On-the-fly Presentation
"Make a single slide with a pie chart showing my current budget distribution."

1. Create a minimal JSON with one `chart` type slide.
2. Run the generator script.
3. Output the `.html` file path for the user.
