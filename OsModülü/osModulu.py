import os
from datetime import datetime
print(dir(os))  #os modulüyle neler yapabileceğimizi gösterir...


print(os.getcwd())  #bulunduğumuz dizini gösterir...


print(os.listdir())


for i in os.listdir():  #daha efektif bir şekilde bulunduğumuz dizinde bulunan her şeyi listeler...
    print(i)


# os.mkdir("deneme") #şeklinde kullanırsak deneme adında klasör oluşturur..

#os.makedirs("deneme1/deneme2") #iç içe klasör oluşturmayı sağlıyor..


#os.rmdir("deneme1/deneme2")  #deneme1'in altındaki deneme2 klasörünü silmemizi sağlıyor....


#os.removedirs("deneme1/deneme2") #tüm alt dizinleri silmemizi sağlıyorrr....

#OsModülü klasörünün altında bir tane deneme.txt dosyası oluşturuyorum daha sonra bu dosyanın adını komutla değiştiricezz..

#os.rename("deneme.txt", "deneme1.txt")

print(os.stat("deneme1.txt")) #deneme1.txt dosyasının bütün özelliklerini bize verir...

print(os.stat("deneme1.txt").st_mtime) #dosyanın değiştirilme zamanını veriyor..

#ancak bu gösterimden çok fazla bir şey anlamadığımız için aynı işlemi birde datetime'ı import edip deneyelim...


print(datetime.fromtimestamp(os.stat("deneme1.txt").st_mtime)) # şeklinde yaparsak daha güzel bir görüntü elde edebiliriz..

print(os.walk("/home/mustafa/PycharmProjects/PythonAlistirmalar/OsModülü"))  #bu objenin generator bir şeklinde yazılmış bir fonksiyon

#şimdi bu fonksiyon üzerinde gezinelim


for i in os.walk("/home/mustafa/PycharmProjects/PythonAlistirmalar"): #bu dizin içerisinde olan her şeyi listeledi..
    print(i)


for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("/home/mustafa/PycharmProjects/PythonAlistirmalar"): #bu daha güzel bir gösterim..
    print("Klasor Yolu: ",klasorYolu)
    print("Klasor İsmi: ",klasorIsimleri)
    print("Dosya İsmi: ",dosyaIsimleri)
    print("***************************************************")


#eğer sadece klasör isimlerini görmek istersek
print("\n\nBurada bu dizindeki sadece klasör isimleri gösterilmiştir....")
for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("/home/mustafa/PycharmProjects/PythonAlistirmalar"): #bu daha güzel bir gösterim..
    for i in klasorIsimleri:
        print(i)

print("\n\nBurada da sadece .py dosyaları gösterilmiştir....")
#eğer dosyalardan sadece .py olanları göstermek istersek....
for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("/home/mustafa/PycharmProjects/PythonAlistirmalar"): #bu daha güzel bir gösterim..
    for i in dosyaIsimleri:
        if(i.endswith(".py")):
            print(i)





