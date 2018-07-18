from PIL import Image,ImageFilter

#resimleri açmamızı sağlıyorlar
image = Image.open("Kaplan.jpg")
image2 = Image.open("aslan.jpg")

#kaplan resmini farklı bir adla kaydetmemizi sağlayan komut satırı
image.save("kaplan2.jpg")

#resmimizin yönünü çevirmemizi sağlıyor..
image.rotate(155).save("kaplan3.jpg")

#aslan resmimizi siyah beyaz yapıyor...
image2.convert(mode="L").save("aslanSiyahBeyaz.jpg")


# kaplan resmine yeni boyut veriyoruz.....
degistir = (683, 360)
image.thumbnail(degistir)
image.save("kaplan4.jpg")

#kaplan resmini blurluyoruz...
image.filter(ImageFilter.GaussianBlur(10)).save("kaplan5.jpg")

#resmi kırpıyoruz...
kirpilacakAlan = (0,0, 400 ,300)
image.crop(kirpilacakAlan).save("kaplan6.jpg")