import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n = 1024
X = np.linspace(0, 10, n)
Y_scatter = np.random.normal(0, 1, n)
Y_line = np.sin(X) + 0.2 * np.random.randn(n)
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, len(categories))

# 散点图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(X, Y_scatter, color='orange', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# 折线图
plt.subplot(1, 3, 2)
plt.plot(X, Y_line, color='orange', linestyle='--')
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# 柱状图
plt.subplot(1, 3, 3)
plt.bar(categories, values, color='orange')
plt.title('Bar Plot')
plt.xlabel('category')
plt.ylabel('value')
plt.legend()

plt.tight_layout()
plt.show()

