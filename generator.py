# Bellekte yer kaplamayan bir iteratör oluşturur.

def cube():

    for i in range(5):
        yield i ** 3

for i in cube():
    print(i)