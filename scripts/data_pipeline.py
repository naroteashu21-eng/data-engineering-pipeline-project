import pandas as pd

# Extract
data = pd.read_csv('data/sales_data.csv')

# Transform
data['total_price'] = data['price'] * data['quantity']

# Load
data.to_csv('data/processed_sales_data.csv', index=False)

print("Data pipeline executed successfully")
