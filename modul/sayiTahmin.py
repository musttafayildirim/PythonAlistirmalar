import random
import time


print("""
**************************************************************
Sayı tahmin oyunu

1 ile 100 arasında verilen sayıyı bilmeye çalışalım :D

Dikkat toplam hakkımız 10'dur (-_-)

**************************************************************

""")



rastgeleSayi = random.randint(1,100)

tahminHakki = 10
bilmesayısı = 0
while True:
    tahmin = int(input("Tahmininiz: "))


    if(tahmin > rastgeleSayi):
        print("Bilgiler kontrol ediliyor..")

        time.sleep(1)

        print("Daha küçük bir sayı söyleyiniz.")

        tahminHakki -= 1
        bilmesayısı +=1
    elif(tahmin < rastgeleSayi):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz...")
        tahminHakki -= 1
        bilmesayısı +=1

    else:
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        bilmesayısı += 1
        print("Tebrikler {}. seferde doğru bildiniz.".format(bilmesayısı))
        break
    if(tahminHakki == 0):
        print("Tahmin hakkınız bitmiştir..")
        break