a1,b1,c1,a2,b2,a3 = map(float, input().split(' '))
tb = (a1 + b1 + c1 + (a2 + b2)*2 + a3) / 10
print("Điểm trung bình là:", round(tb,1))