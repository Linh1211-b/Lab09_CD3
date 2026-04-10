import pandas as pd

df = pd.read_csv('suckhoe.csv')

# 1. Phát hiện Tuoi không hợp lệ
invalid_age = df[(df['Tuoi'] <= 0) | (df['Tuoi'] > 100)]
print("Dòng tuổi không hợp lệ:", len(invalid_age))

# 2 & 3. Điền thiếu CanNang, ChieuCao bằng trung vị
df['CanNang'] = df['CanNang'].fillna(df['CanNang'].median())
df['ChieuCao'] = df['ChieuCao'].fillna(df['ChieuCao'].median())

# 4. Chuẩn hóa NhomMau
df['NhomMau'] = df['NhomMau'].str.strip().str.upper()
df['NhomMau'] = df['NhomMau'].replace({
    'A+': 'A', 'A-': 'A', 'B+': 'B', 'B-': 'B',
    'AB+': 'AB', 'AB-': 'AB', 'O+': 'O', 'O-': 'O'
})

# 5. Tính BMI
df['BMI'] = df['CanNang'] / (df['ChieuCao']/100)**2

print(df.head())
print(df['BMI'].describe())