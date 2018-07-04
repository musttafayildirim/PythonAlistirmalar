import kutuphane

kumanda = kutuphane.kumanda()


print("""
1. Tv açma
2. Tv Kapatma
3. Ses ayarları
4. Kanal Ekleme
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri
""")


while True:
    islem = input("İşlem Seçiniz:")

    if(islem == "1"):
        kumanda.tvAc()
    elif(islem == "2"):
        kumanda.tvKapat()
    elif(islem == "Ç" or islem == "ç"):
        print("Program Kapatılıyor...")
        break
    elif(islem == "3"):
        kumanda.sesAyarı()
    elif(islem == "4"):
        kanalIsimleri = input("Kanal isimlerini arada ',' kullanarak ayırınız giriniz: ")

        kanalListesi = kanalIsimleri.split(",")

        for eklenecekKanallar in kanalListesi:
            kumanda.kanalEkle(eklenecekKanallar)

    elif(islem == "5"):
        print("Kanal Sayısı: ",len(kumanda))
    elif(islem == "6"):
        kumanda.rastgeleKanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Hatalı Parametre")

