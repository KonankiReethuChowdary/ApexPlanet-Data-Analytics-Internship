import pandas as pd
try:
    df = pd.read_excel(r"C:\Users\reeth\Downloads\ApexPlanet_DataAnalytics_Dataset (1).xlsx") 
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: Could not find your dataset file. Check the filename!")
print("\n--- Data Quality Check ---")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Duplicates: {df.duplicated().sum()}")
print("\nMissing Values per Column before cleaning:")
print(df.isnull().sum())
df_clean = df.drop_duplicates() 
if 'Age' in df_clean.columns:
    df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())
if 'order date' in df_clean.columns:
    df_clean['order date'] = pd.to_datetime(df_clean['order date'], errors='coerce')
if all(col in df_clean.columns for col in ['quantity', 'unit price', 'total sales']):
    df_clean['total sales'] = df_clean['quantity'] * df_clean['unit price']
df_clean.to_csv("cleaned_dataset.csv", index=False)
print("\n🎉 Success! 'cleaned_dataset.csv' has been created in your folder.")