import streamlit as st
from analytics.data_processing import load_data
from analytics.stats import compute_summary
from components.cards import metric_card

def app():
    st.header("🏠 Resumen General")
    
    df = load_data()

    summary = compute_summary(df)

    # Mostrar cards con métricas clave
    cols = st.columns(4)
    metric_card(cols[0], "Total Asegurados", summary["total"])
    metric_card(cols[1], "Promedio Charges", f"${summary['avg_charges']:.2f}")
    metric_card(cols[2], "Promedio Edad", f"{summary['avg_age']:.1f}")
    metric_card(cols[3], "Promedio BMI", f"{summary['avg_bmi']:.1f}")

    st.subheader("Primeros registros")
    st.dataframe(df.head())
