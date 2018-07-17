import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT, yazar TEXT,yayınevi TEXT,sayfaSayisi INT)")
    con.commit()
def veriEkle():
    cursor.execute("insert into kitaplık values ('İstanbul Hatırası','Ahmet Ümit','Everest',568)")
    con.commit()

def veriEkle2():
    cursor.execute("insert into kitaplık values (?,?,?,?)",(isim,yazar,yayınevi,sayfaSayisi))
    con.commit()

def verileriAl():
    cursor.execute("select * from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def verileriAl2():
    cursor.execute("select isim,yayınevi from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosundaki Kitap isimleri ve Yayınevleri")
    for i in liste:
        print(i)

def verileriAl3(yayınevi):
    cursor.execute("select isim,yayınevi from kitaplık where yayınevi =  ?",(yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık tablosundaki Kitap isimleri ve Yayınevleri")
    for i in liste:
        print(i)


def verileriGuncelle(eskiYayınevi,yeniYayınevi):
    cursor.execute("update kitaplık set yayınevi = ? where yayınevi = ?",(yeniYayınevi,eskiYayınevi))
    con.commit()

def yazarSil(yazar):
    cursor.execute("delete from kitaplık where yazar = ?", (yazar,))
    con.commit()

"""
isim = input("Kitap Adı Giriniz: ")
yazar = input("Kitabın Yazarını Giriniz: ")
yayınevi = input("Yayınevi: ")
sayfaSayisi = int(input("Sayfa Sayısı: "))
"""
verileriGuncelle("yayınevi","Everest")
yazarSil("ben")
verileriAl()
con.close()