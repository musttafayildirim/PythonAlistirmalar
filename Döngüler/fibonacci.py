print("Fibonacci Hesaplama Programımız\n")
a = 1
b = 1

fibonacci = [a,b]

sayi = int(input("Kaçıncı sayıya kadar fibonacci serisini devam ettirmek istiyorsun?  "))
for i in range(sayi-2):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)
