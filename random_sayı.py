print("performans ödevi ")
print("____________________________")


print("no 26 rasgele sayı üretimi ve liste analızzı")
#burada random(rasgele)sayı üretmek için bir kütüphane kullanıyoruz
import random
degisken_sayi=int(input("oluşturulcak sayı aralğığı seçin="))
sayi=random.randint(0,degisken_sayi)

#liste oluşturma 
sayi_listesi=[]
#içiniboşbırakıyoruz çunku rasgele satyı gelcek

sayi_listesi.append(sayi)
#sayıyı listeyeekliyoruz
print(sayi_listesi)
# ANALİZ KISMI BEN BURDA OYUNA DÖNÜŞTÜRÜYPRUM

#EL YAPIMI OYUN 
aralik=int(input("OYUNU BAŞLATMAK İÇİN SAYI GİRİN="))
alınan_sayi=random.randint(0,aralik)

print(" SAYI TAHMİN OYNU BAŞLADI")
print(" SEÇTİĞİNİZ ARALIK 0,",aralik)

print("ÖĞRENİM sayıhakkında bilgiler alcaksın her 1 bilgi de 1 deneme hakkın olcak")

print()

print("SORU 1= sayın  0 ile 11 arası bir sayı  ile çarpıldı ")

soru_1=alınan_sayi*random.randint(0,11)

print(soru_1)

hak_1=int(input("sayıyı tahmin edin ="))

if hak_1==alınan_sayi:
    print("SAYI DOĞRU OYUN BİTTİ")

else:
    print("sayı yanlış 2. soru geliyor")

soru_2=alınan_sayi+random.randint(0,24)
print()
print("soru 2 sayın 0 ile 24 arasıbir sayı ile toplandı")
print(soru_2)
hak_2=int(input("sayıyı tahmin edin ="))
if hak_2==alınan_sayi:
    print("DOĞRU TAHMİN ")

else:
    print("yanlış  cevap soru 3 geliyor")
print("soru 3 sayın 1 ile 492 arası bir sayı ile bölündü")
soru_3=alınan_sayi/random.randint(1,492)
print(soru_3)
hak_3=int(input("sayıyı tahmin edin ="))
son_soru=alınan_sayi+(999)/2*35+alınan_sayi

if hak_3==alınan_sayi:
    print("DOĞRU TAHMİN OYUN BİTTİ")

else:
    bonus_soru=str(input("HAKKIN BİTTİ OYUN SONA ERDİ SON BİR ŞANS İSTERMİSİN  e/h="))
    print(bonus_soru)
    if bonus_soru=="e":
        print("BONUS SORUN= sayın+999/2*35+sayn kolay gelsin")
        hak_4=int(input("SON TAHMİNİ YAPIN ="))
        if hak_4==alınan_sayi:
            print("TEBRİK EDİYORUM DOĞRU BİLDİNİZ")

        else:
            print("OYUN BİTTİ BECERİKSİZ")

    else:
        print("KORKAK OLDUĞUNU BİLMİYORIM HAHAHA oyun bitti")




