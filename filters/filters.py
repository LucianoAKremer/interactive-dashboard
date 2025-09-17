import streamlit as st

def apply_filters(df):
    st.sidebar.subheader("Filtros")

    sex_options = st.sidebar.multiselect("Sexo", df['sex'].unique(), default=df['sex'].unique())
    smoker_options = st.sidebar.multiselect("Fumador", df['smoker'].unique(), default=df['smoker'].unique())
    region_options = st.sidebar.multiselect("Región", df['region'].unique(), default=df['region'].unique())
    age_range = st.sidebar.slider("Rango de Edad", int(df['age'].min()), int(df['age'].max()),
                                  (int(df['age'].min()), int(df['age'].max())))
    bmi_range = st.sidebar.slider("Rango de BMI", int(df['bmi'].min()), int(df['bmi'].max()),
                                  (int(df['bmi'].min()), int(df['bmi'].max())))

    df_filtered = df[
        (df['sex'].isin(sex_options)) &
        (df['smoker'].isin(smoker_options)) &
        (df['region'].isin(region_options)) &
        (df['age'].between(age_range[0], age_range[1])) &
        (df['bmi'].between(bmi_range[0], bmi_range[1]))
    ]

    return df_filtered
