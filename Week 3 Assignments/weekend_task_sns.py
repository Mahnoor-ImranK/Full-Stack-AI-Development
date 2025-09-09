import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("DataSets\RealEstate-USA.csv")

# Show dataset info
print(df.head())
print(df.info())

# 1. Scatterplot: Price vs House Size
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="house_size", y="price", hue="city")
plt.title("Scatterplot: Price vs House Size by City")
plt.show()

# 2. Histogram of House Prices
plt.figure(figsize=(8,6))
sns.histplot(data=df, x="price", bins=30, kde=True)
plt.title("Distribution of House Prices")
plt.show()

# 3. Boxplot: Price by City
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="city", y="price")
plt.xticks(rotation=90)
plt.title("Boxplot: House Prices by City")
plt.show()

# 4. Countplot: Houses by State
plt.figure(figsize=(10,6))
sns.countplot(data=df, x="state", order=df['state'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Count of Houses by State")
plt.show()

# 5. KDE Plot of Price
plt.figure(figsize=(8,6))
sns.kdeplot(data=df, x="price", hue="city", warn_singular=False)
plt.title("KDE Plot of House Prices by City")
plt.show()

# 6. Pairplot for Price, Bed, Bath, House Size
sns.pairplot(df[["price", "bed", "bath", "house_size"]].dropna())
plt.show()

# 7. Violin Plot: Price by Beds
plt.figure(figsize=(8,6))
sns.violinplot(data=df, x="bed", y="price")
plt.title("Violin Plot: Price vs Number of Beds")
plt.show()

# 8. Heatmap of Correlation
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Heatmap of Correlation")
plt.show()

# 9. Barplot: Average Price by State
plt.figure(figsize=(12,6))
sns.barplot(data=df, x="state", y="price", estimator="mean")
plt.xticks(rotation=90)
plt.title("Average House Price by State")
plt.show()

# 10. Stripplot: Price by Beds
plt.figure(figsize=(8,6))
sns.stripplot(data=df, x="bed", y="price", jitter=True)
plt.title("Stripplot: Price by Beds")
plt.show()

# 11. Swarmplot: Price by Baths
plt.figure(figsize=(8,6))
sns.swarmplot(data=df, x="bath", y="price")
plt.title("Swarmplot: Price by Baths")
plt.show()

# 12. Regression plot: House Size vs Price
plt.figure(figsize=(8,6))
sns.regplot(data=df, x="house_size", y="price")
plt.title("Regression: House Size vs Price")
plt.show()

# 13. Jointplot: Acre Lot vs Price
sns.jointplot(data=df, x="acre_lot", y="price", kind="scatter")
plt.show()

# 14. Jointplot with KDE: Acre Lot vs Price
sns.jointplot(data=df, x="acre_lot", y="price", kind="kde")
plt.show()

# 15. Rugplot: House Prices
plt.figure(figsize=(8,6))
sns.rugplot(data=df, x="price")
plt.title("Rugplot: House Prices")
plt.show()

# 16. ECDF Plot: Price
plt.figure(figsize=(8,6))
sns.ecdfplot(data=df, x="price")
plt.title("ECDF Plot: House Prices")
plt.show()

# 17. Displot: Bed counts
sns.displot(df, x="bed", bins=10, kde=True)
plt.title("Distribution of Beds")
plt.show()

# 18. Catplot: Price by City
sns.catplot(data=df, x="city", y="price", kind="box", height=6, aspect=2)
plt.xticks(rotation=90)
plt.show()

# 19. Catplot: Price by State
sns.catplot(data=df, x="state", y="price", kind="violin", height=6, aspect=2)
plt.xticks(rotation=90)
plt.show()

# 20. Relplot: House Size vs Price
sns.relplot(data=df, x="house_size", y="price", hue="city", height=6)
plt.show()

# 21. Lineplot: prev_sold_date vs Price
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="prev_sold_date", y="price")
plt.xticks(rotation=90)
plt.title("Lineplot: Previous Sold Date vs Price")
plt.show()

# 22. Area plot (Lineplot with fill)
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="prev_sold_date", y="price", estimator="mean", errorbar=None)
plt.fill_between(df["prev_sold_date"].astype(str), df["price"], alpha=0.3)
plt.xticks(rotation=90)
plt.title("Area Plot: Price Trend by Sold Date")
plt.show()

# 23. Pointplot: Average Price by State
plt.figure(figsize=(10,6))
sns.pointplot(data=df, x="state", y="price")
plt.xticks(rotation=90)
plt.title("Pointplot: Average Price by State")
plt.show()

# 24. Lineplot: House Size vs Price
plt.figure(figsize=(8,6))
sns.lineplot(data=df, x="house_size", y="price")
plt.title("Lineplot: House Size vs Price")
plt.show()

# 25. Relplot with Size: House Size vs Price
sns.relplot(data=df, x="house_size", y="price", size="bed", hue="bath", height=6)
plt.title("Relplot: House Size vs Price with Bed/Bath")
plt.show()

# 26. Lineplot: prev_sold_date vs House Size
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="prev_sold_date", y="house_size")
plt.xticks(rotation=90)
plt.title("Lineplot: Previous Sold Date vs House Size")
plt.show()

# 27. Boxenplot: Price by State
plt.figure(figsize=(12,6))
sns.boxenplot(data=df, x="state", y="price")
plt.xticks(rotation=90)
plt.title("Boxenplot: Price by State")
plt.show()

# 28. Stripplot: House Size by State
plt.figure(figsize=(12,6))
sns.stripplot(data=df, x="state", y="house_size", jitter=True)
plt.xticks(rotation=90)
plt.title("Stripplot: House Size by State")
plt.show()

# 29. Heatmap: Average Price by Bed and Bath
pivot = df.pivot_table(values="price", index="bed", columns="bath", aggfunc="mean")
plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, cmap="coolwarm")
plt.title("Heatmap: Average Price by Bed & Bath")
plt.show()
