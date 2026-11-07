print("HESAP MAKİNESİ")

sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))


print("1 - Toplama")
print("2 - Çikarma")
print("3 - Çarpma")
print("4 - Bölme")

secim= input("Yapmak istediğiniz işlemi seçiniz:")

if secim == '1':
    print("Sonuç:", sayi1 + sayi2)
elif secim == '2':
    print("Sonuç:", sayi1 - sayi2)
elif secim == '3':
    print("Sonuç:", sayi1 * sayi2)
elif secim =='4':
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayı sıfıra bölünemez!")

else:
    print("Geçersiz seçim!")


