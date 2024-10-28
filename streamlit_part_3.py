# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps
import pandas as pd  # Pandas for data manipulation
from time import time, sleep
import datetime
from warnings import filterwarnings

filterwarnings("ignore")

# Add a title to the Streamlit app
st.title("Date and time input, Progress bar")

#implement a date input:
st.markdown("---")  
st.write("this is a date input :")
date = st.date_input("choose a date : ", key="date_input")
st.write("you 've selected : ", st.session_state.date_input)
#print ("type of date variable: ", type(date))

#########################################################################################################################################################################

# we need to concert the time variable to seconds so e can use it in the sleep function:
def convert_to_seconds(to: datetime.time) -> int:
    h,m,s = to.hour, to.minute, to.second
    return h * 3600 + m * 60 + s

def run_progress_bar(ts:datetime.time):
    st.write("this is a progress bar representing the time you've selected :")
    bar = st.progress(0)
    if str(ts) == "00:00:00":
        st.warning("Please select a valid period of time")
    else:
        #implement a progress bar:
        sec = convert_to_seconds(ts)
        div = sec / 100
        progress_status = st.empty() #object that can store anything but it deletes it when it goes out of scope
        print("we have",div,"second divisions for",sec,"seconds")
        for i in range(100):
            bar.progress(i+1)
            progress_status.success(f"Progress: {i+1}%")
            sleep(div)

#implement a time input:
st.markdown("---")
st.write("this is a time input :")
t = st.time_input("Set a timer for : ", key="time_input", value = datetime.time(minute=0, hour=0, second=0), step=datetime.timedelta(seconds=60))
st.write("you 've selected : ", t )
print ("type of 't' variable: ", type(t))
run_progress_bar(t)
