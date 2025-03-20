SoGiolam = float(input("Nhập số giờ làm: "))
LuongGio = float(input("Nhập lương theo giờ: "))
GioTieuChuan = 44
GioVuotChuan = max(0, SoGiolam - GioTieuChuan)
ThucLinh = GioTieuChuan * LuongGio + GioVuotChuan * LuongGio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {ThucLinh}")