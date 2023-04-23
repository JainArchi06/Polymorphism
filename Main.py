#runtime PolyMorphism
class parent:
    name="Tom"
class child(parent):
    name="jerry"

obj=child()
print(obj.name)

# using pass method
class parent:
    name="Tom"
class child(parent):
    pass

obj=child()
print(obj.name)

#Compiletime Polymorphism
class Bank:
    def rateofinterest(self):
        return 0
class icici(Bank):
    def rateofinterest(self):
        return 10.2
obj=icici()
print(obj.rateofinterest())
obj1= Bank()
print(obj.rateofinterest)