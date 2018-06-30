"""Öncelikle iki bilinmeyenli bir denklemin köklerini bulabilmemiz için şunları bilmemiz gerekmektedir.
Deltamız sıfırdan büyük olursa iki reel kökümüz vardır.
Eğer delta < 0 olursa reel kökümüz yoktur.
Ve deltamız sıfıra eşit olursa çakışık iki kökümüz vardır. Buraya dikkat edelim yine iki kökümüz var ama bunlar
çakışık olduğu için bir tane reel sayı buluyoruz.
"""

print("İki Bilinmeyenli Denklem Köklerini Bulan Program")
print("Denklemimiz (ax**2+b*x+c ) şeklinde olmalıdır..")
a = int(input("A değerini giriniz:"))
b = int(input("B değerini giriniz:"))
c = int(input("C değeriniz giriniz:"))
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

if delta < 0:
    print("reel kök yoktur...")
if delta == 0:
    print("çakışık iki kök vardır...")
    print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1, x2))
if delta > 0:
    print("gerçek iki kök vardır...")
    print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1, x2))
