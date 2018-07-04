# Asallık testi yapacağızzz

#burada fonksiyonumuzu tanımlıyoruz
def asalMi(sayi):
    if (sayi == 1 ):
        return False
    elif (sayi == 2 ):
        return True
    else:
        for i in range(2, sayi):
            if(sayi % i == 0):  #burada dongümüz boyunca verilen sayıya kadar kontrol yapılıyor
                return False    #eğer dongü içindeki bir sayıya bölünürse sayımızın değeri false dönüyor...
        return True


while True:
    sayı = input("Sayı: ")

    if(sayı == "ç" or sayı == "Ç"):
        break
    else:
        sayı = int(sayı)

        if(asalMi(sayı)):
            print(sayı, "Asal bir sayıdır....")
        else:
            print(sayı, "Asal bir sayı değildir...")