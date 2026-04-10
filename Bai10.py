import pandas as pd

df = pd.read_csv('lienhe.csv')

# 1. Email về chữ thường
df['Email'] = df['Email'].str.lower().str.strip()

# 2. Kiểm tra email hợp lệ (rất đơn giản)
df['Email_Valid'] = df['Email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', regex=True, na=False)

# 3. Tách đầu số điện thoại (ví dụ: 10 số Việt Nam)
df['DauSo'] = df['SoDienThoai'].astype(str).str.extract(r'(\d{3,4})')  # 3-4 số đầu

# 4. Xóa khoảng trắng thừa DiaChi
df['DiaChi'] = df['DiaChi'].str.strip().str.replace(r'\s+', ' ', regex=True)

# 5. Trích xuất Domain
df['Domain'] = df['Email'].str.extract(r'@([\w\.-]+)')

print(df.head())
print("Email không hợp lệ:", (~df['Email_Valid']).sum())