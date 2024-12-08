sayilar= [3,5,7,2,12,32,45]

#1- "sayilar" listesindeki her bir elemanı yazdırınız.
x=0
for x in sayilar:
    print(x)

#2- "sayilar" listesinde hangi sayilar 3 ü katıdır?
x=0
for i in sayilar:
    if i%3==0:
        print(i)

#3- "sayilar" listesinde tüm sayıların toplamı nedir?
print("Sayılar listesindeki elemanların toplamı : " + str(sum(sayilar))) 

urunler= ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

#4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanarak.)

iphone_marka=[]
for urun in urunler:
    if urun.find("iphone") != -1:
        iphone_marka.append(urun)
print("Iphone marka ürünler: " , iphone_marka)

#5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)

samsung_marka=[]
for urun in urunler:
    if urun.find("samsung") != -1:
        samsung_marka.append(urun)

print("Samsung ürün sayısı: " +str(len(samsung_marka)))

                     
