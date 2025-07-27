import os

def rename_inmage(path,name):
    os.chdir(path)
    os.getcwd()
    j=1
    if  os.listdir():
        for i in os.listdir():
            if i.lower().endswith(".jpg"):
                new_name=f"{name}{j}.jpg"
                os.rename(i,new_name)
                j+=1


def don_tmdlog(path):

    try:
        # Lấy danh sách các mục trong thư mục
        path_list = os.listdir(path)
    except Exception as e:
        print(f"Không truy cập được thư mục: {path}")
        return

    for item in path_list:
        full_path = os.path.join(path, item)
        # Đệ quy nếu là thư mục
        if os.path.isdir(full_path):
            don_tmdlog(full_path)
        else:
            try:
                if full_path.lower().endswith(".tmd") or full_path.lower().endswith(".log"):
                    os.remove(full_path)
                    print(f"Đã xóa file: {full_path}")
            except Exception as e:
                print(f"Không thể xóa file: {full_path} - {e}")

    # Sau khi duyệt xong, nếu thư mục rỗng thì xóa
    try:
        if not os.listdir(path):
            os.rmdir(path)
            print(f"Đã xóa thư mục rỗng: {path}")
    except Exception as e:
        print(f"Không thể xóa thư mục: {path} - {e}")
