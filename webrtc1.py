import streamlit as st
img_file_buffer = st.camera_input("Take a picture")

if picture:
     st.image(picture)
