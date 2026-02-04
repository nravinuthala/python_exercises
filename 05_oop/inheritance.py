class Person():
    def __init__(self, aadharid, firstname, lastname):
        self.aadharid = aadharid
        self.firstname = firstname
        self.lastname = lastname

    def display_personal_details(self):
        return self.aadharid, self.firstname, self.lastname

class Employee(Person):
    def __init__(self, aadharid, firstname, lastname, empid, dept, company):
        super().__init__(aadharid, firstname, lastname)
        self.empid = empid
        self.dept = dept
        self.company = company

    def display_emp_data(self):
        personal_details = self.display_personal_details()
        emp_details = (self.empid, self.dept, self.company)
        return personal_details, emp_details

emp1 = Employee(1234, "Nag", "Rav", 101, "Finance","Acme")
print(emp1.aadharid)
details = emp1.display_personal_details()
print(details)
