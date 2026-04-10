import pandas as pd

df = pd.read_csv('muonsach.csv')

# 1. Chuyển sang kiểu datetime
df['NgayMuon'] = pd.to_datetime(df['NgayMuon'], errors='coerce')
df['NgayTra'] = pd.to_datetime(df['NgayTra'], errors='coerce')

# 2. Giữ nguyên bản ghi chưa trả (NgayTra thiếu)

# 3. Chuẩn hóa TrangThai
df['TrangThai'] = df['TrangThai'].str.strip().str.title()
df['TrangThai'] = df['TrangThai'].replace({
    'Datra': 'DaTra', 'Da tra': 'DaTra',
    'Chuatra': 'ChuaTra', 'Chua tra': 'ChuaTra'
}).fillna('ChuaTra')

# 4. Thêm cột SoNgayMuon
df['SoNgayMuon'] = (df['NgayTra'] - df['NgayMuon']).dt.days
# Với trường hợp chưa trả, có thể để NaN hoặc tính đến hôm nay (tùy yêu cầu)

# 5. Liệt kê sinh viên mượn quá 30 ngày
qua_han = df[(df['SoNgayMuon'] > 30) | (df['TrangThai'] == 'ChuaTra')]
print("Sinh viên mượn quá 30 ngày hoặc chưa trả:")
print(qua_han[['MaSV', 'TenSach', 'SoNgayMuon', 'TrangThai']])