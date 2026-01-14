import streamlit as st
from ai_train import generate_assignment_content

# Page config
st.set_page_config(page_title="Assignment Generator", layout="centered")

# UI
st.title("🎓 AI Assignment Generator")
st.write("This app uses a logic file to generate your work.")

topic = st.text_input(
    "Assignment Topic",
    placeholder="Enter the topic of your assignment..."
)

level = st.selectbox(
    "Complexity",
    ["Undergraduate", "Postgraduate", "PhD"]
)

if st.button("Generate Assignment"):
    if topic.strip():
        with st.spinner("Generating assignment..."):
            try:
                assignment = generate_assignment_content(topic, level)

                st.markdown("---")
                st.markdown(assignment)

                st.download_button(
                    label="📥 Download Text",
                    data=assignment,
                    file_name="assignment.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error generating assignment: {e}")
    else:
        st.warning("Please enter a topic.")
