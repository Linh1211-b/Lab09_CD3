import pandas as pd

df = pd.read_csv('chitieu.csv')

# 1 & 2. Loại SoTien <= 0
df = df[df['SoTien'] > 0]

# 3. Phân nhóm mức chi tiêu bằng pd.cut
bins = [0, 500000, 2000000, float('inf')]
labels = ['Thấp', 'Trung bình', 'Cao']
df['MucChiTieu'] = pd.cut(df['SoTien'], bins=bins, labels=labels)

# 4. Thống kê số giao dịch theo mức
print(df['MucChiTieu'].value_counts())

# 5. Tổng chi theo nhóm
print(df.groupby('NhomChiTieu')['SoTien'].sum())