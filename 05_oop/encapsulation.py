class Voter():
    def __init__(self, name, aadharid):
        self.name = name
        self.__aadharid = aadharid

    def display(self):
        print(self.name)
        print(self.__aadharid)
    
    def get_aadharid(self):
        return self.__aadharid

    def set_aadharid(self, new_aadharid):
        self.__aadharid = new_aadharid 

nagaraj = Voter("Nagaraj", 1234)

nagaraj.display()

print(nagaraj.name)
# print(nagaraj.__aadharid)
print(nagaraj.get_aadharid())
nagaraj.set_aadharid(5678)
nagaraj.display()