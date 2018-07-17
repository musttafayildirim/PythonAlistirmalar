file = open("bilgiler.txt", "w", encoding="utf-8")  # "a" kullanarak dosya açarsak açılan dosyanın üzerine yazmaya devam eder..
file.write("Mustafa Yıldırım\n")                      # "w" kullanarak dosyaları açarsak açılan dosyanın üzerine yazar..(o dosyayı siler tekrar dosya oluşturur....
file.write("Mikail YILDIRIM\n")
file.close()
files = open("bilgiler.txt", "r", encoding="utf-8")  #dosyanın içerisini okumak için kullanılır...
for i in files:
    print(i, end="")
files.close()



with open("bilgiler.txt","r", encoding="utf-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())
    icerik = file.read(15)
    file.seek(0)
    icerik2 = file.read(16)
    print(icerik)
    print(icerik2)


print("naber")


print("Burada r+ çalışmıştır")
with open("bilgiler.txt","r+", encoding="utf-8") as file:
    print(file.read())
