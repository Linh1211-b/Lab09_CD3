import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('diem_sinhvien.csv')

print("Dữ liệu ban đầu:")
print(df.head())
print("\nGiá trị thiếu:")
print(df.isna().sum())

# 1. Kiểm tra giá trị thiếu ở các cột điểm
missing_diem = df[['DiemQT', 'DiemThi']].isna().sum()
print("\nThiếu ở DiemQT và DiemThi:\n", missing_diem)

# 2. Điền thiếu bằng trung bình cột
df['DiemQT'] = df['DiemQT'].fillna(df['DiemQT'].mean())
df['DiemThi'] = df['DiemThi'].fillna(df['DiemThi'].mean())

# 3. Điền thiếu HoTen
df['HoTen'] = df['HoTen'].fillna("ChuaCapNhat")

# 4. Tính lại DiemTK
df['DiemTK'] = 0.4 * df['DiemQT'] + 0.6 * df['DiemThi']

# 5. Thêm cột XepLoai
def xep_loai(diem):
    if diem >= 9.0: return 'A'
    elif diem >= 7.0: return 'B'
    elif diem >= 5.0: return 'C'
    else: return 'D'

df['XepLoai'] = df['DiemTK'].apply(xep_loai)

print("\nDữ liệu sau khi làm sạch:")
print(df.head())
print(df[['DiemQT', 'DiemThi', 'DiemTK', 'XepLoai']].describe())