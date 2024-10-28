# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps

# Remove burger with CSS:
st.markdown("""
<style>
.css-d1b1ld.edgvbh6 {
    visibility: hidden;
}
.css-1v8iw7l.eknhn3m4 {
    visibility: hidden;        
}
.st-emotion-cache-m78myu.e1nzilvr3{
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Add a title to the Streamlit app
st.markdown("""  
<h1>User registration <span style="color:magenta; font-weight: bold">Forms</span></h1>
""", unsafe_allow_html=True)

#implement forms: 
st.markdown("---")
st.write("this is a first form exemple :")
with st.form(key="form1", clear_on_submit = True):
    col1, col2 = st.columns(2)
    col1.text_input("Enter your name", key = "name")
    col1.number_input("Enter your customer number", key = "cust_num", help="Enter you customer ID", format="%6d", value=123456)
    col2.date_input("Enter your date of birth", key = "dob")
    col2.text_input("Enter your email", key = "email" , max_chars = 50)
    st.text_input("Enter your password", key = "password", type = "password")
    st.form_submit_button("Submit")

st.markdown("---")

with st.form(key="form2", clear_on_submit = True):
    tab1, tab2 = st.tabs(["tab1", "tab2"])
    tab1.text_input("Enter your country", key = "country")
    tab1.text_input("Enter your city", key = "city")
    tab2.text_area("Enter your address", key = "address", max_chars = 100)
    tab2.text_input("Enter your postal code", key = "postal_code", max_chars = 5)
    st.form_submit_button("Submit")

print(st.session_state)