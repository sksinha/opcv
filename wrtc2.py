import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events


html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Attendance Web App </h1>
</div><br>

<script>
var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
</script>"""
components.html(html_temp)
st.markdown(html_temp,unsafe_allow_html=True)
st.title('National Informatics Centre')
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

st.write(position)


img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
    
#########################
       
###########################
