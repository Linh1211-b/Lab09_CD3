import pandas as pd

# Đọc file với kiểm tra lỗi
try:
    df = pd.read_csv('khaosat.csv')
    print("Đọc file thành công! Số dòng ban đầu:", len(df))
except FileNotFoundError:
    print("LỖI: Không tìm thấy file 'khaosat.csv'")
    print("Vui lòng đặt file khaosat.csv cùng thư mục với Bai7.py")
    exit()

# ====================== XỬ LÝ THEO YÊU CẦU ======================

# 1. Chuẩn hóa cột CoLamThem thành 1/0
mapping = {
    'Yes': 1, 'yes': 1, 'Y': 1, 'y': 1, 'Có': 1, 'có': 1,
    'No': 0,  'no': 0,  'N': 0, 'n': 0, 'Không': 0, 'không': 0
}
df['CoLamThem'] = df['CoLamThem'].astype(str).str.strip().map(mapping).fillna(0).astype(int)

# 2. Chuẩn hóa MucDoHaiLong về thang 1-5
df['MucDoHaiLong'] = pd.to_numeric(df['MucDoHaiLong'], errors='coerce')
df = df[(df['MucDoHaiLong'] >= 1) & (df['MucDoHaiLong'] <= 5)]

# 3. Đổi tên cột theo chuẩn
df = df.rename(columns={
    'MaSV': 'ma_sv',
    'GioHocMoiNgay': 'gio_hoc_moi_ngay',
    'MucDoHaiLong': 'muc_do_hai_long',
    'CoLamThem': 'co_lam_them'
})

# 4. Loại bỏ GioHocMoiNgay < 0
df = df[df['gio_hoc_moi_ngay'] >= 0]

# 5. Thống kê kết quả
print("\n=== KẾT QUẢ SAU KHI LÀM SẠCH ===")
print(df)

print("\nSố sinh viên làm thêm (1):", df['co_lam_them'].sum())
print("Số sinh viên không làm thêm (0):", (df['co_lam_them'] == 0).sum())
print("\nPhân bố mức độ hài lòng:")
print(df['muc_do_hai_long'].value_counts().sort_index())

# Lưu file sau khi làm sạch (tùy chọn)
df.to_csv('khaosat_cleaned.csv', index=False, encoding='utf-8-sig')
print("\nĐã lưu file cleaned: khaosat_cleaned.csv")