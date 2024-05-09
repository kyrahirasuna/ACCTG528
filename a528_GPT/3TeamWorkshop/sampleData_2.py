import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# Number of transactions
n = 10000

# Generate dates
start_date = datetime(2022, 12, 1)
end_date = datetime(2024, 1, 31)
date_range = (end_date - start_date).days
invoice_dates = [start_date + timedelta(days=np.random.randint(date_range)) for _ in range(n)]
invoice_dates.sort()  # Sort the dates to maintain chronological order

# Generate delivery dates by adding random days to sales dates
delivery_dates = [date + timedelta(days=np.random.randint(1, 14)) for date in invoice_dates]

# Generate sales amount following a normal distribution with mean 1000 and standard deviation 500
sales_amounts = np.random.normal(1000, 500, n).round(2)
# Ensure no negative sales amounts
sales_amounts = np.where(sales_amounts < 10, 10, sales_amounts)

# Generate transaction IDs and invoice numbers
transaction_ids = np.arange(1, n+1)
invoice_numbers = np.arange(1001, 1001+n)

# Generate random customer IDs from a set of 50 possible IDs
customer_ids = np.random.choice(50, n) + 1  # Customer IDs start at 1

# Create DataFrame
df = pd.DataFrame({
    'Transaction ID': transaction_ids,
    'Invoice Date': invoice_dates,
    'Delivery Date': delivery_dates,
    'Sales Amount': sales_amounts,
    'Invoice Number': invoice_numbers,
    'Customer ID': customer_ids
})

# Save to CSV
df.to_csv('synthetic_sales_data_final2.csv', index=False)

print("The dataset has been successfully saved as 'synthetic_sales_data_final2.csv'.")
