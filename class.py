# # constructor (yapıcı) metot
# class Person():
#     #class attriubute
#     address = 'no information'


#     def __init__(self,name,year):# name ve year değişkenleri(object attribute)'tur.
#         #  object attribute
#         self.name = name
#         self.year = year

#     #instance methods
#     def intro(self):
#         print("Hello {}".format(p1.name))

#  #object(instance)
# p1 = Person('ali',2000)
# p1.intro()
# # # accessing object attiributes
# # print("name: {}, yılı: {}, adresi: {}".format(p1.name,p1.year,p1.address))

# # Inheritance(Kalıtım): Miras alma
# class Person():
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#         print("Person created")

# class Student(Person):
#     def __init__(self,name,year):
#         Person.__init__(self,name,year)
#         print("Student created")
# s1 = Student()