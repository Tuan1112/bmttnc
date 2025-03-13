def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False
ChuoiNhiPhan = input("Moi nhap chuoi: ")
sonhiphanList = ChuoiNhiPhan.split(",")
SoChiaHetCho5 = [num for num in sonhiphanList if chiahetcho5(num)]
if len(SoChiaHetCho5) > 0:
    KQ = " , ".join(SoChiaHetCho5)
    print("Cac so nhi phan chia het cho 5: ", KQ)
else:
    print("khong co so nhi phan nao.")