import pandas as pd

sales = pd.read_csv("sales.csv")
products = pd.read_csv("products.csv")

# Profiling
print("Sales Info:")
sales.info()

print("\nSales Describe:")
print(sales.describe())

# Method Chaining (Correct)
pivot = (
    sales
    .merge(products, on="product_id")   # FIXED
    .pivot_table(values="amount",
                 index="region",
                 columns="product_name",
                 aggfunc="sum")
)

print("\nPivot Table:")
print(pivot)