# SORU: Kullanıcıdan alınan sayının asal olup olmadığını ekran yazdırınız.
# Asal sayı 1 ve kendisinden başka hiç bir sayıya bölünmeyen sayıdır.

i: int = 2
sayi: int = int(input("Lütfen kontrol edilecek sayıyı giriniz: "))
asal_mi: bool = True

while i < sayi:
    if sayi %i == 0:
        asal_mi = False
        break
    i += 1
if asal_mi:
    print(f"Sayı asaldır: {sayi}")
else:
    print(f"Sayı asal değildir: {sayi}")