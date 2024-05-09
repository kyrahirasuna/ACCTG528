import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def plot_transactions_over_time(data, granularity):
    # Convert 'Sales Date' to datetime
    data['Sales Date'] = pd.to_datetime(data['Sales Date'])
    
    if granularity == 'Monthly':
        data['Period'] = data['Sales Date'].dt.to_period('M')
    elif granularity == 'Quarterly':
        data['Period'] = data['Sales Date'].dt.to_period('Q')

    # Group by the new 'Period' column and count transactions
    transaction_counts = data.groupby('Period').size()

    # Create a matplotlib Figure
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    transaction_counts.plot(kind='line', marker='o', linestyle='-', ax=ax)
    ax.set_title(f'Number of Transactions Over Time - {granularity}')
    ax.set_xlabel('Period')
    ax.set_ylabel('Number of Transactions')
    ax.grid(True)

    return fig

def compute_total_revenue(data):
    return data['Sales Amount'].sum()
