# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps
import pandas as pd  # Pandas for data manipulation

# Remove burger with CSS:
st.markdown("""
<style>
.css-d1b1ld.edgvbh6 {
    visibility: hidden;
}
.css-1v8iw7l.eknhn3m4 {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Add a title to the Streamlit app
st.title("Hi! I am Streamlit Web App")

#implement file upload :
st.markdown("---")
st.write("this is a file upload :")
uploaded_files = st.file_uploader("Choose a file:", type=["jpg", "png"], key="uploader", help="only .pnj and .jpg images are allowed", accept_multiple_files=True)
if uploaded_files is not None and len(uploaded_files) > 0:
    for uploaded_file in uploaded_files:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
else:
    st.warning("No file uploaded")

#implement slider:
st.markdown("---")
st.write("this is a slider :")

def slide():
    st.write(f"* Selected value is : {st.session_state.slider}")
    #print(slider, type(slider))
slider = st.slider("Choose a number", 0, 100, 50, step=5, key="slider", on_change=slide) 
st.write("Slider value:", slider)

#implementing text widget :
st.markdown("---")
st.text("those are  text widgets :")

str1 = st.text_input("Enter your name", key="text", max_chars=50)
str2 = st.text_area("express your thoughts", key="text_area", max_chars=500, help="Type your thoughts here")

st.write("hello", st.session_state.text, ", you wrote : ", str2)

#impelemnt a select_slider:
st.markdown("---")
st.write("this is a select_slider :")
select_slider = st.select_slider("choose the wanted option : ", ["param1", "param2", "param3"], key="select_slider", value="param2" )
st.write("you 've selected : ", st.session_state.select_slider)

#implement a color picker :
st.markdown("---")
st.write("this is a color picker :")
color_picker = st.color_picker("choose your favorite color : ", "#00f2ff", key="color_picker")
st.write("you 've selected : ", st.session_state.color_picker)
print ("type of color_picker : ", type(st.session_state.color_picker))

#implement a date input:
st.markdown("---")  
st.write("this is a date input :")
date = st.date_input("choose a date : ", key="date_input",value = "default_value_today")
st.write("you 've selected : ", st.session_state.date_input)
print ("type of date variable: ", type(date))

#implement a time input:
st.markdown("---")
st.write("this is a time input :")
time = st.time_input("choose a time : ", key="time_input")
st.write("you 've selected : ", st.session_state.time_input)
print ("type of time variable: ", type(time))

#implement a progress bar:
st.markdown("---")
st.write("this is a progress bar :")
bar = st.progress(0)
for i in range(10):
    bar.progress((i+1) * 10)






# print(st.session_state.uploader) #make the webapp lagging: