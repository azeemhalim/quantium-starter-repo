import pandas as pd
import glob

# Step 1: Load all CSV files in the data folder
files = glob.glob('data/*.csv')

# Step 2: Read and combine them into one dataframe
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# Step 3: Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Step 4: Create sales column (quantity × price)
df["sales"] = df["quantity"] * df["price"]

# Step 5: Keep only sales, date, region
final_df = df[["sales", "date", "region"]]

# Step 6: Save to new CSV
final_df.to_csv("data/processed_sales.csv", index=False)

print("✅ Data processing complete! File saved as data/processed_sales.csv")