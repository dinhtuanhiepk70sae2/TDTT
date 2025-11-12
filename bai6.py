a=float(input("nhập độ dài cạnh a:"))
b=float(input("nhập độ dài cạnh b:"))
c=float(input("nhập độ dài cạnh c:"))
if a+b>c or b+c>a or a+c>b :
    C_nuachuvi=(a+b+c)/2
    s_tamgiac=(C_nuachuvi*(C_nuachuvi-a)*(C_nuachuvi-b)*(C_nuachuvi-c))**(0.5)
    print("diện tích tam giác tạo được là: ",s_tamgiac,"(m2)")
else :
    print("không thể tạo thành một tam giác")