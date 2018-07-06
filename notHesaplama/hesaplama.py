def notHesaplama(satır):
    satır = satır[:-1]
    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    nothesabi = not1 * 0.4 + not2 * 0.6

    if(nothesabi >= 90):
        harf = "AA"
    elif(nothesabi >= 80):
        harf = "AB"
    elif (nothesabi >= 70):
        harf = "BA"
    elif (nothesabi >= 65):
        harf = "CB"
    elif (nothesabi >= 60):
        harf = "CC"
    elif (nothesabi >= 55):
        harf = "DC"
    elif (nothesabi >= 45):
        harf = "DD"
    else:
        harf = "FF"

    return isim + "-------------------->" + harf + "\n"


with open("hesaplanacaklar.txt","r",encoding="utf-8") as file:
    ekleneceklerListesi = []
    for i in file:
        ekleneceklerListesi.append(notHesaplama(i))

    with open("hesabiyapilanlar.txt", "w" ,encoding="utf-8") as file2:

        for i in ekleneceklerListesi:
            file2.write(i)
        file2.write("--------------Hesaplananlar sonu------------------\n")