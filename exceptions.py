# # error => hata
# # error handling => hata yönetimi

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except Exception as e:
#         print('Yanlış bilgi girildi.', e)
#     else:
#         break
#     finally: # finally dosya okuma işlemlerinde faydalı olur.
#         print('try except sonlandı.')

# # 10.3
# import re
# def check_password(psw):
#     if len(psw) < 8:
#         raise Exception("Parola en az 7 karakter olmalı")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermeli.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola büyük harf içermeli.")
#     else:
#         print(psw)
# password = "12345678kkL"

# try:
#     check_password(password)
# except Exception as e:
#     print(e)

# # Diğer Örnek
# class Person:
#     def __init__(self,name,year):
#         if len(name) > 10:
#             raise Exception("name alanı fazla karakter içeriyor.")
#         else:
#             self.name = name
# p = Person("Aliiiiiiiii",2000)

# # 10.4
# liste = ["1","2","5a","abc"]
# #1: Liste elemanları içindeki sayısal değerleri bulunuz.
# for i in liste:
#     try:
#         result = int(i)
#         print(result)
#     except ValueError:
#         continue

# # 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olup olmadığını kontrol et
# while True:
#     girdi = input('sayi: ')
#     if girdi == 'q':
#         break
#     try:
#         result = float(girdi)
#         print("Sayı: ",girdi)
#     except ValueError:
#         print("Geçersiz sayı")
#         continue

        
    
    

