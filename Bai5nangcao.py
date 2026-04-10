import pandas as pd

df = pd.read_csv('your_data.csv')

print("1. Mô tả dữ liệu gốc:")
print(df.info())
print(df.describe())
print("Missing values:\n", df.isna().sum())

# Xử lý missing
df = df.fillna({'numeric_col': df['numeric_col'].median(), 'text_col': 'Unknown'})

# Xử lý trùng
df = df.drop_duplicates()

# Chuẩn hóa
df['date_col'] = pd.to_datetime(df['date_col'])
df['category_col'] = df['category_col'].str.title().str.strip()

# Outlier (IQR)
Q1 = df['numeric_col'].quantile(0.25)
Q3 = df['numeric_col'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['numeric_col'] >= Q1-1.5*IQR) & (df['numeric_col'] <= Q3+1.5*IQR)]

# Tạo 3 biến mới (ví dụ)
df['total'] = df['col1'] * df['col2']
df['ratio'] = df['col1'] / df['col2']
df['age_group'] = pd.cut(df['age'], bins=[0,18,35,60,100], labels=['Trẻ','Trung niên','Người lớn','Cao tuổi'])

# Xuất
df.to_csv('data_cleaned.csv', index=False)
print("Hoàn thành! Dữ liệu sạch đã sẵn sàng cho phân tích/visualization/model.")