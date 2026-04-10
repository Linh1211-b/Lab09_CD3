import pandas as pd

df = pd.read_csv('tuyensinh.csv')

# 1. Chuẩn hóa họ tên, giới tính, ngày sinh
df['HoTen'] = df['HoTen'].str.strip().str.title()
df['GioiTinh'] = df['GioiTinh'].str.strip().str.title().replace({'Nam': 'Nam', 'Nữ': 'Nữ', 'Nu': 'Nữ'})
df['NgaySinh'] = pd.to_datetime(df['NgaySinh'], format='mixed', errors='coerce')

# 2. Xử lý dữ liệu thiếu
df['DiemToan'] = df['DiemToan'].fillna(df['DiemToan'].median())
df['DiemVan'] = df['DiemVan'].fillna(df['DiemVan'].median())
df['DiemAnh'] = df['DiemAnh'].fillna(df['DiemAnh'].median())
df['HoTen'] = df['HoTen'].fillna('ChuaCapNhat')

# 3. Phát hiện điểm ngoài 0-10
invalid = df[(df['DiemToan'] < 0) | (df['DiemToan'] > 10) |
             (df['DiemVan'] < 0) | (df['DiemVan'] > 10) |
             (df['DiemAnh'] < 0) | (df['DiemAnh'] > 10)]
print("Điểm không hợp lệ:\n", invalid)

# Sửa điểm ngoài khoảng (clip)
for col in ['DiemToan', 'DiemVan', 'DiemAnh']:
    df[col] = df[col].clip(0, 10)

# 4. Tính TongDiem
df['TongDiem'] = df['DiemToan'] + df['DiemVan'] + df['DiemAnh']

# 5. Phân nhóm theo qcut (4 nhóm bằng nhau)
df['MucDiem'] = pd.qcut(df['TongDiem'], q=4, labels=['Yếu', 'Trung bình', 'Khá', 'Giỏi'])

# 6. Xuất file
df.to_csv('tuyensinh_cleaned.csv', index=False, encoding='utf-8-sig')

# Thống kê theo khu vực
thongke = df.groupby('KhuVuc').agg({
    'TongDiem': ['mean', 'max', 'min', 'count']
}).round(2)
thongke.to_csv('thongke_tuyensinh_theo_khuvuc.csv', encoding='utf-8-sig')

print("Đã xử lý xong! File sạch và file thống kê đã được xuất.")
print(df.head())