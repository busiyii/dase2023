import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('white',{'font.sans-serif':['simhei','Arial']})
data = pd.read_csv('data0.csv')
df = data.iloc[:, 2:7]
result = np.corrcoef(df, rowvar=False)
print(result)
sns.pairplot(df,kind='reg')
plt.savefig("相关性.png")
plt.show()