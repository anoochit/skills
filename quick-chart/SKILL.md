---
name: quick-chart
description: Generate charts and QR codes using QuickChart.io. Use when the user asks for a chart, graph, visualization, or QR code. Returns a URL that renders the image.
---

# Quick Chart

This skill generates URLs for charts and QR codes using the QuickChart.io API.

## QR Codes

To generate a QR code:

1.  Identify the text or URL to encode.
2.  Run the script:
    ```bash
    python skills/quick-chart/scripts/qr_gen.py "<text>" [size]
    ```
    - Default size is 300.

3.  Output the resulting URL in an image tag: `![QR Code](<url>)`

## Charts

To generate a chart:

1.  Construct a valid Chart.js (v2/v3) configuration JSON object.
    - Common types: `bar`, `line`, `pie`, `doughnut`, `radar`.
    - Structure: `{ "type": "bar", "data": { "labels": [...], "datasets": [...] }, "options": {...} }`

2.  Run the script with the JSON string:
    ```bash
    python skills/quick-chart/scripts/chart_gen.py '<json_config>'
    ```
    - **Important**: Ensure the JSON string is properly escaped for the shell (use single quotes for the argument, and escape inner single quotes if any).

3.  Output the resulting URL in an image tag: `![Chart](<url>)`

## Examples

### Bar Chart
```json
{
  "type": "bar",
  "data": {
    "labels": ["Q1", "Q2", "Q3", "Q4"],
    "datasets": [{
      "label": "Users",
      "data": [50, 60, 70, 180]
    }]
  }
}
```

### Pie Chart
```json
{
  "type": "pie",
  "data": {
    "labels": ["Red", "Blue", "Yellow"],
    "datasets": [{
      "data": [300, 50, 100],
      "backgroundColor": ["rgb(255, 99, 132)", "rgb(54, 162, 235)", "rgb(255, 205, 86)"]
    }]
  }
}
```
