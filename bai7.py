nhap_chuoi=input("nhập chuỗi bất kỳ có trên 20 ký tự: ")
if len(nhap_chuoi) >= 20:
    ky_tu_thu_5=nhap_chuoi[4]
    ky_tu_thu_9=nhap_chuoi[8]
    print(f"Ký tự thứ 5 là: {ky_tu_thu_5}")
    print(f"Ký tự thứ 9 là: {ky_tu_thu_9}")
else:
    print("Lỗi!!!!!!!!!: Chuỗi không đủ (>= 20) ký tự.")