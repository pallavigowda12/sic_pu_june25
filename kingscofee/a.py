import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Database Class ---
class Database:
    def __init__(self, db_name="kings_coffee.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS suppliers (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT UNIQUE NOT NULL,
                     contact TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS sales (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     coffee_type TEXT,
                     sweetener TEXT,
                     quantity INTEGER,
                     sale_date TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS feedback (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     water_quantity_rating TEXT,
                     comments TEXT,
                     feedback_date TEXT)''')
        self.conn.commit()

# --- Main Application Class ---
class KingsCoffeeApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Kings Coffee Management & Analysis App")
        self.seed_df = None
        self.sales_df = None
        self.feedback_df = None
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        self.tab_suppliers = ttk.Frame(tab_control)
        self.tab_sales = ttk.Frame(tab_control)
        self.tab_feedback = ttk.Frame(tab_control)
        self.tab_reports = ttk.Frame(tab_control)
        self.tab_data_analysis = ttk.Frame(tab_control)

        tab_control.add(self.tab_suppliers, text='Suppliers')
        tab_control.add(self.tab_sales, text='Sales')
        tab_control.add(self.tab_feedback, text='Feedback')
        tab_control.add(self.tab_reports, text='Reports')
        tab_control.add(self.tab_data_analysis, text='CSV Data Analysis')

        tab_control.pack(expand=1, fill="both")

        self.create_suppliers_tab()
        self.create_sales_tab()
        self.create_feedback_tab()
        self.create_reports_tab()
        self.create_data_analysis_tab()

    # --- Placeholder Tab Methods ---
    def create_suppliers_tab(self):
        frame = self.tab_suppliers
        ttk.Label(frame, text="Supplier Management Coming Soon...").pack(pady=20)

    def create_sales_tab(self):
        frame = self.tab_sales
        ttk.Label(frame, text="Sales Entry Coming Soon...").pack(pady=20)

    def create_feedback_tab(self):
        frame = self.tab_feedback
        ttk.Label(frame, text="Feedback Collection Coming Soon...").pack(pady=20)

    def create_reports_tab(self):
        frame = self.tab_reports
        ttk.Label(frame, text="Business Reports Coming Soon...").pack(pady=20)

    # --- Data Analysis Tab ---
    def create_data_analysis_tab(self):
        frame = self.tab_data_analysis
        ttk.Label(frame, text="Load CSV files for Data Analysis").grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Button(frame, text="Load Seed Purchases CSV", command=self.load_seed_csv).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frame, text="Load Sales CSV", command=self.load_sales_csv).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(frame, text="Load Feedback CSV", command=self.load_feedback_csv).grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(frame, text="Analysis Results:").grid(row=2, column=0, columnspan=3, pady=10)

        self.analysis_text = tk.Text(frame, width=80, height=25)
        self.analysis_text.grid(row=3, column=0, columnspan=3, padx=10)

        ttk.Button(frame, text="Run Full Analysis", command=self.run_full_analysis).grid(row=4, column=1, pady=10)

    # --- CSV Loaders ---
    def load_seed_csv(self):
        file_path = filedialog.askopenfilename(title="Select Seed Purchases CSV",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.seed_df = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Seed purchases data loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load seed purchases CSV.\n{e}")

    def load_sales_csv(self):
        file_path = filedialog.askopenfilename(title="Select Sales CSV",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.sales_df = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Sales data loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load sales CSV.\n{e}")

    def load_feedback_csv(self):
        file_path = filedialog.askopenfilename(title="Select Feedback CSV",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.feedback_df = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Feedback data loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load feedback CSV.\n{e}")

    # --- Analysis Runner ---
    def run_full_analysis(self):
        self.analysis_text.delete("1.0", tk.END)
        if self.seed_df is None or self.sales_df is None or self.feedback_df is None:
            messagebox.showwarning("Missing Data", "Please load all three CSV files before analysis.")
            return

        try:
            supplier_summary = self.seed_df.groupby('supplier').agg(
                total_quantity_kg=('quantity_kg', 'sum'),
                total_cost=('cost_per_kg', lambda x: np.sum(self.seed_df.loc[x.index, 'quantity_kg'] * x))
            ).reset_index()

            self.analysis_text.insert(tk.END, "=== Supplier Summary ===\n")
            self.analysis_text.insert(tk.END, supplier_summary.to_string(index=False) + "\n\n")

            coffee_sales = self.sales_df.groupby('coffee_type')['quantity_sold'].sum()
            self.analysis_text.insert(tk.END, "=== Sales Quantity by Coffee Type ===\n")
            self.analysis_text.insert(tk.END, coffee_sales.to_string() + "\n\n")

            feedback_counts = self.feedback_df['water_quantity_rating'].value_counts()
            self.analysis_text.insert(tk.END, "=== Customer Feedback on Water Quantity ===\n")
            self.analysis_text.insert(tk.END, feedback_counts.to_string() + "\n\n")

            sweetener_sales = self.sales_df.groupby('sweetener')['quantity_sold'].sum()
            self.analysis_text.insert(tk.END, "=== Sales Quantity by Sweetener ===\n")
            self.analysis_text.insert(tk.END, sweetener_sales.to_string() + "\n\n")

            if messagebox.askyesno("Show Plots?", "Would you like to see charts for the analysis?"):
                self.show_plots(coffee_sales, sweetener_sales, feedback_counts)

        except Exception as e:
            messagebox.showerror("Analysis Error", f"Error during analysis:\n{e}")

    def show_plots(self, coffee_sales, sweetener_sales, feedback_counts):
        plt.figure(figsize=(10,6))
        coffee_sales.plot(kind='bar', title='Coffee Sales by Type')
        plt.ylabel('Quantity Sold')
        plt.show()

        plt.figure(figsize=(10,6))
        sweetener_sales.plot(kind='bar', title='Sales by Sweetener')
        plt.ylabel('Quantity Sold')
        plt.show()

        plt.figure(figsize=(10,6))
        feedback_counts.plot(kind='bar', title='Water Quantity Feedback')
        plt.ylabel('Number of Responses')
        plt.show()

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = KingsCoffeeApp(root)
    root.mainloop()
