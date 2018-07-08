from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL,"")  #burası sayesinde türkçe olarak yazıyoruz...
suAn = datetime.now() #dediğimiz zaman datetime.now() fonksiyonunu bir tane değişkene atamış olduk..

print(datetime.strftime(suAn,"%Y"))  #yılı verir.

print(datetime.strftime(suAn,"%B"))  #ayı verir

print(datetime.strftime(suAn,"%A"))  #günü verir

print(datetime.strftime(suAn,"%X"))  #saati verir

print(datetime.strftime(suAn,"%D"))   #tarihi verir mesela 07/08/18 şeklinde



print(datetime.ctime(suAn))  #şeklinde kullanırsak Sun Jul 8 13:07:38 2018 şeklinde bir kullanılım sağlar



print(datetime.strftime(suAn,"%A %B %Y")) #gün ay yıl şeklinde gösterir.



saniye = datetime.timestamp(suAn)
print(saniye)

#timestamp içerisine verilen zamanı saniyeye çeviriyor...


suAn2 = datetime.fromtimestamp(saniye)
print(suAn2)
#fromtimestamp fonksiyonu içerisine verilen saniyeyi normal zamana çeviriyor..



suAn = datetime.fromtimestamp(0)
print(suAn)

#saniyeyi 0 verirsek bizi 1970'e getirecektir....


print("Burada yaş hesabı yapılmıştır...")
tarih = datetime(1997,5,12)
suAn = datetime.now()

sonuc = suAn - tarih

print(sonuc.days/365)




