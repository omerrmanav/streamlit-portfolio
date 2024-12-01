import streamlit as st
from main_page import main_page
from my_projects import my_projects

PAGES = {
    "About Me": main_page,
    "Projects": my_projects
}

def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[choice]
    page()

if __name__ == "__main__":
    main()