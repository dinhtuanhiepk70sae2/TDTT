c = input("Nhập một ký tự: ")
if c.isupper():
    print("Ký tự thường tương ứng là:", c.lower())
elif c.islower():
    print("Ký tự hoa tương ứng là:", c.upper())
else:
    print("Ký tự không phải là chữ cái")