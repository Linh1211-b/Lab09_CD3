import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

print("=== BÀI NÂNG CAO 3: TIỀN XỬ LÝ DỮ LIỆU BỆNH NHÂN ===\n")

# ====================== ĐỌC DỮ LIỆU ======================
try:
    df = pd.read_csv('benhnhan.csv')
    print(f"Đọc thành công: {len(df)} bệnh nhân")
except FileNotFoundError:
    print("❌ LỖI: Không tìm thấy file 'benhnhan.csv'")
    print("Vui lòng tạo file benhnhan.csv và đặt cùng thư mục với Bai3nangcao.py")
    exit()

# ====================== XỬ LÝ DỮ LIỆU ======================

# 1. Chuẩn hóa cột phân loại
df['GioiTinh'] = df['GioiTinh'].astype(str).str.strip().str.title()
df['GioiTinh'] = df['GioiTinh'].replace({'Nam': 'Nam', 'Nữ': 'Nữ', 'Nu': 'Nữ'})

df['ChanDoan'] = df['ChanDoan'].astype(str).str.strip().str.title().replace({'nan': pd.NA})

# 2. Chuyển các cột số sang numeric
numeric_cols = ['Tuoi', 'HuyetApTamThu', 'HuyetApTamTruong', 'DuongHuyet']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Điền giá trị thiếu bằng median
for col in numeric_cols:
    if df[col].isna().sum() > 0:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
        print(f"Đã điền median cho {col}: {median_value:.2f}")

# 4. Xử lý outlier cho Tuổi
df['Tuoi'] = df['Tuoi'].clip(lower=1, upper=120)

# 5. Mã hóa ChanDoan
le = LabelEncoder()
df['ChanDoan_Code'] = le.fit_transform(df['ChanDoan'].fillna('Unknown'))

print("\nCác nhãn ChanDoan đã mã hóa:",
      dict(zip(le.classes_, range(len(le.classes_)))))

# 6. Chuẩn hóa (Scaling) các cột số
scaler = StandardScaler()
cols_to_scale = ['Tuoi', 'HuyetApTamThu', 'HuyetApTamTruong', 'DuongHuyet']

# Tạo cột mới có tiền tố 'scaled_'
scaled_values = scaler.fit_transform(df[cols_to_scale])
scaled_df = pd.DataFrame(scaled_values, columns=['scaled_' + c for c in cols_to_scale], index=df.index)

# Gộp lại vào DataFrame gốc
df = pd.concat([df, scaled_df], axis=1)

# ====================== KẾT QUẢ ======================
print("\n=== DỮ LIỆU SAU KHI XỬ LÝ (10 cột đầu) ===")
print(df[['MaBN', 'Tuoi', 'GioiTinh', 'HuyetApTamThu', 'HuyetApTamTruong',
          'DuongHuyet', 'ChanDoan', 'ChanDoan_Code',
          'scaled_Tuoi', 'scaled_HuyetApTamThu']].round(3))

print("\nSố giá trị thiếu còn lại:", df.isnull().sum().sum())

# ====================== LƯU FILE ======================
df.to_csv('benhnhan_preprocessed.csv', index=False, encoding='utf-8-sig')
print("\n✅ Hoàn thành! File đã được lưu: benhnhan_preprocessed.csv")
print("   File này đã sẵn sàng để đưa vào mô hình Machine Learning.")