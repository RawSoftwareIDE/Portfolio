import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="RawSoftware Portfolio", layout="wide")

# Custom CSS
st.markdown("""
<style>
    [data-testid="stDecoration"] {background: #F50B0B;}
    .main {
        padding: 0rem 5rem;
    }
    .stApp {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #F50B0B;
    }
    .stExpander {
        background-color: #1E2329;
        border: 1px solid #2E3339;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .stExpander:hover {
        box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
        transition: box-shadow 0.3s ease-in-out;
    }
    .stExpander > div:first-child {
        background-color: #2E3339;
        color: #4CAF50;
        font-weight: bold;
        transition: background-color 0.3s ease-in-out;
    }
    .stExpander > div:first-child:hover {
        background-color: #3E444A;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='centered'><h1>RawSoftware</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='centered'><h3>Computer Programmer</h3></div>", unsafe_allow_html=True)

# About Me
st.markdown("<div class='centered'><h2>About Me</h2></div>", unsafe_allow_html=True)
st.markdown("<div class='centered'>Passionate software engineer with a focus on creating efficient and scalable solutions. I love tackling complex problems and turning ideas into reality through code.</div>", unsafe_allow_html=True)

# Skills
st.markdown("<div class='centered'><h2>Skills</h2></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.expander("Programming Languages"):
        st.write("- Python\n- JavaScript\n- Java\n- C++, C, C#")

    with st.expander("Web Technologies"):
        st.write("- HTML5\n- CSS\n- React\n- Streamlit")

with col2:
    with st.expander("Databases"):
        st.write("- MySQL\n- SQL Lite")

    with st.expander("Tools & Platforms"):
        st.write("- Github\n- VisualStudio")

# Projects
st.markdown("<div class='centered'><h2>Projects</h2></div>", unsafe_allow_html=True)

with st.expander("Accelerate AntiCheat (Private)"):
    st.write("**Description:** A simple but effecient AntiCheat for Minecraft")
    st.write("**Key Features:**")
    st.write("- Efficient \n - Packet Based \n - Machine Learning \n - Advanced Detections \n - Extremly LightWeight")
    st.write("**Technologies:** Java")

# Footer
st.markdown("<div class='centered'><p>© 2024 RawSoftware. All rights reserved.</p></div>", unsafe_allow_html=True)
