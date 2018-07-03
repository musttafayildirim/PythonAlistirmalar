"""Şimdi while döngüsü kullanarak kullanıcı adı ve parola ile giriş yaparak
ATM'den para çekme, güncelleme ve mevcut durumu gösteren bir basit uygulama gerçekleştireceğiz
"""



#öncelikle bakiye belirliyoruz.
#kullanıcı adı belirliyoruz
#ve şifre belirliyoruz..

MusteriHesapNumarası = "1"
MusteriParola = "1"
MevcutBakiye = 1000
girisHakki = 3
print("******************************************************************\n"
      "**                                                              **\n"
      "**    Merhaba Mustafa Bank'a Hoş Geldiniz                       **\n"
      "**    Para Çekmek İçin 1'e Basınız                              **\n"
      "**    Mevcut bakiyenizi görmek için 0'a basınız.                **\n"
      "**    Para yatırmak için 2'ye basınız.                          **\n"
      "**    Uygulamadan çıkmak için ç'ye basınız..                    **\n"
      "**                                                              **\n"
      "**                                                              **\n"
      "******************************************************************\n"
      )
while True:
    kullaniciHesapNumarasi = input("Hesap Numaranızı Giriniz: ")
    parola = input("Parolanızı Giriniz: ")
    if (MusteriHesapNumarası != kullaniciHesapNumarasi and parola != MusteriParola):
        print("Hatalı Hesap Numarası ve Parola")
        girisHakki -= 1
        print("Kalan Giris Hakkı", girisHakki)
    elif (MusteriHesapNumarası != kullaniciHesapNumarasi and parola == MusteriParola):
        print("Hatalı Hesap Numarası")
        girisHakki -= 1
        print("Kalan Giris Hakkı", girisHakki)
    elif (MusteriHesapNumarası == kullaniciHesapNumarasi and parola != MusteriParola):
        print("Hatalı parola")
        girisHakki -= 1
        print("Kalan Giris Hakkı", girisHakki)
    elif(MusteriHesapNumarası == kullaniciHesapNumarasi and parola == MusteriParola):
        while True:
                islem = input("Yapmak istediğiniz işlemi seçiniz..")
                if(islem == "0"):
                    print("Mevcut bakiyeniz: ", MevcutBakiye)
                elif(islem == "1"):
                    cekilecekTutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
                    if(cekilecekTutar - MevcutBakiye > 0):
                        print("Yetersiz Bakiye")
                        continue
                    MevcutBakiye -= cekilecekTutar
                    print("Kalan Tutarınız: ", MevcutBakiye)
                    print("Paranızı sağ köşeden alınız.")
                elif(islem == "2"):
                    yatirilanPara = int(input("Yatırmak istediğiniz parayı yazınız: "))
                    print("Lütfen paranızı para çekme bölmesine yerleştiriniz.")
                    MevcutBakiye +=yatirilanPara
                    print("Güncel bakiyeniz: ", MevcutBakiye)
                elif(islem == "ç" or islem == "Ç"):
                    print("Kartınızı almayı unutmayınız..")
                    break
                else:
                    print("Hatalı bir tuşa bastınız....")
    if (girisHakki == 0):
        print("Programı tekrar çalıştırıp deneyiniz.")
        break