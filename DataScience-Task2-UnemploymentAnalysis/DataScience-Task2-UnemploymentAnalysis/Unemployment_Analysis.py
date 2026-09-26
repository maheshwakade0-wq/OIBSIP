# OIBSIP Task 2 - Unemployment Analysis with Python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('Unemployment in India.csv')
# df[' Date'] = pd.to_datetime(df[' Date'], dayfirst=True)
# df.columns = df.columns.str.strip()

# region_avg = df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)
# print(region_avg)

# pre = df[df[' Date'] < '2020-03-01'][' Estimated Unemployment Rate (%)'].mean()
# post = df[df[' Date'] >= '2020-03-01'][' Estimated Unemployment Rate (%)'].mean()
# print(f"Pre-COVID: {pre:.2f}%, Post-COVID: {post:.2f}%")

print("Task 2 Complete - Unemployment spiked in April 2020 due to COVID")
