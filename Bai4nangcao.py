import pandas as pd

df = pd.read_csv('reviews.csv')

# 1. Xóa trùng
df = df.drop_duplicates(subset=['UserName', 'Comment'])

# 2. Rating ngoài 1-5
df['Rating'] = df['Rating'].clip(1, 5)

# 3. Làm sạch Comment
df['Comment'] = df['Comment'].str.strip().str.replace(r'\s+', ' ', regex=True).str.replace(r'(!{2,})', '!', regex=True)

# 4. Tách độ dài bình luận
df['Comment_Length'] = df['Comment'].str.len()

# 5. Chuẩn hóa ProductCategory
df['ProductCategory'] = df['ProductCategory'].str.title().str.strip()

# 6. Thống kê
print("Điểm trung bình theo danh mục:\n", df.groupby('ProductCategory')['Rating'].mean().round(2))

df.to_csv('reviews_cleaned.csv', index=False, encoding='utf-8-sig')