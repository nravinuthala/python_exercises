class Student():
    batch = "Python_AI"

    def __init__(self, name, city, term1_score, email,mobile):
        self.name = name
        self.city = city
        self.term1_score = term1_score
        self.email = email
        self.mobile = mobile
    
    def display_info(self):
        print(self.name)
        print(self.city)


mani = Student("Maniraj", "GDK", [73.3, 84], "some@email.com", 1234567890)
mani.display_info()
print(mani.batch) # prints class variable value
print(Student.batch) # prints class variable value
print(Student.name) # gives error that name is not defined 


