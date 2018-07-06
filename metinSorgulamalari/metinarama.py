class dosya():

    def __init__(self):

        with open("aranacakmetin.txt", "r", encoding="utf-8") as file:

            dosyaIcerigi = file.read()

            kelimeler = dosyaIcerigi.split()

            self.sadeKelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip("\'")
                i = i.strip("\"")
                i = i.strip("?")
                i = i.strip(";")
                i = i.strip(":")
                i = i.strip("(")
                i = i.strip(")")


                self.sadeKelimeler.append(i)

    def kelimeFrekansi(self):

        kelimeSozluk = dict()

        for i in self.sadeKelimeler:

            if(i in kelimeSozluk):
                kelimeSozluk[i] += 1
            else:
                kelimeSozluk[i] = 1
        for kelime,sayı in kelimeSozluk.items():
            print("{} kelimesi {} defa geçiyor...".format(kelime, sayı))

            print("--------------------------------------------")

dosya = dosya()

dosya.kelimeFrekansi()









