a=float(input("Nhập chiều rộng của mảnh đất hình chữ nhật(m): "))
b=float(input("Nhập chiều dài của mảnh đất hình chữ nhật(m): "))
r_kvchtron=a/2
S_cn=a*b
S_tron=3.14*r_kvchtron**2
s_trongcay=S_cn-S_tron
print("Diện tích trồng cây còn lại là:",round(s_trongcay,2),"m^2")