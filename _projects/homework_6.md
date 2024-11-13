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

# Visualization:

We can use a vegachart HTML tag like so:

```
<vegachart schema-url="{{ site.baseurl }}/assets/json/scatter1.json" style="width: 100%"></vegachart>
```
<vegachart schema-url="{{ site.baseurl }}/assets/json/scatter1.json" style="width: 100%"></vegachart>

# Data:
Here is the link to my data.
```
<div class="left">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/hw6/scatter.png" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/hw6/Workbook.ipynb" text="The Analysis" %}
</div>
```

<div class="left">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/hw6/scatter.png" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/hw6/Workbook.ipynb" text="The Analysis" %}
</div>