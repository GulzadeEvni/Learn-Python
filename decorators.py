# 13
# # decoratorler, bir fonksiyonu özellik eklemeye ve o özelliği diğer fonksiyonlarda kullanmaya yarar.
# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki kısım")
#         func(name)
#         print("fonksiyondan sonraki kısım")
#     return wrapper

# # def Hello():
# #     print("Hello")


# # Hello = my_decorator(Hello)
# # Hello()

# # VEYA
# @my_decorator
# def Hello(name):
#     print("Hello",name)

# Hello("Gülzade")


# Farklı örnek
import math, time
def zaman_hesapla(func):
    def inner(*args, **kwarg):

        start = time.time()
        time.sleep(1)
        func(*args, **kwarg)
        finish = time.time()
        print("fonksiyon" +func.__name__ +  str(finish - start) + "saniye sürdü")
    return inner

@zaman_hesapla
def us_alma(a,b):

    print(math.pow(a,b))

@zaman_hesapla
def faktoriyel(num):

    print(math.factorial(num))


us_alma(2,3)
faktoriyel(4)