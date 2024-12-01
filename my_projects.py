import streamlit as st

import streamlit as st

def my_projects():
    st.title("My Projects")

    # Project 1: SVM, KNN, and Deep Learning
    st.subheader("1. SVM, KNN, and Deep Learning Project")
    st.write("""
    This project demonstrates the implementation of various machine learning algorithms, 
    including Support Vector Machine (SVM), K-Nearest Neighbors (KNN), and Deep Learning models. 
    It focuses on dataset analysis and performance comparison of these methods.
    """)
    st.markdown("[View on GitHub](https://github.com/omerrmanav/svm-knn-deep-learning)")

    # Project 2: Cinema Management Project
    st.subheader("2. Cinema Management Project")
    st.write("""
    A desktop application designed to manage cinema operations such as ticket bookings, 
    movie scheduling, and user management. It features an interactive interface, database integration, 
    and real-time updates to streamline cinema administration tasks.
    """)
    st.markdown("[View on GitHub](https://github.com/omerrmanav/Cinema-Management-Project)")
