import streamlit as st
import uuid
from agent.graph import graph

st.set_page_config(
    page_title="Python Debugging Agent",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Debugging Agent")
st.write("Paste buggy Python code and let the agent fix it.")

# Problem statement
problem_statement = st.text_area(
    "Problem Statement (Optional)",
    placeholder="Example: Return factorial of n using recursion",
    height=120
)

# Code input
code = st.text_area(
    "Enter Python Code",
    placeholder="Paste your buggy Python code here...",
    height=300
)

# Button
if st.button("🚀 Debug Code", use_container_width=True):

    if code.strip() == "":
        st.warning("Please enter some code.")
    else:
        with st.spinner("Agent is debugging your code..."):

            initial_state = {
                "code": code,
                "error": "",
                "analysis": "",
                "iteration": 0,
                "problem_id": str(uuid.uuid4()),
                "problem_statement": problem_statement
            }

            try:
                result = graph.invoke(initial_state)

                st.success("Debugging Completed!")

                st.subheader("✅ Fixed Code")
                st.code(result["code"], language="python")

            except Exception as e:
                st.error("Something went wrong while debugging.")
                st.exception(e)

                