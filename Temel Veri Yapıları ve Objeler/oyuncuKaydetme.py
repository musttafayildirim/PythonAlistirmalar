print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adını Giriniz: ")
soyad = input("Oyuncunun Soyadını Giriniz: ")
takım = input("Oyuncunun Takımını Giriniz: ")

print("Oyuncu bilgileri kaydediliyor....")

bilgiler = (ad, soyad, takım)

print("Oyuncunun Adı {}\nSoyadı {}\nTakım Bilgisi {}\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Oyuncu Bilgileri Kaydedildi...")

