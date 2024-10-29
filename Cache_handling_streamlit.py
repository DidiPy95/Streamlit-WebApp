import streamlit as st
from time import sleep, time

st.title("Cache handling")  # Sets the title of the Streamlit app

# implementing caching for the function:
@st.cache_resource  # Decorator to cache the function's result, so it only runs once per unique input
def printer(t):
    sleep(t)  # Pauses execution for 't' seconds to simulate a delay
    return f".... Done after {t} seconds !"  # Returns a message indicating the delay duration

st.write(printer(10))  # Displays the output of the 'printer' function with an input of 10 seconds


    # The @st.cache_resource decorator caches the result of the function, so if the function is called again with the same argument (t=10 in this case),
    # Streamlit will retrieve the cached result instead of rerunning the function. This helps improve performance when functions are computationally expensive 
    # or involve delays, like this one.

