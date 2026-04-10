import pandas as pd
import os

print("=== BÀI NÂNG CAO 2: LÀM SẠCH DỮ LIỆU BÁN HÀNG TỪ NHIỀU FILE ===\n")

# Kiểm tra sự tồn tại của 3 file
files = ['banhang_thang1.csv', 'banhang_thang2.csv', 'banhang_thang3.csv']
missing_files = [f for f in files if not os.path.exists(f)]

if missing_files:
    print("❌ LỖI: Không tìm thấy các file sau:")
    for f in missing_files:
        print(f"   - {f}")
    print("\nVui lòng tạo đủ 3 file CSV và đặt cùng thư mục với Bai2nangcao.py")
    exit()

# Đọc và ghép dữ liệu
dfs = []
for f in files:
    try:
        temp = pd.read_csv(f)
        print(f"✓ Đọc thành công: {f} ({len(temp)} dòng)")

        # Chuẩn hóa tên cột (để tránh lỗi cột khác nhau)
        temp.columns = ['MaDon', 'MaKH', 'NgayDat', 'SanPham', 'SoLuong', 'DonGia']
        dfs.append(temp)
    except Exception as e:
        print(f"❌ Lỗi khi đọc file {f}: {e}")

df = pd.concat(dfs, ignore_index=True)
print(f"\nTổng số dòng sau khi ghép: {len(df)}")

# ==================== XỬ LÝ DỮ LIỆU ====================

# 3. Xử lý trùng mã đơn hàng (giữ bản ghi mới nhất theo ngày)
df['NgayDat'] = pd.to_datetime(df['NgayDat'], format='mixed', errors='coerce')
df = df.sort_values(by='NgayDat').drop_duplicates(subset='MaDon', keep='last')

# 4. Chuẩn hóa giá tiền (loại bỏ dấu phẩy, ký tự lạ)
df['DonGia'] = pd.to_numeric(
    df['DonGia'].astype(str).str.replace(r'[^\d.]', '', regex=True),
    errors='coerce'
)

df['ThanhTien'] = df['SoLuong'] * df['DonGia']

# 5. Tạo cột tháng
df['Thang'] = df['NgayDat'].dt.strftime('%Y-%m')

# ==================== BÁO CÁO ====================

print("\n=== BÁO CÁO DOANH THU ===")
doanh_thu_thang = df.groupby('Thang')['ThanhTien'].sum().round(0)
print(doanh_thu_thang)

print("\n=== TOP 5 SẢN PHẨM DOANH THU CAO NHẤT ===")
top5 = df.groupby('SanPham')['ThanhTien'].sum().nlargest(5).round(0)
print(top5)

print("\n=== SỐ ĐƠN HÀNG CÓ LỖI DỮ LIỆU ===")
loi = df[df.isnull().any(axis=1)]
print(f"Số đơn lỗi: {len(loi)}")
if len(loi) > 0:
    print(loi)

# Lưu file sạch
df.to_csv('banhang_cleaned.csv', index=False, encoding='utf-8-sig')
print("\n✅ Hoàn thành! File sạch đã được lưu: banhang_cleaned.csv")