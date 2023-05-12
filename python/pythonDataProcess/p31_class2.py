class SmartPhone(object):
    def __init__(self, brand, details):
        self.brand = brand
        self.details = details
    def __str__(self):
        return f'str : {self.brand} - {self.details}'
    def __repr__(self):
        return f'repr : {self.brand} - {self.details}'
    def __doc__(self):
        return f'This class is Smart Phone Class. It is have a brand name and detail description.'

SmartPhone1 = SmartPhone('IPhone', {'color': 'white', 'price': 10000})
SmartPhone2 = SmartPhone('Galaxy', {'color': 'Black', 'price' : 8000})
SmartPhone3 = SmartPhone('Blackberry',{'color':'Silver', 'price':6000})

print(SmartPhone1)
print(SmartPhone1.__dict__)
print(SmartPhone2.__dict__)
print(SmartPhone3.__dict__)

print(id(SmartPhone1))
print(id(SmartPhone2))
print(id(SmartPhone3))

print(SmartPhone1.brand == SmartPhone2.brand)
print(SmartPhone1 is SmartPhone2)

print(SmartPhone.__str__(SmartPhone1))
print(SmartPhone.__repr__(SmartPhone2))
print(SmartPhone.__doc__)
print()