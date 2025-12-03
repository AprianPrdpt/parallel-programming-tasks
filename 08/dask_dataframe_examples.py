import dask.dataframe as dd
import pandas as pd

# ------------------------------------------------------------
# 1. READ & WRITE DATA
# ------------------------------------------------------------
print("=== READ & WRITE DATA ===")

pdf = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 40]
})

pdf.to_csv("people.csv", index=False)

ddf = dd.read_csv("people.csv")
print(ddf.head())

ddf.to_parquet("output_parquet", write_index=False)

ddf2 = dd.read_parquet("output_parquet")
print(ddf2.head())

# ------------------------------------------------------------
# 2. GROUPBY
# ------------------------------------------------------------
print("=== GROUPBY EXAMPLE ===")

data = pd.DataFrame({
    "category": ["A", "A", "B", "B", "C"],
    "value": [10, 20, 5, 15, 7]
})

data.to_csv("group.csv", index=False)

ddf_group = dd.read_csv("group.csv")

result = ddf_group.groupby("category")["value"].sum().compute()
print(result)

# ------------------------------------------------------------
# 3. GOTCHA'S FROM PANDAS TO DASK
# ------------------------------------------------------------
print("=== GOTCHAS (Pandas → Dask) ===")

print("Dask tidak langsung menghitung sampai .compute() dipanggil")

new_ddf = ddf.assign(age_plus_5 = ddf["age"] + 5)
print(new_ddf.head())

final_df = new_ddf.compute()
print(final_df)

# ------------------------------------------------------------
# 4. READING IN MESSY DATA
# ------------------------------------------------------------
print("=== MESSY DATA READING ===")

with open("messy.csv", "w") as f:
    f.write("name,age\n")
    f.write("Alice,25\n")
    f.write("Bob,thirty\n")
    f.write("Charlie,35\n")

messy = dd.read_csv("messy.csv", dtype={"age": "object"})
print(messy.compute())

print("Selesai!")
