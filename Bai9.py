import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('moitruong.csv')

# 1. Tính IQR cho NhietDo
Q1 = df['NhietDo'].quantile(0.25)
Q3 = df['NhietDo'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# 2. Đánh dấu outlier
df['Outlier'] = (df['NhietDo'] < lower) | (df['NhietDo'] > upper)

# 3. Thay outlier bằng median
median_nhiet = df['NhietDo'].median()
df.loc[df['Outlier'], 'NhietDo'] = median_nhiet

# 4. Thống kê trước/sau
print("Số outlier:", df['Outlier'].sum())
print("Thống kê NhietDo sau xử lý:", df['NhietDo'].describe())

# 5. Vẽ boxplot
df.boxplot(column='NhietDo')
plt.title('Boxplot NhietDo sau khi xử lý')
plt.show()