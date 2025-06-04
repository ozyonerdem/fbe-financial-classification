import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

file = 'financial_data.csv'
train_file = 'train.csv'
test_file = 'test.csv'
validation_file = 'validation.csv'
target_column = "FBE_Sınıfı"
columns_to_drop = ["Şirket Adı", "Şirketin Kodu", "Periyot", "Yıl", "Görüs Tipi", "Altman Z-Skoru"]
truth_file = 'ground_truth.csv'

def read_csv(filename):
    return pd.read_csv(filename)

def drop_columns(df, cols):
    return df.drop(columns=cols)

def drop_zeros(df):
    numerics = df.select_dtypes(include='number').columns
    return df[(df[numerics] != 0).any(axis=1)]

def drop_nans(df):
    return df.dropna()

def add_colums_with_calculation(df, calculation, col):
    df[col] = df.apply(calculation, axis=1)

def split_dataset(df, col, file_to_test, file_to_train, file_valid, truth):
    df_trainval, df_valid = train_test_split(df, test_size=0.2, stratify=df[col], random_state=42)
    df_valid.to_csv(file_valid, index=False)
    df_train, df_test = train_test_split(df_trainval, test_size=0.125, stratify=df_trainval[col], random_state=42)
    df_test.to_csv(truth, index=False)
    df_test[col] = "?"
    df_train.to_csv(file_to_train, index=False)
    df_test.to_csv(file_to_test, index=False)

def assign_fbe(row):
    score = 0
    if row["Özsermaye Karlılığı (%)"] > 15: score += 2
    elif row["Özsermaye Karlılığı (%)"] > 5: score += 1
    if row["Faaliyet Kar Marjı"] > 10: score += 2
    elif row["Faaliyet Kar Marjı"] > 5: score += 1
    if row["Aktif Karlılık (%)"] > 5: score += 2
    elif row["Aktif Karlılık (%)"] > 2: score += 1
    if row["Cari Oran"] > 1.5: score += 2
    elif row["Cari Oran"] > 1: score += 1
    if row["Net Borç / FAVÖK"] < 3: score += 2
    elif row["Net Borç / FAVÖK"] < 6: score += 1
    if row["FAVÖK / Kısa Vade Borç"] > 0.5: score += 2
    elif row["FAVÖK / Kısa Vade Borç"] > 0.2: score += 1
    if row["Özsermaye / Aktif"] > 0.4: score += 2
    elif row["Özsermaye / Aktif"] > 0.25: score += 1
    if row["Net Satışlar / Kısa Vade Borç"] > 3: score += 2
    elif row["Net Satışlar / Kısa Vade Borç"] > 1.5: score += 1
    if score >= 10:
        return "Yuksek"
    elif score >= 6:
        return "Orta"
    else:
        return "Dusuk"

df1 = read_csv(file)
df1 = drop_columns(df1, columns_to_drop)
df1 = drop_zeros(df1)
df1 = drop_nans(df1)
add_colums_with_calculation(df1, assign_fbe, target_column)
split_dataset(df1, target_column, test_file, train_file, validation_file, truth_file)