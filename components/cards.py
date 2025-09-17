import streamlit as st

def metric_card(col, title, value):
    with col:
        st.metric(label=title, value=value)
