import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('G:/FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer/DataSetForPractice/startup_growth_investment_data.csv')

print(df.dtypes)

# Filter top 40 rows
dffilter = df.head(40)
print(dffilter)

sns.set(style="whitegrid")

# Scatterplot: Investment Amount vs Valuation, colored by Industry
sns.scatterplot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)", hue="Industry")
plt.title('Investment vs Valuation by Industry')
plt.show()

# KDE Plot: Growth Rate vs Investment Amount
sns.displot(data=dffilter, x="Growth Rate (%)", y="Investment Amount (USD)", kind='kde')
plt.title('Growth Rate vs Investment Density')
plt.show()

# Histplot: Funding Rounds vs Number of Investors
sns.histplot(data=dffilter, x="Funding Rounds", y="Number of Investors")
plt.title('Funding Rounds vs Investor Count')
plt.show()

# Lineplot: Valuation trend across Startup Names
sns.lineplot(data=dffilter, x="Startup Name", y="Valuation (USD)")
plt.xticks(rotation=90)
plt.title('Valuation by Startup')
plt.show()

# Barplot: Average Growth Rate by Industry
sns.barplot(data=dffilter, x="Industry", y="Growth Rate (%)", errorbar=None)
plt.xticks(rotation=45)
plt.title('Growth Rate by Industry')
plt.show()

# Catplot: Investment Amount by Country
sns.catplot(data=dffilter, x="Country", y="Investment Amount (USD)", kind="box", height=5, aspect=2)
plt.xticks(rotation=45)
plt.title('Investment Distribution by Country')
plt.show()

# Pivot and Heatmap: Average Valuation by Industry and Country
glue = dffilter.pivot_table(index="Industry", columns="Country", values="Valuation (USD)", aggfunc='mean')
sns.heatmap(glue, annot=True, fmt=".0f", cmap="Blues")
plt.title('Average Valuation by Industry and Country')
plt.show()
