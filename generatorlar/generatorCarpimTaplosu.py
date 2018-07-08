def carpimTablosu():
    for i in range(1,11):
        print("\n")
        for j in range(1,11):
            yield  "{} x {} = {}".format(i,j,i*j)

for i in carpimTablosu():
    print(i)



#yield anahtar kelimesini kullandığımız zaman veri bellekte yer
#işgal etmiyor biz ne zaman çağırırsak sadece o zaman kullanılıyor ve
#siliniyor.




