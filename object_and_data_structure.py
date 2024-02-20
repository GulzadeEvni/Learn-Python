# #       Sayı Tipleri
# # İki sayı tipi vardır integer, float.
# number = 5
# number2 = 5.0
# print(type(number))
# print(type(number2))

# #        Math Operators
# # +, -, *, /, **, %, //

# #       Değişken Tanımlama
# # Sayı ile başlamaz, _ başta olabilir(_number), büyük-küçük harf duyarlılığı vardır, türkçe karakter kullanılmamalı.

# #       Veri Tipi Dönüşümleri
# # int to float için
# number3 = 5
# print(float(number3))
# # float to int için
# number4 = 4.0
# print(int(number4))
# # bool to string
# isTrue = True
# print(str(isTrue))
# # bool to int
# print(int(isTrue))
# # Veri Türü Dönüşümleri için Örnek
# Alan_value = int(input("Lütfen dairenin alanını giriniz: "))
# pi_value = 3.14
# Daire_alani = pi_value * pow(Alan_value,2)
# print("Dairenin Alanı: {} ".format(Daire_alani))
# # formatlama
# result = 200 / 700
# print('the result is {r:1.4}'.format(r=result))
# String Metotları
# message = "hello there,my name is Gülzade"
# #message = message.strip()
# message = message.split(",")
# message = '*'.join(message)
# print(message)
# String Metot Alıştırma
# website = "http://www.sadikturan.com"
# course = "Python Kursu"
# # 1-website'ın sadece www.sadikturan.com bu kısmı kalsın
# result = website.lstrip("htp:/")
# print(result)
# # 2- www.sadikturan.com sadece sadikturan kısmı kalsın
# result2 = result.strip("w.com")
# print(result2)
# # 3- website içinde kaç tane a var bul
# result3 = website.count("a")
# print(result3)
# # 4
# result4 = 'Hello'.center(50,"*")
# print(result4)
# result4 = 'Hello'.ljust(50,"*")
# print(result4)
# result4 = 'Hello'.rjust(50,"*")
# print(result4)

# Listeler
# Farklı değişkenler depolanabilir.
# list1 = ['one', 'two', 'three']
# list2 = ['four', 'five', 'six']
# numbers = list1 +list2
# print(len(numbers))

# userA = ['Sadık', 30]
# userB = ['Çınar',2]
# users = [userA , userB]
# print(users)
# print(users[1][0])

# İstenilen indise eleman ekler
# number = [1,2,2,8,4,5,]
# number.insert(3,74)
# number.insert(-1,100)
# number.pop()#index no belirtilmezse sondan siler, belirtilirse o indeksi siler.
# number.remove(1)# istenilen değeri siler
# number.sort()
# number.clear()# tüm elemanları siler.
# print(number)
# print(number.count(2))

# Tuple
# tuple = ('Ayşe', 'Fatma')
# tuple[0] = 'Deniz' # Hata verir tuple'da elemanlar değiştirilemez.
# print(tuple)

# Dictionary (key - value) şeklinde çalışır.
# plakalar = {'Kocaeli' : 41, 'İstanbul': 34}
# plakalar['ankara'] = 6
# print(plakalar)
# print(plakalar['İstanbul'])

# users = {'sadıkturan': {
#             'age': 36,
#             'mail': 'sadık@gmail.com',
#             'adres': 'Kocaeli'
#         }, 
#          'çınarturan': {
#             'age': 2,
#             'mail': 'çınar@gmail.com',
#             'adres': 'Kocaeli'
    
#          }
#          }
# print(users['çınarturan']['age'])

# Sets
# indekslenemezdir.İndeks numaraları ile elemanlara ulaşılamaz.
# fruits = {'orange','apple','banana'}
# #print(fruits[0]) #Hata verir
# fruits.add('cheery')
# fruits.update(['mango','grape'])# zaten varolan bir elemanı tekrar eklemez.
# print(fruits)





