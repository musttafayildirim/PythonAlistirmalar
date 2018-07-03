print("************************************\n"
      "*****                            ***\n"
      "*****                            ***\n"
      "*****                            ***\n"
      "*****        Faktoriyel Hesabı   ***\n"
      "****         Mustafa YILDIRIM    ***\n"
      "****                             ***\n"
      "****                             ***\n"
      "****                             ***\n"
      "************************************\n")

print("Programdan çıkmak için Ç'ye basınız.")
while True:
    islem = input("Faktoriyel hesaplaması yapmak istiyor musunuz? E/H")
    if(islem == "E" or islem == "e"):
        sayi = int(input("Sayıyı Giriniz: "))
        if(sayi == 0):
            print("Faktoriyel: 1")
            continue
        elif(sayi > 0):
            print("Faktoriyel Hesaplanıyor....")
            faktoriyel = 1

            for i in range(1,sayi+1):
                faktoriyel *= i
            print("Faktoriyel: ", faktoriyel)

        else:
            print("Lütfen pozitif sayı giriniz....!!!!")

    elif(islem == "H" or islem == "h"):
        print("Çıkış yapılıyor..")
        break

    else:
        print("Hatalı giriş yaptınız")