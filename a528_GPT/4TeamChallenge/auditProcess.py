import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

def plot_transactions_over_time(data, granularity):
    # Convert 'Invoice Date' to datetime
    data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])
    
    if granularity == 'Monthly':
        data['Period'] = data['Invoice Date'].dt.to_period('M')
    elif granularity == 'Quarterly':
        data['Period'] = data['Invoice Date'].dt.to_period('Q')

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

def display_csv(cutoff_window, data, frame, filter_active=False, trivial_materiality=None, random_selection=False, after_2023=False):
    # Clear previous treeview if exists
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a Treeview widget
    tree = ttk.Treeview(frame, columns=list(data.columns), show='headings')
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=100)

    # Scrollbars for the Treeview
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    # Inserting data into the Treeview
    if filter_active and trivial_materiality is not None:
        filtered_data = data[data['Sales Amount'] > trivial_materiality]
    else:
        filtered_data = data

    if after_2023:
        # Convert 'Invoice Date' to datetime if it's not already
        data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])
        filtered_data = data[data['Invoice Date'].dt.year > 2023]
    
    if random_selection:
        # Select 5 random rows from the filtered data if possible
        if len(filtered_data) > 5:
            filtered_data = filtered_data.sample(5)
        else:
            print("Not enough data to select 5 random entries.")

    for index, row in filtered_data.iterrows():
        tree.insert("", 'end', values=list(row))

    tree.pack(fill='both', expand=True)

def display_materiality_info(cutoff_window, total_revenue):
    overall_materiality = 0.005 * total_revenue
    trivial_materiality = 0.05 * overall_materiality

    materiality_frame = ttk.Frame(cutoff_window)
    materiality_frame.pack(pady=20, padx=10, fill='x', expand=False)

    label_overall = ttk.Label(materiality_frame, text=f"Overall Materiality: ${overall_materiality:,.2f}", font=('Helvetica', 14))
    label_overall.pack()

    label_trivial = ttk.Label(materiality_frame, text=f"Trivial Materiality: ${trivial_materiality:,.2f}", font=('Helvetica', 14))
    label_trivial.pack()
