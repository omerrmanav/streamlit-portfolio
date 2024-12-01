import streamlit as st

def main_page():
    st.title("ÖMER MANAV")
    # st.image("assets\profile.jpeg", use_column_width=True)
    st.title("About Me")
    st.write("""
        I am a 3rd year Software Engineering student at Üsküdar University.
        """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/profile.jpeg", use_column_width=True)  # Profil resmi
        

    with col2: 
        st.write("""
        I take care to develop myself in different areas during the software development process.
        I worked on a deep learning project using
        Python language. In this context, in a project
        where we used SVM and KNN classification
        algorithms, we aimed to produce logical
        predictions with the data set we created. I
        have a special interest and curiosity in deep
        learning and data science. \n
        In addition, I worked on a Cinema
        Management System project that I developed
        using Java and MySQL with a layered
        architecture in accordance with OOP rules.
        I aim to produce innovative solutions by
        combining both theoretical knowledge and
        practical experience.
        I am open to learning to continuously improve
        myself and adapt to new technologies.

        """)
    st.subheader("Contact Information")
    st.write("📧 Email: omanav922@gmail.com")
    st.write("📱 Phone: +90 505 014 13 63")
    st.write("🌐 LinkedIn: [linkedin.com/in/omerrmanav](https://linkedin.com/in/omerrmanav)")
    st.write("💻 GitHub: [github.com/omerrmanav](https://github.com/omerrmanav)")

    st.title("Education")
    st.write("""
    - 🎓 **Bachelor of Software Engineering**  
      Uskudar University, 2022 - Present
    - 📜 **Preparatory School**  
      Uskudar University, 2021 - 2022
    """)