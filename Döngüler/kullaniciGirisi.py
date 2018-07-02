"""Basit bir kullanıcı girişi uygulaması gerçekleştireceğiz"""

#bir tane kullanıcı girişi için kullanıcı adı ve parola belirliyoruz

sistemKullanıcıAdi = "Mustafa"
sistemParola = "123456"

#şimdi kullanıcı için giriş hakkı belirliyoruz

girisHakki = 3

while True:
    kullaniciAdi = input("Kullanıcı Adınızı Giriniz: ")
    parola = input("Parolanızı Giriniz: ")

    if(sistemKullanıcıAdi != kullaniciAdi and sistemParola == parola):
        girisHakki -= 1
        print("Kullanıcı Adınız Yanlış\nKalan Giriş Hakkınız", girisHakki)
    elif (sistemKullanıcıAdi == kullaniciAdi and sistemParola != parola):
        girisHakki -= 1
        print("Parolanız Yanlış\nKalan Giriş Hakkınız", girisHakki)
    elif (sistemKullanıcıAdi != kullaniciAdi and sistemParola != parola):
        girisHakki -= 1
        print("Kullanıcı Adınız ve Parolanız Yanlış\nKalan Giriş Hakkınız", girisHakki)
    else:
        print("Hosgeldiniz {}".format(kullaniciAdi))
        break
    if(girisHakki==0):
        print("Programı tekrar çalıştırıp deneyiniz.")
        break