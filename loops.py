# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for key,value in d.items():# dictionary tipinde for kullanımı
#     print(key,value)

# # Alıştırma
# sayilar = [1,3,5,7,9,12,19,21]
# #1-dizideki 3'ün katı olan sayılar
# for sayi in sayilar:
#     if ((sayi % 3 ) == 0):
#         print(sayi)
# #2-Dizi elemanlarının toplamı
# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

# #3-Dizideki tek sayıların karesi
# for sayi in sayilar:
#     if ((sayi % 2) == 1):
#         print(pow(sayi,2))

# sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir']
# #4-Şehirlerden hangileri en fazla 5 karakterlidir
# for sehir in sehirler:
#     if (len(sehir) <= 5):
#         print(sehir)

# urunler = [
#     {'name':'samsung', 'price': '1000'},
#     {'name':'samsung', 'price': '4000'},
#     {'name':'samsung', 'price': '8000'}
#     ]
# #5-Ürünlerin fiyat toplamı
# toplam = 0
# for urun in urunler:
#     toplam += int(urun['price']) 
# print(toplam)

# # While

# name = ''
# while not name.strip():
#     name = input('İsminiz: ')
# print(name)

# sayilar = [1,3,5,7,9,12,19,21]
# # Soru 1
# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# # Soru 2
# a = int(input("Başlangıç değerini giriniz: "))
# b = int(input("Bitiş değerini giriniz: "))
# i = a
# while i < b :
#     i += 1
#     if (i %2 == 1):
#         print(i)

# # Soru 3
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# # Soru 4
# numbers = []
# i = 0
# while i < 5 :
#     girdi = int(input("Sayı Girin: "))
#     numbers.append(girdi)
#     i += 1
# numbers.sort()
# print(numbers)

# # Enumerate
# index = 0
# greeting = 'Hello There'
# for letter in greeting:
#     print(f'index: {index} letter: {letter}')
#     index += 1

# # greeting'in enumerate ile kullanımı
# greeting = 'Hello There'
# for index , letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter}')

# greeting = 'Hello'
# for item in enumerate(greeting):
#     print(item)

# # Zip: Listeleri birleştirir
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# print(list(zip(list1,list2)))

# for item in zip(list1,list2):
#     print(item)

# # list comprehensions

# numbers = [x for x in range(10)]
# print(numbers)

# numbers = [x**2 for x in range(10)]
# print(numbers)

# numbers = [x*x for x in range(10) if x%3 == 0]
# print(numbers)

# myString = 'Hello'
# myList = [letter for letter in myString]
# print(myList)

# years = [1999,2000,2015,1889]
# ages = [2023-year for year in years]
# print(ages)

# results = [x if x%2==0 else 'TEK' for x in range(1,10)]
# print(results)

# result = [(x,y) for x in range(3) for y in range(3)]
# print(result)

# # Alıştırma 

# import random

# sayi = random.randint(1,100)
# i = 5
# while i > 0:
#     i -= 1
#     tahmin = int(input("Tahmin Edilen Sayı: "))

#     if tahmin == sayi:
#         print("Tberikler")
#         break
#     elif tahmin < sayi:
#         print("Yukarı")
#     else:
#         print("Aşağı")
    
#     if i == 0:
#         print("Hakkınız Bitti.")

# # Alıştırma

# x = int(input("Sayıyı Giriniz: "))
# asalMi = True
# if x == 1 :
#     print("1 Asal Değildir.")
# for i in range(2,x):
#     if x % i == 0:
#         asalMi = False
#         break
# if asalMi:
#     print("Sayi Asal")
# else:
#     print("Asal Değil")
    





    
    



    

