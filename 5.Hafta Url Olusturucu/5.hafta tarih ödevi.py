def gecerli_tarih_mi(tarih_str):
    parcalar = tarih_str.split('.')
    if len(parcalar) != 3:
        return False
    yil, ay, gun = parcalar

    if not (yil.isdigit() and ay.isdigit() and gun.isdigit()):
        return False
    if len(yil) != 4:
        return False
    if len(ay) != 2:
        return False
    if len(gun) != 2:
        return False

    y = int(yil)
    a = int(ay)
    g = int(gun)

    if not (1 <= a <= 12):
        return False
    if not (1 <= g <= 31):
        return False
    return True


def tarih_gir(mesaj):
    while True:
        tarih_str = input(mesaj)
        if gecerli_tarih_mi(tarih_str):
            return tarih_str
        else:
            print("Hatalı format! Lütfen tarihi YYYY.AA.GG formatında giriniz.")


def coklu_girdi_al(mesaj):
    print(mesaj)
    girdiler = input()
    return [girdi.strip() for girdi in girdiler.split(',')]


baslangic_tarih = tarih_gir("Başlangıç tarihi: ")
bitis_tarih = tarih_gir("Bitiş tarihi: ")
kategoriler = coklu_girdi_al("Lütfen kategori giriniz:")
gazeteler = coklu_girdi_al("Lütfen gazete giriniz:")

baslangic_gun = int(baslangic_tarih.split('.')[-1])
bitis_gun = int(bitis_tarih.split('.')[-1])

baslangic_ay = int(baslangic_tarih.split('.')[1])
bitis_ay = int(bitis_tarih.split('.')[1])

baslangic_yil = int(baslangic_tarih.split('.')[0])
bitis_yil = int(bitis_tarih.split('.')[0])

# print("1.Tarih Günü:", baslangic_gun)
# print("2.Tarih Günü:", bitis_gun)
# print("1.Tarih Ayı:", baslangic_ay)
# print("2.Tarih Ayı:", bitis_ay)
# print("1.Tarih Yılı:", baslangic_yil)
# print("2.Tarih Yılı:", bitis_yil)
# print(baslangic_yil,baslangic_ay,baslangic_gun)
# print(bitis_yil,bitis_ay,bitis_gun)

if baslangic_yil == bitis_yil:
    if baslangic_ay == bitis_ay:
        if baslangic_gun == bitis_gun:
            print("Girilen tarihler aynıdır. Lütfen Farklı tarihler giriniz.")

print("\nGirilen Tarih Aralıkları:")

print("Aralık:", baslangic_tarih, "ile", bitis_tarih)

# for gazete in gazeteler:
#     print(gazete)
#     format ="www.{}.com.tr".format(gazete)
#     for kategori in kategoriler:
#         for i in range(int(baslangic_yil), int(bitis_yil)+1):
#          for j in range(int(baslangic_ay), int(bitis_ay)+1):
#           for k in range(int(baslangic_gun), int(bitis_gun)+1):
#               print("{}/{}/{}-{}-{}".format(format,kategori,k,j,i))
with open("h5url.txt", "w", encoding="utf-8") as f:
    for yil in range(baslangic_yil, bitis_yil + 1):
        if yil == baslangic_yil:
            ay_bas = baslangic_ay
        else:
            ay_bas = 1
        if yil == bitis_yil:
            ay_bit = bitis_ay
        else:
            ay_bit = 12
        for ay in range(ay_bas, ay_bit + 1):
            if yil == baslangic_yil and ay == baslangic_ay:
                gun_bas = baslangic_gun
            else:
                gun_bas = 1
            if yil == bitis_yil and ay == bitis_ay:
                gun_bit = bitis_gun
            else:
                gun_bit = 31
            for gun in range(gun_bas, gun_bit + 1):
                for gazete in gazeteler:
                    gazete_format = "www.{}.com.tr".format(gazete)
                    for kategori in kategoriler:
                        url = "http://{}/{}/{:04d}-{:02d}-{:02d}".format(gazete_format, kategori, yil, ay, gun)
                        print(url)
                        f.write(url + "\n")


