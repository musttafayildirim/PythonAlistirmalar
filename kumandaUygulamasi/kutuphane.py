import random
import time

class kumanda():

    def __init__(self, tvDurumu = "Kapalı", tvSes = 0, kanalListesi = ["TRT"], kanal = "TRT"):

        self.tvDurumu = tvDurumu
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal


    def tvAc(self):

        if(self.tvDurumu == "Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor..")
            self.tvDurumu = "Açık"


    def tvKapat(self):

        if(self.tvDurumu == "Kapalı"):
            print("Televizyon zaten Kapalı")
        else:
            print("Televizyon kapatılıyor")
            self.tvDurumu = "Kapalı"


    def sesAyarı(self):

        while True:
            giris = input("Sesi azaltmak için '-' ye basınız.\nSesi artırmak için '+' tuşuna basınız.\nÇıkış yapmak için 'Ç' tuşuna basınız.")

            if(giris == 'ç' or giris == 'Ç'):
                print("Çıkış yapılıyor..")
                print("Güncel sesimiz = ",self.tvSes)
                break
            elif(giris == "+"):
                if(self.tvSes != 60):
                    self.tvSes +=1
                    print("Ses artırıldı güncel ses {} ".format(self.tvSes))
            elif(giris == "-"):
                if(self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses azaltıldı güncel ses {} ".format(self.tvSes))
            else:
                print("Hatalı parametre girilmeye çalışıldı...")


    def kanalEkle(self, kanalIsmi):
        print("Kanal ekleniyor..")
        time.sleep(1)

        self.kanalListesi.append(kanalIsmi)

        print("Kanal Eklendi")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi)-1)

        self.kanal = self.kanalListesi[rastgele]

        print("Şu anki kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanalListesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}".format(self.tvDurumu, self.tvSes, self.kanalListesi, self.kanal)




