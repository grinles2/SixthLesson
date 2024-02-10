# class GrandParent:
# Капусуляция и насоедование
#     #Атрибуты
#     #height = 170
#     #satiety = 100
#     #age = 60
#     def about(self):
#         print("Im grandparent")
#     def about_myself(self):
#         print("Im grandparent")
#
# class Parent(GrandParent):
#     def about_myself(self):
#         print("Im parent")
#         #age = 35
#
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# Полифармотизм
# class Class1:
#     var = 10
#     def __init__(self):
#         self.var = 20
#     def method(self):
#         return "Class 1 METHOD"
# class Class2(Class1):
#     def __init__(self):
#         print(self.var) # 10
#         super().__init__()
#         print(self.var)
#         print(super().var)
#         print(super().method())
#     def method(self):
#         return "Class 2 METHOD"
#
# cl = Class2()
# print(cl.method())

    #height = 50
    #def __init__(self):
        #print(self.height)
        #print(self.age)
        #print(self.satiety)

#ch = Child()


# class Hello_World:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# class Hi(Hello_World):
#     def hi_printer(self):
#
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# hello = Hello_World()
# hello.printer()
#
# hi = Hi()
# hi.hi_printer()