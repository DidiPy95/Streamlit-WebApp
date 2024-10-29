import streamlit as st
import streamlit.components.v1 as com

# Define the CSS file path
css_filepath = r"styles.css" 
with open(css_filepath, "r") as f:
    css_link = f"<style>{f.read()}</style>"

# Define the HTML structure with logical and descriptive class names
com.html(css_link + """
<div class="custom-component">
    <h1 class="title">Hello, Streamlit!</h1>
    <h2 class="subtitle">This is a custom HTML element</h2>
    <img class="image" src="https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt7c0bf7e21d4410b4/6319700b8cc2fa14e223aa27/8895.png" alt="Streamlit logo">
    <p class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
    <iframe class="lottie" src ="https://lottie.host/embed/40a90f08-e448-45e2-a49e-756547b447d2/M8NLJeXK17.json"></iframe>
</div>
""", scrolling=True, width=700, height=800)

#using iframe component make the integration of lottie animation more fluid and responsive:
com.iframe("https://lottie.host/embed/b432f924-985f-413d-9ad4-2232a0bfc146/YezBp5EojO.json") 