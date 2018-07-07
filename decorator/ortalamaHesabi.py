def ekstra(fonk):
    def wrapper(sayilar):
        ciftlerToplami = 0
        ciftler = 0
        teklerToplami = 0
        tekler = 0

        for sayi in sayilar:
            if(sayi % 2 == 0 ):
                ciftler += 1
                ciftlerToplami += sayi
            else:
                tekler += 1
                teklerToplami += sayi
        print("Teklerin ortalamasi: ",(teklerToplami/tekler))
        print("Çiftlerin ortalamasi: ",(ciftlerToplami/ciftler))

        fonk(sayilar)
    return wrapper


@ekstra
def ortalamaBul(sayilar):
    toplam = 0

    for i in sayilar:
        toplam += i

    print("Genel ortalama = ",(toplam/len(sayilar)))


ortalamaBul([1,2,3,5,64,86,45])


