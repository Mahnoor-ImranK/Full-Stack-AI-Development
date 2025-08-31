import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('G:\FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer\DataSetForPractice\RealEstate-USA.csv')

print(df.dtypes)
dffilter= df.head(40)
print(dffilter)

sns.set(style="whitegrid")

#scatterplot
sns.scatterplot(data=dffilter, x="bed", y="price", hue="bath")
plt.title('Bed vs Price')
plt.show()

#kind='kde'
sns.displot(data=dffilter, x="acre_lot" , y="price", kind='kde')
plt.title('Acre Lot vs Price')
plt.show()

#histplot
sns.histplot(data=dffilter, x="acre_lot" , y="price")
plt.title('Acre Lot vs Price')
plt.show()

# The relationship between x and y
sns.lineplot(data=dffilter, x="bed" , y="price"  )
plt.title('Bed vs Price')
plt.show()

#barplot
sns.barplot(data=dffilter, x="acre_lot", y="price", legend=False)
plt.title('Acre Lot vs Price')
plt.show()

#catplot
sns.catplot(data=dffilter, x="bed", y="price")
plt.title('Bed vs Price')
plt.show()

#pivot and heatmap
glue = dffilter.pivot(columns="bed", values="price")
sns.heatmap(glue)
plt.title('Bed vs Price')
plt.show()
