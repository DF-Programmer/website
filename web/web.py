import streamlit as st

st.set_page_config(page_title='My Website', page_icon=':globe_with_meridians:', layout='centered')

#~~~ welcoming section
with st.container():
    st.write("Aspiring Freelance Programmer")
    st.title("Hello, I'm Dom!")
    st.subheader("This is my website where you can find all my social media platforms and learn about me.")

#~~~ About me section
with st.container():
    st.write("---")
    st.title("About Me")
    st.subheader("Programming with Python:") #~~~ My coding section
    st.write("""
        I have been programming for over 3 years using python.
        Over this time I have learn alot and tackled many challenges along the way.
        Some of my projects I have built include;
        interactable calculators, login servers that stores usernames/passwords, a notepad app, and more.
        I am always looking to tackle new projects and learn more.
        """)
    st.write("##")
    st.subheader("My Goals:") #~~~ My goals section
    st.write("""
        My overall goal is to put my skills abilities to good use.
        I would love to teach others my new discoveries and what I have learnt over the years.
        Most importantly, I want to enjoy doing what I love and continue to improve my programming skills.
        """)
    st.write("##")
    st.subheader("Other:") #~~~ Other section
    st.write(
        """
        I also have some experience programming with otehr languages such as Lua.
        I have a moderate understanding of how to use Lua effectively but I am still learning to improve my knowledge.
        I also know the basics of SQL and Javascript although I still have alot to learn with these languages.
        I would love to improve my Lua skills as well as learn new languages such as JavaScript, C# and HTML.
        """
        )
    
#~~~ Link section
with st.container():
    st.write("---")
    st.header("Links to my pages::link:")
    st.write("[YouTube](https://www.youtube.com/channel/UCEz-tcPheuI_JLaLC6HjXzw)")
    st.write("[Fiverr](https://www.fiverr.com/df_programmes)")
