import streamlit as st

st.title("Fairness Model Demonstration")
model = st.radio("Select a model", ["deBERTa", "Base Promt", "Few-Shot", "Self-Correction"])

if model == "deBERTa":
    st.write("deberta")
elif model == "Base Prompt":
    st.write("Base Prompt")
elif model == "Few-Shot":
    pass
elif model == "Self-Correction":
    pass
