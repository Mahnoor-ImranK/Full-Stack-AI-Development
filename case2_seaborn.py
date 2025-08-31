import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('G:/FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer/DataSetForPractice/FastFoodRestaurants.csv')

print(df.dtypes)

# Filter top 40 rows
dffilter = df.head(40)
print(dffilter)

sns.set(style="whitegrid")

# Scatterplot: Latitude vs Longitude (restaurant locations)
sns.scatterplot(data=dffilter, x="longitude", y="latitude", hue="province")
plt.title('Restaurant Locations by Province')
plt.show()

# KDE Plot: Density of restaurant locations
sns.displot(data=dffilter, x="longitude", y="latitude", kind='kde')
plt.title('Density of Restaurant Locations')
plt.show()

# Histplot: Distribution of restaurants across longitude and latitude
sns.histplot(data=dffilter, x="longitude", y="latitude")
plt.title('Geographic Distribution of Restaurants')
plt.show()

# Lineplot: Longitude trend across restaurant names
sns.lineplot(data=dffilter, x="name", y="longitude")
plt.xticks(rotation=90)
plt.title('Longitude by Restaurant Name')
plt.show()

# Barplot: Number of restaurants per province (using count)
sns.countplot(data=dffilter, x="province")
plt.xticks(rotation=45)
plt.title('Restaurant Count by Province')
plt.show()

# Catplot: Distribution of restaurants by city
sns.catplot(data=dffilter, x="city", kind="count", height=5, aspect=2)
plt.xticks(rotation=90)
plt.title('Restaurant Count by City')
plt.show()

# Pivot and Heatmap: Count of restaurants by city and province
glue = dffilter.pivot_table(index="city", columns="province", values="name", aggfunc='count')
sns.heatmap(glue, annot=True, fmt="d", cmap="YlOrRd")
plt.title('Restaurant Count by City and Province')
plt.show()
