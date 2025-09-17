import streamlit as st
from dashboards import home, analytics_page

PAGES = {
    "Home": home,
    "Analytics": analytics_page
}

st.set_page_config(page_title="Insurance Dashboard", layout="wide")

st.title("📈 Insurance Dashboard")

# Selector de página
selection = st.sidebar.radio("Ir a", list(PAGES.keys()))
page = PAGES[selection]
page.app()
