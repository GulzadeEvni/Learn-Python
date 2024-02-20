# def add(*params):# tek yıldız bunun bir tuple listesi olduğu anlamına gelir.
#     return sum(params)
# print(add(10,20))

# def displayUser(**params):# ** dictionary old. gösterir.
#     for key,value in params.items():
#         print("{} is {}".format(key,value))

# displayUser(name = 'Ali', age = 30, city = 'Kırşheir')
# displayUser(name = 'Ayşe', age = 30, city = 'Kırşehir')

# # Alıştırma
# value = int(input("Değer Giriniz: "))
# def yazdir(deger):
#     i = 0
#     while i < value:
#         print(deger)
#         i += 1

# yazdir("Gülzade")

# #VEYA
# def yazdir(kelime, adet):
#     print(kelime * adet)
# yazdir('Ali\n', 5)

# # Alıştırma
# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste

# result = listeyeCevir(10,20,50,'Gül')  
# print(result)  

# # Alıştırma

# deger1 = int(input("1. Sayıyı Girin: "))
# deger2 = int(input("2. Sayıyı Girin: "))

# def asalBul(a,b):
#     for sayi in range(a, b+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % 2 == 0):
#                     break
#             else:
#                 print(sayi)

# asalBul(deger1,deger2)
    
# # Alıştırma
# def tamBolen(sayi):
#     sayilar = []
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             sayilar.append(i)
#     return sayilar

# result = tamBolen(20)
# print(result)

# # Lambda, Map, Filter
# def square(num):return num**2
# numbers = [1,3,5,7]
# result = list(map(square,numbers))
# print(result)

# # VEYA 
# for item in map(square,numbers):
#     print(item)

