import pandas as pd

df = pd.read_csv('nhansu.csv')

# 1. Chuẩn hóa GioiTinh (giả sử có nhiều dạng: nam, Nam, nữ, Nu, ...)
df['GioiTinh'] = df['GioiTinh'].str.strip().str.title()
df['GioiTinh'] = df['GioiTinh'].replace({'Nam': 'Nam', 'Nữ': 'Nữ', 'Nu': 'Nữ', 'Male': 'Nam', 'Female': 'Nữ'})

# 2. Chuẩn hóa PhongBan (viết hoa chữ cái đầu)
df['PhongBan'] = df['PhongBan'].str.strip().str.title()

# 3. Xóa khoảng trắng thừa trong HoTen
df['HoTen'] = df['HoTen'].str.strip()

# 4. Đổi tên cột
df = df.rename(columns={
    'MaNV': 'ma_nv',
    'HoTen': 'ho_ten',
    'GioiTinh': 'gioi_tinh',
    'PhongBan': 'phong_ban',
    'Luong': 'luong'
})

print(df.head())
print(df['gioi_tinh'].value_counts())