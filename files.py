# 11.1
# Dosya açmak ve oluşturmak için open() kullanılır
# Kullanımı: open(dosya_adı, dosya_erişim_modu)

# "w":yazma modu. Dosyayı konumda oluşturur.
# "a":ekleme. Dosya konumda yoksa oluşturur
# "x": Sadece dosya oluşturur. Dosya zaten varsa hata verir.İçeriği değiştirmeyeceksek kullanılır.
# "r": okuma. varsayılan. Dosya konumda yoksa hata verir.

#file = open("newfile.txt","w",encoding='utf-8') # bulunulan konumda dosyayı oluşturur
#file.close() # dosya içeriği fazlaysa işimiz bittikten sonra dosyayı kapatmalıyız
#file.write("Gülzade Evni") # dosyaya bilgi yazar.Önceki dosya içeriğini siler ve son yazılanı ekler.
#file.close()

# file = open("newfile.txt","a",encoding="utf-8") # a modu içeriği her çalıştırdığında yazar ve içerik kaybolmaz
# file.write("Gülzade Evni  ")
# file.close()

# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya bulunamadı.")
# finally:
#     file.close()

# # 11.2
# file = open("newfile.txt","r",encoding="utf-8")
# # for döngüsü ile okuma
# for i in file:
#     print(i, end="") # end ile boş bir satır eklenmez.

# # read() fonksiyonu ile
# content = file.read()
# print(content)
# file.close()

# content2 = file.read(5) # içeriğin ilk 5 karakterini alır.
# print(content2)
# file.close()

# # readline() fonksiyonun ile: Her çalıştırıldığında satır satır okur.
# print(file.readline(), end="")
# file.close()

# # 11.3 
# # Dosya okuma işlemleri
# with open("newfile.txt","r",encoding="utf-8") as file: # with kullanıldığında dosya kapatma işlemi yapmaya gerek yoktur.
#     content = file.read()
#     print(content)
#     print(file.tell())# imlecin konumunu verir.


# # 11.4
# # Dosya Güncellemeleri
# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ hem okuma hem yazma işlemini temsil eder.
#     print(file.read())

# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ hem okuma hem yazma işlemini temsil eder.
#     file.write("Ayaz")

# # farklı örnek
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nAyazzzzzz Kuşum")
# with open("newfile.txt","r",encoding="utf-8") as file: # r+ hem okuma hem yazma işlemini temsil eder.
#     print(file.read())






