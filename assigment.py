# numbers = 1,2,3,4,5,6
# x, *y, z = numbers # bu kullanımda x ilk değeri alır, z sonuncu değeri alır, *y kalan değerleri yani ortadaki değerleri alır.
# *x, y, z =numbers 
# print(x)

# #Alıştırmalar
# #1-Girilen sayının 0-100 arası olduğunu kontrol etme
# input_value = int(input("Bir Sayı Giriniz: "))
# if 0 < input_value < 100:
#     print("Doğru Aralıkta")
# else:
#     print("Yanlış Aralıkta")

# #2- Girilen sayının pozitif çift sayı olduğunu bulma
# value = int(input("Bir Sayı Giriniz: "))
# even = value % 2
# if even == 0 and value >= 0:
#     print("Sayı Pozitif Çift")
# else:
#     print("Sayı Pozitif Çift Değil")

# #3-Girilen sayının pozitif-negatif çift olduğunu bulma
# value = int(input("Bir Sayı Giriniz: "))
# if (value <= 0) and ((value % 2)== 0):
#     print("Sayı Negatif Çift")
# elif (value >= 0) and ((value % 2)== 0):
#     print("Sayı Pozitif Çift")
# else:
#     print("Sayı Çift Değil")


# # Identity Operator: is
# x, y = [1,2,3]
# z = [1,2,3]
# print(x == z)#True döner çünkü değerleri karşılaştırır ve değerleri aynıdır
# print(x is z)# False döner çünkü is değer karşılaştırması yapmaz (bellekteki adresleri farklı olduğu için ) false döner.

# # Membership Operator : in
# name = "ali"
# print('a' in name)
# print('a' not in name)