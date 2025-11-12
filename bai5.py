def process_char(char_hoa):
    if 'B' <= char_hoa <= 'Z':
        char_thuong = char_hoa.lower() 
        char_lien_truoc = chr(ord(char_thuong) - 1)
        return char_lien_truoc
    elif char_hoa == 'A':
        return "Trường hợp đặc biệt: Không có chữ cái thường liền trước 'a' trong bảng chữ cái (nếu chỉ xét bảng chữ cái tiếng Anh tiêu chuẩn không vòng lặp)."
    else: 
        return "Đầu vào không hợp lệ. Vui lòng nhập một chữ cái hoa từ A đến Z."
input_char = input("Nhập một chữ cái hoa (A-Z): ").upper() 
result = process_char(input_char)
print(f"Kết quả: (result)")