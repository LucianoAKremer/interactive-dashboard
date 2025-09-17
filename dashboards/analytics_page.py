import streamlit as st
from analytics.data_processing import load_data
from analytics.plots import plot_charges_by_region, plot_bmi_vs_charges, plot_charges_by_smoker
from filters.filters import apply_filters

def app():
    st.header("📊 Análisis Interactivo")

    df = load_data()

    # Aplicar filtros dinámicos
    df_filtered = apply_filters(df)

    st.subheader("Charges por Región")
    st.plotly_chart(plot_charges_by_region(df_filtered), use_container_width=True)

    st.subheader("BMI vs Charges")
    st.plotly_chart(plot_bmi_vs_charges(df_filtered), use_container_width=True)

    st.subheader("Charges por Fumador")
    st.plotly_chart(plot_charges_by_smoker(df_filtered), use_container_width=True)
