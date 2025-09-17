def compute_summary(df):
    return {
        "total": len(df),
        "avg_charges": df['charges'].mean(),
        "avg_age": df['age'].mean(),
        "avg_bmi": df['bmi'].mean()
    }
