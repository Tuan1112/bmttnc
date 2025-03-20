def daochuoi(chuoi):
    return chuoi[:: -1]
input_str = input("Nhap chuoi: ")
print("Ket qua: ", daochuoi(input_str))