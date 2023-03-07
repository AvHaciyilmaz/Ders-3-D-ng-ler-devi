# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı


baslangic: int = 1
bitis: int = int(input("Bitiş: "))
tek_toplam = 0
cift_toplam = 0

if bitis < 1:
    print("Sayı 0 dan büyük olmalıdır")
else:
    while baslangic <= bitis:
        if baslangic %2 != 0:
            tek_toplam += baslangic ** 2
        else:
            cift_toplam += baslangic ** 3
        baslangic += 1

print(f"Tek_toplam: {tek_toplam}")
print(f"Cift_toplam: {cift_toplam}")























# baslangic: int = 1
# bitis: int = int(input("Bitiş: "))
# tek_toplam = 0
# cift_toplam = 0
#
# if bitis < 1:
#     print("Sayı 0 dan büyük olmalıdır")
# else:
#     while baslangic <= bitis:
#         if baslangic %2 != 0:
#             baslangic ** 2
#             tek_toplam += baslangic
#         else:
#             baslangic ** 3
#             cift_toplam += baslangic
#         baslangic += 1
#
# print(f"Tek_toplam: {tek_toplam}")
# print(f"Cift_toplam: {cift_toplam}")