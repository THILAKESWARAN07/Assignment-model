import streamlit as st
from ai_train import generate_assignment_content 

st.set_page_config(page_title="Assignment Generator", layout="centered")

st.title("🎓 AI Assignment Generator")
st.write("This app uses a logic file to generate your work.")


topic = st.text_input("Assignment Topic", placeholder="Enter the topic of your assignment...")
level = st.selectbox("Complexity", ["Undergraduate", "Postgraduate", "PhD"])

if st.button("Generate Assignment"):
    if topic:
        with st.spinner("Generating assignment..."):
         
            assignment = generate_assignment_content(topic, level)
            
            st.markdown("---")
            st.markdown(assignment)
            
            st.download_button("Download Text", assignment, file_name="assignment.txt")
    else:
        st.warning("Please enter a topic.")