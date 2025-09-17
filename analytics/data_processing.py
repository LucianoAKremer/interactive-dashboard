import pandas as pd

DATA_PATH = "data/insurance_dataset.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    # Limpieza básica
    df.dropna(inplace=True)
    df['sex'] = df['sex'].str.lower()
    df['smoker'] = df['smoker'].str.lower()
    df['region'] = df['region'].str.lower()
    return df
