import pandas as pd

df = pd.read_csv('sanpham.csv')

# 1 & 2. Loại bỏ ký tự tiền tệ và chuyển sang số
df['Gia'] = df['Gia'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['Gia'] = pd.to_numeric(df['Gia'], errors='coerce')

# 3. Chuẩn hóa DanhMuc về chữ thường
df['DanhMuc'] = df['DanhMuc'].str.lower().str.strip()

# 4. Loại sản phẩm tồn kho âm
df = df[df['SoLuongTon'] >= 0]

# 5. Sắp xếp theo Gia giảm dần
df = df.sort_values(by='Gia', ascending=False)

print(df.head())