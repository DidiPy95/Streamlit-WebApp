# Import necessary libraries
import streamlit as st  # Streamlit for creating web apps
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Add a title to the Streamlit app
st.markdown("""  
<h1>Streamlit Sidebar  & Graphs</h1>
""", unsafe_allow_html=True)

#implement sidebar:
st.sidebar.markdown("---")
st.sidebar.write("Graph Selection:")
plt.style.use("dark_background")

def get_graph():
    if st.session_state.graph == "Linechart":
        st.subheader("Linechart Graph")
        fig = plt.figure(figsize = (12,8)) 
        x = np.arange(-2*np.pi, 2*np.pi, 0.1)
        plt.plot(x,np.sin(x))
        plt.title('Line chart')
        st.pyplot(fig)
    elif st.session_state.graph == "Histogram chart":
        st.subheader("Histogram chart")
        fig = plt.figure(figsize = (12,8)) 
        x = np.random.normal(0,5,200)
        plt.hist(x, bins = 20, histtype= "barstacked", rwidth = 0.8, color= "magenta")
        plt.title('Histogram chart')
        st.pyplot(fig)
    elif st.session_state.graph == "H-bar chart":
        st.subheader("H-bar chart")
        fig = plt.figure(figsize = (12,8)) 
        categories = [f'Catégorie {chr(65 + i)}' for i in range(15)]  # 15 catégories de A à O
        values = np.random.randint(10, 100, size=15)  # Génère 15 valeurs aléatoires entre 10 et 100
        plt.barh(categories, values, color= "cyan")
        plt.title('H-bar chart')
        st.pyplot(fig)
    else:
        st.sidebar.write("3D graph")
        st.subheader("3D Graph1")
        def f(x,y):
            return np.cos(x)+np.sin(y)

        x = np.linspace(-10,10,100)
        y = np.linspace(-10,10,100)

        X, Y = np.meshgrid(x,y)
        Z = f(X,Y)

        fig1 = plt.figure(figsize = (12,8)) # start with a figure
        ax1 = plt.axes(projection = '3d')
        ax1.plot_surface(X,Y,Z, cmap = 'plasma')
        plt.title('Surface 3D')
        ax1.set_xlabel('axe x')
        ax1.set_ylabel('axe y')
        ax1.set_zlabel('axe z')
        st.pyplot(fig1)

        ###############################
        st.markdown("---")
        ###############################

        #another method:
        st.subheader("3D Graph2")
        def h(x,y):
            return 10 - (x**2 + y**2)


        fig2 = plt.figure(figsize = (12,8)) # it's important to define a figure
        X = np.arange(-5,5, 0.2)
        Y = np.arange(-5,5, 0.2)
        X,Y = np.meshgrid(X,Y)
        Z = h(X,Y)

        ax2 = plt.axes(projection = '3d')
        ax2.plot_wireframe(X,Y,Z, cmap = 'viridis')
        plt.title('wireframe 3D')
        ax2.set_xlabel('axe x')
        ax2.set_ylabel('axe y')
        ax2.set_zlabel('axe z')
        st.write(fig2)

st.session_state.graph = "Histogram chart"
opt = st.sidebar.radio("Choose the graph type", ("Linechart", "Histogram chart", "H-bar chart", "3D graph"), on_change=get_graph, key="graph")
st.write("you 've selected : ", opt)
st.write("Session State : ", st.session_state)
# print(plt.style.available)

