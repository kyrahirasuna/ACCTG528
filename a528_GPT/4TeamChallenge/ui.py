import tkinter as tk
from tkinter import ttk, filedialog, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from auditProcess import plot_transactions_over_time, compute_total_revenue, display_csv

def load_file():
    global data, total_revenue, overall_materiality, trivial_materiality
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        data = pd.read_csv(filepath)
        total_revenue = compute_total_revenue(data)
        overall_materiality = 0.005 * total_revenue  # Calculating materiality as 0.5% of total revenue
        trivial_materiality = 0.05 * overall_materiality  # Calculating trivial materiality as 5% of overall materiality
        revenue_text.set(f"Total Revenue: ${total_revenue:,.2f}")
        materiality_text.set(f"Overall Materiality: ${overall_materiality:,.2f}")
        trivial_materiality_text.set(f"Trivial Materiality: ${trivial_materiality:,.2f}")
        combo_granularity.set('Choose Granularity')


def open_cutoff_testing_dashboard():
    global trivial_materiality, overall_materiality
    cutoff_window = tk.Toplevel(root)
    cutoff_window.title("Cutoff Testing Dashboard")
    cutoff_window.geometry("800x600")

    table_frame = ttk.Frame(cutoff_window)
    table_frame.pack(fill='both', expand=True, padx=10, pady=10)

 # Labels for displaying materiality values
    overall_mat_label = Label(cutoff_window, text=f"Overall Materiality: ${overall_materiality:,.2f}", font=('Helvetica', 14))
    overall_mat_label.pack(pady=(10, 0))

    trivial_mat_label = Label(cutoff_window, text=f"Trivial Materiality: ${trivial_materiality:,.2f}", font=('Helvetica', 14))
    trivial_mat_label.pack(pady=(10, 0))
    filter_button = ttk.Button(cutoff_window, text="Filter for Above Trivial", command=lambda: apply_filter_and_show_random_button(cutoff_window, data, table_frame, trivial_materiality))
    filter_button.pack(pady=10)

    after_2023_button = ttk.Button(cutoff_window, text="Filter for Post-2023 Invoices", command=lambda: display_csv(cutoff_window, data, table_frame, after_2023=True))
    after_2023_button.pack(pady=10)

    global random_button
    random_button = ttk.Button(cutoff_window, text="Sample Data", command=lambda: display_csv(cutoff_window, data, table_frame, True, trivial_materiality, True))
    random_button.pack_forget()  # Initially, do not show the random button

    display_csv(cutoff_window, data, table_frame)  # Initially display all data

    # Initially display all data
    if 'data' in globals():
        display_csv(cutoff_window, data, table_frame)

def apply_filter_and_show_random_button(cutoff_window, data, table_frame, trivial_materiality):
    display_csv(cutoff_window, data, table_frame, True, trivial_materiality)
    random_button.pack(pady=10)  # Show the random button after filtering
        
def show_graph():
    if 'data' in globals():
        granularity = combo_granularity.get()
        fig = plot_transactions_over_time(data, granularity)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    else:
        result_text.set("Please load a CSV file first.")
def run_gui():
    global result_text, combo_granularity, root, revenue_text, materiality_text, trivial_materiality_text
    root = tk.Tk()
    root.title("Audit Revenue Testing")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    btn_load = tk.Button(frame, text="Load CSV", command=load_file)
    btn_load.pack(fill=tk.X)

    options = ['Monthly', 'Quarterly']
    combo_granularity = ttk.Combobox(frame, values=options, state="readonly")
    combo_granularity.pack(fill=tk.X)
    combo_granularity.set('Choose Granularity')

    btn_show_graph = tk.Button(frame, text="Show Graph", command=show_graph)
    btn_show_graph.pack(fill=tk.X)

    btn_open_cutoff = tk.Button(frame, text="Open Cutoff Testing Dashboard", command=open_cutoff_testing_dashboard)
    btn_open_cutoff.pack(fill=tk.X, pady=10)

    result_text = tk.StringVar()
    label_result = tk.Label(frame, textvariable=result_text, wraplength=300)
    label_result.pack(pady=(10, 0))

    revenue_text = tk.StringVar()
    label_revenue = tk.Label(frame, textvariable=revenue_text, font=('Helvetica', 16))
    label_revenue.pack(pady=(10, 0))

    materiality_text = tk.StringVar()
    label_materiality = tk.Label(frame, textvariable=materiality_text, font=('Helvetica', 16))
    label_materiality.pack(pady=(10, 0))
    trivial_materiality_text = tk.StringVar()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
