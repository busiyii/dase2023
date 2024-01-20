import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# 散点图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.scatterplot(x='total_bill', y='tip', data=tips, color='orange', marker='o')
plt.title('Scatter Plot')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# 折线图
plt.subplot(1, 3, 2)
sns.lineplot(x='total_bill', y='tip', data=tips, color='green', linestyle='--')
plt.title('Line Plot')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# 柱状图
plt.subplot(1, 3, 3)
sns.barplot(x='day', y='total_bill', data=tips, color='blue')
plt.title('Bar Plot')
plt.xlabel('Day')
plt.ylabel('Total Bill')

plt.tight_layout()
plt.show()
