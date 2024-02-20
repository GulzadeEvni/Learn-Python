# 15.1 
# from datetime import datetime
# result = dir(datetime)
# print(result)

# result = datetime.now()
# result2 = result.year
# result2 = result.month
# print(result2)

# zaman = result.ctime()
# rint(zaman)

# simdi = datetime.today()
# res = datetime.strftime(simdi,'%Y') #yılı verir
# res = datetime.strftime(simdi,'%X') #saati verir
# res = datetime.strftime(simdi,'%d') # günü verir
# print(res)

# t = '3 february 2023 hour 17:37'
# dt = datetime.strptime(t,'%d %B %Y hour %H:%M')
# print(dt)

# birthday = datetime(2000,11,20,9,30)
# print(birthday)

# 15.2 
#import os, datetime
#print(os.name)

#dizin değiştirme
#os.chdir('../..')# .. bir üst dizine geçer ../.. iki üst dizine geçer
#os.chdir('C:\\')

# klasör oluşturma
#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasor")

# # listeleme
# b = os.listdir('C:\\')
# print(b)

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# # dosya hakkında bilgi verir
# c = os.stat("loops.py")
# c = datetime.datetime.fromtimestamp(c.st_ctime)
# print(c)


# # uygulama çalıştırma
# os.system("notepad.exe")

# # path: uzantılar üzerinde işlem yapar
#d = os.path.abspath("loops.py")# dosyanın konumunu verir
#print(d)


# etkin dizin gösterme
# a = os.getcwd() 
# print(a)

# 15.3
import re
str = "Python Kursu: Python Programlama"
# result = re.findall("Python",str)
# result = len(result)
# print(result)

result = re.split(" ",str)
print(result)