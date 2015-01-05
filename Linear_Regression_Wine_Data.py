#Load the dataset using pandas
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep = ';')
# Present the dataset
print df.describe()
# Calculate pairwise correlation matrix to see how 
#different variables are related to quality
print df.corr()

#Create some scatterplots of the data 
import matplotlib.pylab as plt
plt.scatter(df['alcohol'], df['quality'])
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Against Quality')
plt.show()
