import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from auditProcess import plot_transactions_over_time, compute_total_revenue

def load_file():
    global data
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        data = pd.read_csv(filepath)
        total_revenue = compute_total_revenue(data)
        revenue_text.set(f"Total Revenue: ${total_revenue:.2f}")
        combo_granularity.set('Choose Granularity')
        result_text.set("File loaded successfully.")

def show_graph():
    if 'data' in globals():
        granularity = combo_granularity.get()
        fig = plot_transactions_over_time(data, granularity)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    else:
        result_text.set("Please load a CSV file first.")

def open_cutoff_testing_dashboard():
    cutoff_window = tk.Toplevel(root)
    cutoff_window.title("Cutoff Testing Dashboard")
    label = tk.Label(cutoff_window, text="Cutoff Testing Dashboard", font=('Helvetica', 16))
    label.pack(pady=20)
    # Additional widgets and functionalities can be added here for cutoff testing

def run_gui():
    global result_text, combo_granularity, root, revenue_text
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

    root.mainloop()

if __name__ == "__main__":
    run_gui()
