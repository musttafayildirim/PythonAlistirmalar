import sqlite3
import time


class Kitap():

    def __init__(self, isim, yazar, yayınevi, tür, baskı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı


    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}".format(self.isim, self.yazar, self.yayınevi, self.tür, self.baskı)


class kutuphane():

    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):

        self.baglanti = sqlite3.connect("kutuphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create table if not exists kitaplar(isim TEXT, yazar TEXT, yayınevi TEXT, tür TEXT, baskı int)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()



    def baglantiyiKes(self):

        self.baglanti.close()

    def kitaplarıGoster(self):

        sorgu = "select * from kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor....")
        else:
            for i in kitaplar:

                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print("**************")
                print(kitap)


    def kitapSorgula(self, isim):

        sorgu = "Select * from kitaplar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor..")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitapEkle(self,Kitap):

        sorgu = "insert into kitaplar values (?,?,?,?,?)"

        self.cursor.execute(sorgu, (Kitap.isim, Kitap.yazar, Kitap.yayınevi, Kitap.tür, Kitap.baskı))

        self.baglanti.commit()

    def kitapSil(self,isim):

        sorgu = "delete from kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baskıYükselt(self, isim):

        sorgu = "select * from kitaplar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor....")
        else:
            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2, (baskı, isim))

            self.baglanti.commit()
