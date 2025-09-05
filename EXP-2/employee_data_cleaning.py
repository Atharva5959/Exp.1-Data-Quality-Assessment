import pandas as pd

# Load CSV (fix if it comes as a single column)
file_path = r"C:\Users\Admin\Downloads\EXP-1 ASSIGNMENT-2\employee_data.csv"
df = pd.read_csv(file_path, sep=",", engine="python", encoding="utf-8-sig")

if df.shape[1] == 1:  # if only 1 column, split manually
    df = df[df.columns[0]].str.split(",", expand=True)
    df.columns = df.iloc[0]   # set header
    df = df.drop(0).reset_index(drop=True)

# Cleaning steps
df = df.drop_duplicates()

if "Salary" in df.columns:
    df["Salary"] = (
        df["Salary"].astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .replace("", "0").astype(float)
    ).fillna(df["Salary"].median())

if "Department" in df.columns:
    df["Department"] = df["Department"].fillna("Unknown").str.strip().str.title()

if "Joining_Date" in df.columns:
    df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], errors="coerce")

# Save cleaned file
output_file = r"C:\Users\Admin\Downloads\EXP-1 ASSIGNMENT-2\employee_data_cleaned.csv"
df.to_csv(output_file, index=False)

print("✅ Cleaned data saved at:", output_file)
print(df.head())
