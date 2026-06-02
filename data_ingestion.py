import pandas as pd
import os

path = r"C:\Users\suchithra\Downloads\MutualFundProject\data\raw"

files = os.listdir(path)

for file in files:

    if file.endswith(".csv") or file.endswith(".xlsx"):

        print("\n========================")
        print("FILE NAME:", file)
        print("========================")

        file_path = os.path.join(path, file)

        # Read CSV
        if file.endswith(".csv"):
            df = pd.read_csv(file_path)

        # Read Excel
        else:
            df = pd.read_excel(file_path)

        print("\nHEAD:")
        print(df.head())

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nMISSING VALUES:")
        print(df.isnull().sum())