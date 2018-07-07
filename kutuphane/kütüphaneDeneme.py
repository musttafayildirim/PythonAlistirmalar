from kutuphane import *

print("""
*************************************************************
            Kütüphane Programına Hoş Geldiniz
            
İşlemler: 

1. Kitapları Göster
2. Kitapları Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt

Çıkmak için Ç ye basınız...
***************************************************************
""")

kütüphane = kutuphane()


while True:
    islem = input("Ne yapmak istiyorsunuz..")

    if(islem == 'ç' or islem == 'Ç'):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandırıldı....")
        break

    elif(islem == "1"):
        kütüphane.kitaplarıGoster()

    elif (islem == "2"):
        isim = input("Kitap ismi: ")

        print("Kitap Sorgulanıyor..")
        time.sleep(1)
        print("Kitap Bulundu....")

        kütüphane.kitapSorgula(isim)


    elif (islem == "3"):
        isim = input("isim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yanınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))

        yeniKitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap ekleniyor...")

        kütüphane.kitapEkle(yeniKitap)

        print("Kitap eklendi...")


    elif (islem == "4"):
        isim = input("Hangi kitabı silelim...")
        cevap = input("Emin misiniz? E/H")
        if(cevap == "E" or cevap == "e"):
            print("Kitap siliniyor..")
            time.sleep(1)
            kütüphane.kitapSil(isim)
        elif(cevap == "H" or cevap == "h"):
          print("Kitap Silinmedi")
        else:
            print("Hatalı giriş")
            break

    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz???")
        print("Baskı yükseltiliyor...")
        time.sleep(1)
        kütüphane.baskıYükselt(isim)
        print("Baskı yükseltildi..")
    else:
        print("Hatalı tuşlama yapıldı...")