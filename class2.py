from datetime import date

class Person:
    def __init__(self,name,surname,birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        return age
        

if __name__ == "__main__":
    person = Person("name","surname",date(2000,2,15))
    print(person.age())
