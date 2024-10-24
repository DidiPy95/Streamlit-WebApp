# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps
import pandas as pd  # Pandas for data manipulation


# Create a sample pandas DataFrame
tabel = pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5, 6, 7],
    "Column 2": [8, 9, 10, 11, 12, 13, 14]
})

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

# Add a subheader to the app
st.subheader("Hi! I am your Sunheader")

# Add a header to the app
st.header("I am Header")

# Display a simple text message in the app
st.text("Hi I am text function and programmers use me")

# Display a Markdown link to Google within the app
st.markdown("[Google](https://www.google.com)")

# Add a horizontal rule (divider) using Markdown
st.markdown("---")

# Display a LaTeX expression (matrix) within the app
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# Create a JSON object and display it in a pretty JSON format
json = {"a": "1,2,3", "b": "4,5,6"}
st.json(json)

# Define a simple function
def funct():
    return 0

# Display Python code snippet within the app
code = """
print("hello World")
def funct():
    return 0
"""
st.code(code, language="python")

# Write Markdown text (renders as H2 header in Streamlit)
st.write("## H2")

# Display a metric widget with label, value, and delta
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1ms⁻¹")

# Display the pandas DataFrame as a static table
st.table(tabel)

# Display the pandas DataFrame as an interactive dataframe (possibility to sort columns and rows)
st.dataframe(tabel)

#display audio and video
st.audio(r"C:\Users\Proprietaire\OneDrive\Documents\Streamlit\file_example_MP3_2MG.mp3")
st.video(r"C:\Users\Proprietaire\OneDrive\Documents\Streamlit\file_example_MP4_640_3MG.mp4")

#implementcheckbox : we can assign the checkbox to a variable :
# state = st.checkbox("checkbox", value = False)
# if state:
#     st.info("Checkbox is checked")
# else:
#     st.warning("Checkbox is not checked")
st.markdown("---")

#implement checkbox with callback : st.checkbox permet de créer une seule case à cocher, et non pas une liste d'options.
st.write("this is a checkbox :")
def on_change():
    print(" * Callback_triggered : st.session_state.checker : ",st.session_state.checker)

state = st.checkbox("checkbox" , value = False, on_change=on_change, key="checker")
if state:
    st.info("Checkbox is checked")
else:
    st.warning("Checkbox is not checked")

#implement radio button :
st.markdown("---")
st.write("this is a radio button :")
radio_btn = st.radio("choose the wanted option : ", ["option 1", "option 2", "option 3"], key="radio")

#implement button :
st.markdown("---")
st.write("this is a button :")

def btn_clicked():
    print(" * Callback_triggered : st.session_state.button : ",st.session_state.button)

btn = st.button("click me", key="button", on_click=btn_clicked)

#implement selectbox :
st.markdown("---")
st.write("this is a selectbox :")
selectbox = st.selectbox("choose the wanted option : ", ["param1", "param2", "param3"], key="selectbox")

#implement multiselectbox :
st.markdown("---")
st.write("this is a multiselect :")
multiselect = st.multiselect("choose your favorite option : ", ["Audi", "BMW", "Mercedes"], key="multiselect")








print(st.session_state)