import streamlit as st
import altair as alt
from vega_datasets import data
 
st.title('HW 5: building inventory Analysis')

st.text("The URL for this app is: https://huggingface.co/spaces/Janezjl/Data_Visualization")

building_url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
brush = alt.selection_interval(encodings=['x','y'])
chart1 = alt.Chart.from_dict({
  # Data
  "data": {"url":building_url},
  #// Marks
  "mark":"rect",
  "height":400,
  # Encoding (note:error for encoding vs encodings)
  "encoding":{
    "x":{"bin":{"maxbins":10}, "field":"Square Footage", "type":"quantitative"},
    "y":{"field":"Agency Name","type":"ordinal"},
    "color":{"aggregate":"count", "type":"quantitative"} 
    # will show the number of records with a specific student/teacher ratio in a particular state
  }
  
}).add_params(
    brush
)
chart2 = alt.Chart.from_dict({
    # Data
    "data":{"url":building_url},
    # mark
    "mark":"bar",
    # encoding
    "encoding":{
        "x":{"field":"Total Floors", "bin":True, "type":"quantitative", "axis":{"title":"Floors built"}}, 
        "y":{"aggregate":"count", "type":"quantitative", "axis":{"title":"Floors built Distribution"}}
    }
}
).transform_filter(
    brush
)

chart = chart1 | chart2
chart


st.markdown("For the first chart, the square footage of properties under the management of various agencies is displayed in the first chart, Square Footage Distribution by Agency. A separate agency is represented by each row, and the binned square footage is displayed on the x-axis. The number of records (or individual properties) for that agency within each square footage range is indicated by the color's intensity in each row. Higher counts are shown by darker hues, which makes it simple to identify firms that manage a greater number of properties within particular size categories. Agencies with substantial property holdings in particular size bins can be found using this heatmap-style method. The varying color scheme was used to successfully direct the viewer's attention to areas of greater density while keeping a clean, uncluttered appearance.")

st.markdown("The second chart, Floors Built Distribution, is a bar chart showing the distribution of buildings by the number of floors. The x-axis represents the number of floors in the buildings, while the y-axis shows the count of records (or properties). This chart reveals that the majority of buildings managed by these agencies are low-rise, with most buildings having fewer than five floors. The straightforward bar chart format, with a single color for the bars, keeps the focus on the distribution of floors without adding unnecessary visual complexity. If given more time, I would consider adding interactivity to both charts, such as tooltips or data labels, for better data exploration. Additionally, I might refine the color scheme in the square footage chart to ensure clearer differentiation between high and low counts.")