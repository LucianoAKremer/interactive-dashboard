import plotly.express as px

def plot_charges_by_region(df):
    fig = px.bar(df.groupby("region")["charges"].mean().reset_index(),
                 x="region", y="charges", color="region",
                 labels={"charges":"Average Charges", "region":"Region"})
    return fig

def plot_bmi_vs_charges(df):
    fig = px.scatter(df, x="bmi", y="charges", color="smoker",
                     labels={"bmi":"BMI", "charges":"Charges", "smoker":"Smoker"})
    return fig

def plot_charges_by_smoker(df):
    fig = px.box(df, x="smoker", y="charges", color="smoker",
                 labels={"smoker":"Smoker", "charges":"Charges"})
    return fig
