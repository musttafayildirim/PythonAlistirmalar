def toplama(a,b,c):
    print("toplamları: ", a+b+c)


toplama(5,3,5)


def faktoriyel(sayi):
    faktoriyel = 1
    deger = 0
    if(sayi == 0 or sayi == 1):
        return faktoriyel
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
            deger += 1
        print("Faktoriyel fonksiyonu çalıştı... {}! = {}".format(deger, faktoriyel))
        return faktoriyel


def toplama(a,b,c):
    print("Birinci Fonksiyon çalıştı ve sayıların toplamı: ",a+b+c)
    return a+b+c
def ikiylecarp(a):
    print("İkinci fonksiyon çalıştı ve sayıların toplamının iki ile çarpımı: ",a * 2)
    return a * 2

def ucebol(a):
    print("Üçüncü fonksiyon çalıştı ve sayıların üçe bölümü: ", a/3)
    return a / 3

print(ucebol(ikiylecarp(toplama(faktoriyel(10),faktoriyel(15),faktoriyel(5)))))


def toplamaa(*a):
    toplamaa = 0
    for i in a:
        toplamaa += i
    return toplamaa

print(toplamaa(56,44,58,1,555,4,654))








