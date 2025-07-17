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
import pandas as pd
import matplotlib.pyplot as plt

'''Database managment'''
class DataManager:
    def __init__(self):
        self.df = None

    def load_kaggle_data(self):
        try:
            self.df = pd.read_csv("coffee_shop_data.csv")  # Change to Kaggle file name
            messagebox.showinfo("Loaded", "Kaggle dataset loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load Kaggle data.\n{e}")

    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            try:
                self.df = pd.read_csv(path)
                messagebox.showinfo("Imported", "CSV file imported.")
            except Exception as e:
                messagebox.showerror("Error", f"CSV import failed.\n{e}")

'''Data Analysis'''
class CoffeeAnalytics:
    def __init__(self, df):
        self.df = df
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

    def descriptive(self): #Dialy Cofee Sales
        print("\n📊 Descriptive Analysis:")
        print(self.df.describe())
        print("\nBy Coffee Type:")
        print(self.df.groupby('Coffee_Type')[['Units_Sold', 'Daily_Revenue']].sum())
        self.df.groupby('Coffee_Type')['Daily_Revenue'].sum().plot(kind='bar', color='sienna')
        plt.title("Total Revenue by Coffee Type")
        plt.ylabel("Revenue ₹"); plt.xticks(rotation=45); plt.tight_layout(); plt.show()

    def diagnostic(self): #Weekly Cofee Sales
        print("\n🔍 Diagnostic Analysis:")
        for c in self.df['Coffee_Type'].unique():
            sub = self.df[self.df['Coffee_Type'] == c]
            plt.plot(sub['Date'], sub['Daily_Revenue'], marker='o', label=c)
        plt.title("Daily Revenue Trend by Coffee Type")
        plt.xlabel("Date"); plt.ylabel("Revenue ₹")
        plt.legend(); plt.xticks(rotation=45); plt.tight_layout(); plt.show()

    def predictive(self): #Monthly Sales forecasting
        print("\n📈 Predictive Analysis:")
        for c in self.df['Coffee_Type'].unique():
            sub = self.df[self.df['Coffee_Type'] == c].copy()
            sub['Forecast'] = sub['Daily_Revenue'].rolling(window=3).mean()
            plt.plot(sub['Date'], sub['Forecast'], label=f"{c} Forecast")
        plt.title("Forecasted Revenue (Moving Average)")
        plt.xlabel("Date"); plt.ylabel("Revenue ₹")
        plt.legend(); plt.xticks(rotation=45); plt.tight_layout(); plt.show()

    def prescriptive(self): #Pricing Strategy
        print("\n🧠 Prescriptive Analysis:")
        avg = self.df['Daily_Revenue'].mean()
        slow = self.df[self.df['Daily_Revenue'] < avg]
        print("Days Below Average:\n", slow[['Date', 'Coffee_Type', 'Daily_Revenue']])
        print("\nCoffee Types to Consider for Dynamic Pricing:")
        print(slow['Coffee_Type'].value_counts())
        slow.groupby('Coffee_Type')['Daily_Revenue'].mean().plot(kind='barh', color='crimson')
        plt.title("Target Types for Pricing Strategy")
        plt.xlabel("Avg Revenue ₹"); plt.tight_layout(); plt.show()

 #Graphical User Interface
class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kings Coffee Intelligence System ☕")
        self.root.geometry("500x430")
        self.data = DataManager()

        tk.Label(root, text="Coffee Analytics Dashboard", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(root, text="Load Kaggle Dataset", command=self.data.load_kaggle_data).pack(pady=5)
        tk.Button(root, text="Import Custom CSV", command=self.data.import_csv).pack(pady=5)
        tk.Label(root, text="Select Analysis Type:", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(root, text="📊 Dialy cofee sales", command=self.run_descriptive).pack(pady=5)
        tk.Button(root, text="🔍 Weekly sales of a cofee", command=self.run_diagnostic).pack(pady=5)
        tk.Button(root, text="📈 Monthly sales forecasting", command=self.run_predictive).pack(pady=5)
        tk.Button(root, text="🧠 Pricing Strategy", command=self.run_prescriptive).pack(pady=5)

    def run_descriptive(self):
        if self.data.df is not None: CoffeeAnalytics(self.data.df).descriptive()
        else: messagebox.showwarning("No Data", "Please load a dataset.")

    def run_diagnostic(self):
        if self.data.df is not None: CoffeeAnalytics(self.data.df).diagnostic()
        else: messagebox.showwarning("No Data", "Please load a dataset.")

    def run_predictive(self):
        if self.data.df is not None: CoffeeAnalytics(self.data.df).predictive()
        else: messagebox.showwarning("No Data", "Please load a dataset.")

    def run_prescriptive(self):
        if self.data.df is not None: CoffeeAnalytics(self.data.df).prescriptive()
        else: messagebox.showwarning("No Data", "Please load a dataset.")

#Main function
if __name__ == "__main__":
    root = tk.Tk()
    CoffeeApp(root)
    root.mainloop()
