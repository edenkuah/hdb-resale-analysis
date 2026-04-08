import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def thousands_formatter(x, pos):
    return f"{int(x/1000)}k"
df = pd.read_csv('Resale_Flat_Prices.csv')

average_prices = df.groupby('town')['resale_price'].mean().sort_values(ascending=False)
top_10_avg = average_prices[:10]

print(top_10_avg.head())
plt.figure(figsize=(10, 6))
plt.bar(top_10_avg.index, top_10_avg.values)

plt.xlabel("Towns")
plt.ylabel("Prices")
plt.title("Top 10 most expensive HDB towns (in terms of resale prices)")
plt.ylim(bottom=0)

plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.show()
