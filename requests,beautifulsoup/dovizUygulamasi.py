import requests
import sys
birinciDoviz = "EUR"
print("Bu uygulama girilen cinsten EUR'nun karşılığı olan dövizi söyler...")
ikinciDoviz = input("Döviz: ")

miktar = float(input("Miktar: "))

url = "http://data.fixer.io/api/latest?access_key=a188dda32806028275c1bc3fde289402"

response = requests.get(url)

jsonVerisi = response.json()

try:
    print(jsonVerisi["rates"][ikinciDoviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru giriniz..")
    sys.stderr.flush()
