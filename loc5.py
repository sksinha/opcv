import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
#####
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_LOCATION" in result:
        st.write(result.get("GET_LOCATION"))
######
#import json
#y = json.loads(result)
#print(y["lat"])
y=pd.DataFrame(result)
if y.shape[0]:
    st.write(y)
lat=y.head(1)
lon=y.head(2)
st.write(lat,lon)
#map_data = y[[lat, lon]]
st.map(lat,lon)  
