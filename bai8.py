ten_chu_ho = input("Nhập họ tên chủ hộ: ")
chi_so_dien_thang_tr_str = input("Nhập chỉ số điện tháng trước: ")
chi_so_dien_thang_tr = int(chi_so_dien_thang_tr_str)
chi_so_dien_thang_nay_str = input("Nhập chỉ số điện tháng này: ")
chi_so_dien_thang_nay = int(chi_so_dien_thang_nay_str)
kwh_tieu_thu = chi_so_dien_thang_nay - chi_so_dien_thang_tr
tong_tien_truoc_vat = 0
if kwh_tieu_thu <= 50:
    tong_tien_truoc_vat = kwh_tieu_thu * 1984
elif kwh_tieu_thu <= 100:
    tong_tien_truoc_vat += 50 * 1984
    tong_tien_truoc_vat += (kwh_tieu_thu - 50) * 2050
elif kwh_tieu_thu <= 200:
    tong_tien_truoc_vat += 50 * 1984 + 50*2050
    tong_tien_truoc_vat += (kwh_tieu_thu - 100) * 2380
elif kwh_tieu_thu <= 300:
    tong_tien_truoc_vat += 50*1984 + 50*2050 + 100*2380
    tong_tien_truoc_vat += (kwh_tieu_thu-200) *2998
elif kwh_tieu_thu <=400:
    tong_tien_truoc_vat += 50*1984 + 50*2050 + 100*2380 + 100*2998
    tong_tien_truoc_vat += (kwh_tieu_thu - 300) *3450
else:
    tong_tien_truoc_vat += 50*1984 + 50*2050 + 100*2380 + 100*2998 + 100*3460
    tong_tien_truoc_vat += (kwh_tieu_thu - 400) * 3460 
tong_tien_phai_tra = round(tong_tien_truoc_vat*1.08)
print(f"Họ tên chủ hộ: {ten_chu_ho}")
print(f"Chỉ số điện tháng trước: {chi_so_dien_thang_tr}")
print(f"Chỉ số điện tháng này: {chi_so_dien_thang_nay}")
print(f"Số kWh tiêu thụ: {kwh_tieu_thu}")
print(f"Tổng tiền phải trả (đã bao gồm VAT): {tong_tien_phai_tra}.")