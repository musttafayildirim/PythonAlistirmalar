import time

def zamanHesaplama(func):
    def wrapper(sayilar):
        basla = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__ + " " + str(bitis - basla) +"saniye sürdü")
        return sonuc
    return wrapper

@zamanHesaplama
def kareleriHesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc

@zamanHesaplama
def kupleriHesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 3)

    return sonuc

kareleriHesapla(range(100000))
kupleriHesapla(range(100000))

