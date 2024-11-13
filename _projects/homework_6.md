---
name: Homework 5
tools: [Python, HTML, vega-lite]
image: assets/pngs/scatter.png
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
<vegachart schema-url="{{ site.baseurl }}/assets/json/scatter2.json" style="width: 100%"></vegachart>

```
<vegachart schema-url="{{ site.baseurl }}/assets/json/square.json" style="width: 100%"></vegachart>




# Explanation:
#### First Plot:
The first scatter plot visualizes the relationship between "Square Footage," "Year Acquired," and "Total Floors (binned)" for each building. The x-axis represents the square footage of each building, while the y-axis shows the year it was acquired. Color represents binned categories of building height (measured in floors), allowing us to differentiate tall buildings from shorter ones. A sinebow color scheme was chosen to create a smooth gradient, where lighter to darker shades indicate an increase in the number of floors. Binning Total Floors simplifies the data, making it easier to compare buildings of different heights at a glance. 

This visualization includes transformations to enhance clarity: a dropdown filter for County to focus on specific regions, binning of Total Floors to simplify height comparisons, and a logarithmic scale for Year Acquired to balance historical data. These adjustments make the visualization more user-friendly and insightful.

The interactive component uses the "County" variable, allowing users to filter buildings by county. This makes it possible to explore specific regions and focus on buildings within a selected county, enhancing the plot's clarity and relevance. Compared to Homework #5, this version includes binned data and a refined color scheme to represent Total Floors. The addition of interactivity also allows for a more user-friendly experience, as users can dynamically update the plot to explore buildings from different counties without overwhelming the visualization with too much data at once.

#### Second Plot:
The second plot visualizes the relationship between "Square Footage" and "Building Status," with color representing the "Year Constructed" for buildings within each selected county. The x-axis encodes square footage as a quantitative variable, while the y-axis encodes building status as a nominal variable, providing insights into the distribution of building statuses relative to size. Color is used to indicate the year of construction, binned into five categories to simplify the interpretation of historical data. A sinebow color scheme was chosen for smooth color gradation, where cooler colors represent older buildings and warmer colors represent newer ones. This scheme helps distinguish the age of buildings visually and supports analysis of building age patterns within different size ranges and statuses.

Data transformations include filtering by "County" using an interactive dropdown that lets users select a county and focus on buildings in that area, reducing visual clutter and providing regional insights. The "Year Constructed" was binned to simplify historical comparisons across different age ranges. Compared to Homework 5, this plot replaces floors with "Building Status" and adds interactivity to select counties, adapting to Altair's interactive selection capabilities.

For interactivity, a dropdown filter on "County" lets users dynamically select a specific county, clarifying the plot by focusing on a subset of buildings. This interaction allows users to investigate specific regions, making the data exploration more engaging and relevant to regional analysis.

# Data & Analysis:
Here is the link to my data.
```
<div class="left">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/assets/pngs/scatter.png" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/python_notebooks/Workbook.ipynb" text="The Analysis" %}
</div>
```

<div class="left">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/assets/pngs/scatter.png" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/JingleiZhu-Jane/JingleiZhu-Jane.github.io/blob/main/python_notebooks/Workbook.ipynb" text="The Analysis" %}
</div>

