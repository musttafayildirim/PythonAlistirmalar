#burada oluşturacağımız class'ta 5'in kuvvetlerini alacağız
#bunu kendi yazdığımız itirasyon yöntemi ile yapacağız..


class Kuvvet5():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):

        return self
    def __next__(self):
        if(self.kuvvet <= self.max):
            sonuc = 5 ** self.kuvvet

            self.kuvvet += 1
            return sonuc

        else:
            self.kuvvet = 0   #bu satır bizim tekrardan for döngüsünde dönmemizi sağlıyor......
            raise StopIteration

kuvvet = Kuvvet5(6)



for i in kuvvet:
    print(i)

print("Aşağıdaki dönünün çalışması için else bloğunda self.kuvvet=0 yapılması gerekiyordu yaptık...")
for j in kuvvet:
    print(j)
