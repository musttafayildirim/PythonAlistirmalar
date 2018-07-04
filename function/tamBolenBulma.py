"""Bu çalışmamda sizlere tam bolen nasıl bulunur onu göstermeye  çalıştım

kendinize iyi bakın iyi günler diliyorum.. :D

"""


def tamBolenBul(sayi):

    tamBolenler = []

    for i in range(1, sayi+1):

        if (sayi % i == 0 ):      #burada ki if bloğumuz sayesinde for döngüsü içinde
            tamBolenler.append(i)  #tüm sayıları kontrol ediyoruz ve eğer sayımız kendisine gelene kadar
    return tamBolenler              #başka bir sayıya bölünürse onu tamBolenler listemize ekliyoruz..

while True:

    sayi = input("Sayı: ")

    if (sayi == "ç" or sayi == "Ç"):
        print("Program sonlandırıldı.............")
        break

    else:
        sayi = int(sayi)
        print("Tam bölenmelerimiz: ", tamBolenBul(sayi))
