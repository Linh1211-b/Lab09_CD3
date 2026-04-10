import pandas as pd

df = pd.read_csv('donhang.csv')
print("Số dòng ban đầu:", len(df))

# 1. Kiểm tra trùng toàn bộ
print("Trùng toàn bộ:", df.duplicated().sum())

# 2. Kiểm tra trùng theo MaDon
print("Trùng theo MaDon:", df.duplicated(subset=['MaDon']).sum())

# 3. Xóa trùng, giữ bản ghi đầu tiên
df = df.drop_duplicates(subset=['MaDon'], keep='first')

# 4. Tạo cột ThanhTien
df['ThanhTien'] = df['SoLuong'] * df['DonGia']

# 5. Sắp xếp theo NgayDat tăng dần
df['NgayDat'] = pd.to_datetime(df['NgayDat'])  # chuyển sang datetime nếu cần
df = df.sort_values(by='NgayDat')

print("Dữ liệu sau khi xử lý:")
print(df.head())
print("Số dòng còn lại:", len(df))