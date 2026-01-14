import streamlit as st
from ai_train import generate_assignment_content

st.set_page_config(page_title="Assignment Generator", layout="centered", page_icon="🎓")

st.title("🎓 AI Assignment Generator")
st.info("Provide a topic and complexity level to generate a full-length academic assignment.")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Assignment Topic", placeholder="e.g., The Impact of Quantum Computing on Cryptography")

with col2:
    level = st.selectbox("Complexity Level", ["Undergraduate", "Postgraduate", "PhD"])

# Execution Section
if st.button("Generate Assignment", use_container_width=True):
    if topic.strip():
        with st.spinner("Writing your assignment... this may take a minute..."):
            assignment = generate_assignment_content(topic, level)
            
            if "Error" in assignment:
                st.error(assignment)
            else:
                st.markdown("---")
                st.markdown(assignment)
                
                st.download_button(
                    label="📥 Download Assignment (.txt)",
                    data=assignment,
                    file_name=f"{topic.replace(' ', '_')}_assignment.txt",
                    mime="text/plain"
                )
    else:
        st.warning("Please enter a topic before generating.")