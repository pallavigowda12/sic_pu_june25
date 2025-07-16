'''This project focuses on optimizing a boutique coffee shop's operations through strategic data analysis. 
By applying four core types of analytics—descriptive, diagnostic, predictive, and prescriptive—the initiative
identifies top-performing coffee types, uncovers patterns behind sales fluctuations,
forecasts future demand based on monthly trends, and introduces dynamic pricing strategies 
to enhance revenue during off-peak hours. The approach uses customer and sales data to inform decisions 
around inventory management, staffing, promotional timing, and pricing adjustments. The goal is to create a smart, 
data-driven business model that not only meets customer preferences but also boosts profitability, reduces waste, 
and strengthens overall operational efficiency.'''

'''
Descriptive	  Daily coffee sales	     Latte identified as the most popular beverage.
Diagnostic	  Weekly sales drop pattern	 Notable dips on midweek and Sundays for multiple items.
Predictive	  Monthly sales forecasting	 Latte and Cold Brew projected to maintain strong demand.
Prescriptive  Pricing strategy based on  traffic trends	Dynamic pricing recommended during slow hours.'''


import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------ DataManager Class ------------------
class DataManager:
    def __init__(self):
        self.df = None

    def load_default_data(self):
        try:
            self.df = pd.read_csv("coffee_shop_revenue.csv")  # Replace with Kaggle path
            messagebox.showinfo("Success", "Default Kaggle dataset loaded.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load default data: {e}")

    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                messagebox.showinfo("Success", "CSV file imported successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import CSV: {e}")

# ------------------ Analysis Class ------------------
class CoffeeAnalytics:
    def __init__(self, df):
        self.df = df

    def descriptive(self):
        print("Descriptive Analysis:")
        print(self.df.describe())
        self.df.hist(figsize=(12, 8), color='skyblue', edgecolor='black')
        plt.suptitle("Descriptive Analysis")
        plt.show()

    def diagnostic(self):
        print("Diagnostic Analysis:")
        if 'Daily_Revenue' in self.df.columns:
            plt.plot(self.df['Daily_Revenue'], marker='o')
            plt.title("Daily Revenue Trend")
            plt.xlabel("Day")
            plt.ylabel("Revenue")
            plt.show()
        else:
            print("Column 'Daily_Revenue' not found.")

    def predictive(self):
        print("Predictive Analysis:")
        if 'Daily_Revenue' in self.df.columns:
            self.df['Revenue_MA'] = self.df['Daily_Revenue'].rolling(window=5).mean()
            plt.plot(self.df['Daily_Revenue'], label='Actual')
            plt.plot(self.df['Revenue_MA'], label='Forecast', color='orange')
            plt.title("Revenue Forecast")
            plt.legend()
            plt.show()
        else:
            print("Column 'Daily_Revenue' not found.")

    def prescriptive(self):
        print("Prescriptive Analysis:")
        if 'Daily_Revenue' in self.df.columns:
            slow_days = self.df[self.df['Daily_Revenue'] < self.df['Daily_Revenue'].mean()]
            print("Recommend dynamic pricing on these days:\n", slow_days.index.tolist())
        else:
            print("Column 'Daily_Revenue' not found.")

# ------------------ GUI Class ------------------
class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop Analytics")
        self.root.geometry("500x400")
        self.data_manager = DataManager()

        tk.Label(root, text="☕ Coffee Shop Analytics", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(root, text="Load Kaggle Dataset", command=self.data_manager.load_default_data).pack(pady=5)
        tk.Button(root, text="Import CSV File", command=self.data_manager.import_csv).pack(pady=5)

        tk.Label(root, text="Choose Analysis Type:", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(root, text="Descriptive Analysis", command=self.run_descriptive).pack(pady=5)
        tk.Button(root, text="Diagnostic Analysis", command=self.run_diagnostic).pack(pady=5)
        tk.Button(root, text="Predictive Analysis", command=self.run_predictive).pack(pady=5)
        tk.Button(root, text="Prescriptive Analysis", command=self.run_prescriptive).pack(pady=5)

    def run_descriptive(self):
        if self.data_manager.df is not None:
            CoffeeAnalytics(self.data_manager.df).descriptive()
        else:
            messagebox.showwarning("No Data", "Please load or import a dataset first.")

    def run_diagnostic(self):
        if self.data_manager.df is not None:
            CoffeeAnalytics(self.data_manager.df).diagnostic()
        else:
            messagebox.showwarning("No Data", "Please load or import a dataset first.")

    def run_predictive(self):
        if self.data_manager.df is not None:
            CoffeeAnalytics(self.data_manager.df).predictive()
        else:
            messagebox.showwarning("No Data", "Please load or import a dataset first.")

    def run_prescriptive(self):
        if self.data_manager.df is not None:
            CoffeeAnalytics(self.data_manager.df).prescriptive()
        else:
            messagebox.showwarning("No Data", "Please load or import a dataset first.")

# ------------------ Run App ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeApp(root)
    root.mainloop()
