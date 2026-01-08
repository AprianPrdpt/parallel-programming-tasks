# Tip: For faster performance on large files in pandas 2.0+, use the pyarrow engine
# airbnb_data = pd.read_csv("data/listings_austin.csv", engine="pyarrow")
import pandas as pd
import time

start_time = time.perf_counter()
# Read the CSV file
flights_data = pd.read_csv("../nycflights.csv")
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")

# View the first 5 rows
#flights_data.head()
