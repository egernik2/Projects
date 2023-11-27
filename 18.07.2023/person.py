import json
from pprint import pprint

class Person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return 'Name: {}\nAge: {}\nSalary: {}'.format(self.name, self.age, self.salary)

    def get_info(self):
        return 'Name: {}\nAge: {}\nSalary: {}'.format(self.name, self.age, self.salary)

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'salary': self.salary}

    def get_info_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
    

# def main():
#     roman = Person('Ильин Роман', 25, 98000) # Creating object of class Person
#     print('Object created\n') # Info about object was created
#     print('Getting information\n') # Info about what to doing now
#     print(roman.get_info()) # Printing Roman info
#     print('\n\n') # Adding spacing
#     print('Getting json information\n')
#     print(roman.get_info_json()) # Printnint Roman json info
#     print('\n\n') # Adding spacing
#     print('Getting information from dict\n')
#     print(roman.to_dict())

# if __name__ == '__main__':
#     main()