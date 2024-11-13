---
name: Homework 5
tools: [Python, HTML, vega-lite]
image: hw6/scatter.png
description: This is a project for homework 5
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# Homework 5:

We can use a vegachart HTML tag like so:

```
<vegachart schema-url="{{ site.baseurl }}/assets/json/square.json" style="width: 100%"></vegachart>
```

<vegachart schema-url="/assets/json/square.json" style="width: 100%"></vegachart>
