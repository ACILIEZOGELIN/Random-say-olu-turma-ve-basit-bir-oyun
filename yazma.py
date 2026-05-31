import os

# Kodun çalıştığı klasörün yolunu otomatik bulur
klasor_yolu = os.path.dirname(os.path.abspath(__file__))
# txt dosyasının yolunu kodun yanına sabitler
dosya_konumu = os.path.join(klasor_yolu, "ogrenciler.txt")

ogrenci_ad = input("Kaydedilecek öğrencinin adı ve soyadı: ")
ogrenci_no = input("Öğrenci numarası: ")

# Artık direkt "dosya_konumu" değişkenini kullanıyoruz
with open(dosya_konumu, "a", encoding="utf-8") as dosya:
    dosya.write(f"No: {ogrenci_no} - Adı: {ogrenci_ad}\n")

print("Öğrenci başarıyla kaydedildi!")
