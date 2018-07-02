"""Şimdi while döngüsü kullanarak kullanıcı adı ve parola ile giriş yaparak
ATM'den para çekme, güncelleme ve mevcut durumu gösteren bir basit uygulama gerçekleştireceğiz
"""



#öncelikle bakiye belirliyoruz.
#kullanıcı adı belirliyoruz
#ve şifre belirliyoruz..

MusteriHesapNumarası = "1"
MusteriParola = "1"
MevcutBakiye = 1000
while True:
    print("******************************************************************\n"
          "**                                                              **\n"
          "**    Merhaba Mustafa Bank'a Hoş Geldiniz                       **\n"
          "**    Para Çekmek İçin 1'e Basınız                              **\n"
          "**    Mevcut bakiyenizi görmek için 0'a basınız.                **\n"
          "**    Para yatırmak için 2'ye basınız.                          **\n"
          "**    Uygulamadan çıkmak için ç'ye basınız..                    **\n"
          "**    Uygulamaya devam etmek için herhangi bir tuşa basınız     **\n"
          "**                                                              **\n"
          "******************************************************************\n"
          )
    if(input() == "ç"):
        print("Çıkış yapılıyor....")
        break
    else:
        kullaniciHesapNumarasi = input("Hesap Numaranızı Giriniz: ")
        parola = input("Parolanızı Giriniz: ")
        if(MusteriHesapNumarası == kullaniciHesapNumarasi and MusteriParola == MusteriParola):
            print("Giris Yapıldı..\n")
            islem = input("Yapmak istediğiniz işlemi seçiniz..")
            if(islem == "0"):
                print("Mevcut bakiyeniz: ",MevcutBakiye)
            elif(islem == "1"):
                cekilecekTutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
                if(cekilecekTutar - MevcutBakiye > 0):
                    print("Yetersiz Bakiye")
                    continue
                MevcutBakiye -= cekilecekTutar
                print("Kalan Tutarınız: ", MevcutBakiye)
            elif(islem == "2"):
                yatirilanPara = int(input("Yatırmak istediğiniz parayı yazınız: "))
                MevcutBakiye +=yatirilanPara
                print("Güncel bakiyeniz: ", MevcutBakiye)
