import pickle
import os

FILE_NAME = "data.pkl"
menu = {}

DS_LOAI = ["Khai vị", "Món chính", "Tráng miệng", "Đồ uống"]

def load_data():
    global menu
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "rb") as f:
                menu = pickle.load(f)
        except: menu = {}
    else: menu = {}

def save_data():
    with open(FILE_NAME, "wb") as f:
        pickle.dump(menu, f)
    print("Đã lưu dữ liệu thành công!")

def chon_mon_theo_so():
    if not menu:
        print("Menu trống!")
        return None
    
    keys = list(menu.keys())
    print("\n--- DANH SÁCH MÓN ---")
    for i, ten in enumerate(keys, 1):
        print(f"{i}. {ten}")
    
    try:
        idx = int(input("Nhập số thứ tự món: ")) - 1
        if 0 <= idx < len(keys):
            return keys[idx]
        else:
            print("Số không hợp lệ!")
            return None
    except ValueError:
        print("Phải nhập số!")
        return None

def them_mon():
    print("\n--thêm món mới ---")
    ten = input("Nhập tên món: ")
    try:
        gia = float(input("Nhập giá: "))
    except:
        print(">> Giá phải là số!"); return

    print("Chọn loại:")
    for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
    try:
        chon_l = int(input(">> Nhập số loại: ")) - 1
        loai = DS_LOAI[chon_l] if 0 <= chon_l < 4 else "Khác"
    except: loai = "Khác"

    nl = input("Nhập nguyên liệu (cách nhau dấu phẩy): ").split(",")
    
    menu[ten] = {    
        "gia": gia, "loai": loai, 
        "nguyen_lieu": [x.strip() for x in nl],
        "trang_thai": "Còn hàng"
    }
    print("Đã thêm xong!")

def xem_menu():
    print("\n---xem menu ---")
    if not menu: print("Menu trống."); return
    
    for i, (ten, v) in enumerate(menu.items(), 1):
        print(f"{i}. Tên món: {ten}")
        print(f"   Giá: {v['gia']:,.0f}đ")
        print(f"   Loại: {v['loai']}")
        print(f"   Trạng thái: {v['trang_thai']}")
        print(f"   Nguyên liệu: {', '.join(v['nguyen_lieu'])}")
        print("-" * 30)

def cap_nhat_mon():
    print("\n---cập nhật món ---")
    ten = chon_mon_theo_so()
    if not ten: return

    print("Bạn muốn sửa gì?")
    print("1. Giá | 2. Loại | 3. Nguyên liệu")
    chon = input("Chọn (1-3): ")

    if chon == '1':
        menu[ten]['gia'] = float(input("Nhập giá mới: "))
    elif chon == '2':
        for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
        c = int(input("Chọn loại mới: ")) - 1
        menu[ten]['loai'] = DS_LOAI[c]
    elif chon == '3':
        nl = input("Nhập nguyên liệu mới (cách dấu phẩy): ").split(",")
        menu[ten]['nguyen_lieu'] = [x.strip() for x in nl]
    
    print("Cập nhật thành công!")

def xoa_mon():
    print("\n--- XÓA MÓN ---")
    ten = chon_mon_theo_so()
    if ten:
        del menu[ten]
        print("Đã xóa món này!")

def loc_theo_loai():
    print("\n--- LỌC MÓN ---")
    for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
    try:
        c = int(input("Muốn xem loại nào (nhập số): ")) - 1
        can_tim = DS_LOAI[c]
        found = False
        for ten, v in menu.items():
            if v['loai'] == can_tim:
                print(f"- {ten}: {v['gia']:,.0f}đ ({v['trang_thai']})")
                found = True
        if not found: print("Không có món nào thuộc loại này.")
    except: print("Nhập sai số!")

def tim_nguyen_lieu():
    tk = input("\nNhập tên nguyên liệu cần tìm: ").lower()
    found = False
    for ten, v in menu.items():
        ds_nl_thuong = [x.lower() for x in v['nguyen_lieu']]
        if tk in ds_nl_thuong:
            print(f"- {ten} (có chứa {tk})")
            found = True
    if not found: print("Không tìm thấy.")

def doi_trang_thai():
    print("\n--- ĐỔI TRẠNG THÁI ---")
    ten = chon_mon_theo_so()
    if ten:
        print(f"Món: {ten} (Hiện tại: {menu[ten]['trang_thai']})")
        print("1. Còn hàng | 2. Hết hàng")
        c = input("Chọn trạng thái mới (1/2): ")
        if c == '1': menu[ten]['trang_thai'] = "Còn hàng"
        elif c == '2': menu[ten]['trang_thai'] = "Hết hàng"
        print("Đã đổi trạng thái!")

load_data()

while True:
    print("\n=== QUẢN LÝ QUÁN ĂN ===")
    print("1. Thêm món")
    print("2. Xem menu")
    print("3. Cập nhật món (Giá/Loại/Nguyên liệu)")
    print("4. Xóa món")
    print("5. Lọc theo loại")
    print("6. Tìm theo nguyên liệu")
    print("7. Đổi trạng thái (Còn/Hết)")
    print("8. Lưu & Thoát")
    
    chon = input("Mời chọn chức năng (1-8): ")
    
    if chon == '1': them_mon()
    elif chon == '2': xem_menu()
    elif chon == '3': cap_nhat_mon()
    elif chon == '4': xoa_mon()
    elif chon == '5': loc_theo_loai()
    elif chon == '6': tim_nguyen_lieu()
    elif chon == '7': doi_trang_thai()
    elif chon == '8': save_data(); break
    else: print("Chọn sai, vui lòng nhập lại!")