import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load your dataset
try:
    df = pd.read_csv('Output.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Ensure Date is in datetime format
except Exception as e:
    print(f"Failed to load the dataset: {e}")
    # Exit if the dataset cannot be loaded
    import sys
    sys.exit(1)

# Ensure the DataFrame isn't empty and has the expected columns
if df.empty or not {'Vendor', 'Amount', 'Product ID', 'Date'}.issubset(df.columns):
    print("Dataset is empty or missing required columns.")
    sys.exit(1)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Transaction Summary Dashboard"),
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': i, 'value': i} for i in df['Vendor'].unique()],
        value=df['Vendor']. unique()[0],
        clearable=False,
        style={'width': '50%'}
    ),
    html.Div(id='summary-stats'),
    dcc.Graph(id='amount-by-vendor-chart'),
    dcc.Graph(id='product-popularity-chart'),
    dcc.Graph(id='sales-over-time-chart')  # New line graph component
])

# Callback to update summary stats
@app.callback(
    Output('summary-stats', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_summary_stats(selected_vendor):
    filtered_df = df[df['Vendor'] == selected_vendor]
    total_transactions = len(filtered_df)
    total_amount = filtered_df['Amount'].sum()
    return [
        html.H3(f'Total Transactions: {total_transactions}'),
        html.H3(f'Total Amount: ${total_amount:.2f}')
    ]

# Callback to update the vendor-specific chart
@app.callback(
    Output('amount-by-vendor-chart', 'figure'),
    Input('vendor-dropdown', 'value')
)
def update_chart(selected_vendor):
    filtered_df = df[df['Vendor'] == selected_vendor]
    fig = px.bar(filtered_df, x='Product ID', y='Amount', color='Product ID', title=f'Transaction Amounts for {selected_vendor}')
    return fig

# Callback for the product popularity chart
@app.callback(
    Output('product-popularity-chart', 'figure'),
    Input('vendor-dropdown', 'value')
)
def update_product_chart(selected_vendor):
    filtered_df = df[df['Vendor'] == selected_vendor]
    product_summary = filtered_df.groupby('Product ID')['Amount'].sum().reset_index()
    fig = px.bar(product_summary, x='Product ID', y='Amount', title='Most Purchased Products by Amount')
    return fig

# New callback for the sales over time line graph
@app.callback(
    Output('sales-over-time-chart', 'figure'),
    Input('vendor-dropdown', 'value')
)
def update_sales_over_time_chart(selected_vendor):
    filtered_df = df[df['Vendor'] == selected_vendor]
    time_summary = filtered_df.groupby('Date')['Amount'].sum().reset_index()
    fig = px.line(time_summary, x='Date', y='Amount', title='Sales Over Time')
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
