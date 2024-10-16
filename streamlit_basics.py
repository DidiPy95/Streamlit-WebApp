# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps
import pandas as pd  # Pandas for data manipulation

# Create a sample pandas DataFrame
tabel = pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5, 6, 7],
    "Column 2": [8, 9, 10, 11, 12, 13, 14]
})

# Add custom CSS to hide specific Streamlit elements using class selectors
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

# A print statement (will not be visible in the Streamlit app, only in the console)
print("hello World")

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
