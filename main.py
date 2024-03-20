1-Kullanicinin girdigi boy ve agirlik degerlerine gore vucut kitle indeksini (VKİ = agirlik/(boy*boy)) hesaplayiniz.

boy  = float(input('Lütfen boyunuzu "metre" cinsinden giriniz...'))
kilo = float(input('Lütfen kilonuzu "kilogram" cinsinden giriniz...'))
VKİ= kilo / (boy * boy)
print("Vucut Kitle Endeksiniz", VKİ)

2-Maasi ve zam orani girilen iscinin zamli maasini hesaplayarak ekranda gösteriniz.

Güncelmaas=0
maas=input("Mevcut Maasi Gir : ")
zam=input("Zam Oranı(%) : ")
Güncelmaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamli Maaş :",Guncelmaas)

3-Kullanicinin girdigi üc sayi arasinda en buyuk olani bulan ve sonucu yazdiran bir program yaziniz

sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))
sayi3 = int(input("Lütfen Üçüncü Sayıyı Giriniz: "))

enBuyuk = max(sayi1, sayi2, sayi3)
print("En buyuk deger:", enBuyuk)

4-Dairenin alanini ve cevresini hesaplayan python kodunu yazınız.(Dairenin yaricapini kullanicidan aliniz)

yaricap= input(str("Lütfen dairenin yaricapini giriniz: "))
cevre = 2 * 3 * float (yaricap)
alan= 3 * float (yaricap) * float (yaricap)
print("Dairenin Alani", alan)
print("Dairenin Cevresi", Cevre)

5-Kullanicidan alinan bir sayinin palindrom olup olmadigini bulan bir program yazınız.

for i in range(100,1000):
    s = str(i)
    t = s[::-1]
    if s == t:
        print(s)