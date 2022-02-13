# class Gesan:
#     pass
#
# a = Gesan()
# print(type(a))

class Gesan:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = Gesan()
a.setdata(1,2) # a = self , 1 = first, 2 = second
print(a.first)
print(a.second)