"""
Superstore Business Intelligence & DAX Analytics Pipeline
Author: Akash V (@akashvenkey)
"""
import pandas as pd
import numpy as np

def calculate_superstore_kpis(df):
    """Compute core retail DAX KPI equivalents."""
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    profit_margin_pct = (total_profit / total_sales) * 100 if total_sales else 0
    avg_discount = df['Discount'].mean() * 100
    
    return {
        "Total Sales ($)": round(total_sales, 2),
        "Total Profit ($)": round(total_profit, 2),
        "Profit Margin (%)": round(profit_margin_pct, 2),
        "Average Discount (%)": round(avg_discount, 2),
        "Total Transaction Count": len(df)
    }

if __name__ == "__main__":
    # Simulated validation dataset matching Superstore schema
    sample_data = {
        'Sales': [261.96, 731.94, 14.62, 957.5775, 48.86],
        'Profit': [41.9136, 219.582, 6.8714, -383.031, 14.1694],
        'Discount': [0.0, 0.0, 0.0, 0.45, 0.0],
        'Category': ['Furniture', 'Furniture', 'Office Supplies', 'Furniture', 'Office Supplies']
    }
    df = pd.DataFrame(sample_data)
    kpis = calculate_superstore_kpis(df)
    print("=== Superstore BI Executive Metrics Summary ===")
    for k, v in kpis.items():
        print(f"{k}: {v}")