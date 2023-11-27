from person import Person

def menu():
    print('\nMAIN MENU\n')
    print('Actions:\n')
    print('1. Create new person')
    print('2. Load person from JSON')
    print('0. Exit')

def create_new_person():
    name = input('Name and second name: ')
    age = input('Age: ')
    salary = input('Salary: ')
    person = Person(name, age, salary)
    return person

def main():
    menu()
    choice = int(input('Chioce: '))
    if choice == 1:
        person = create_new_person()
    elif choice == 2:
        pass
    elif choice == 0:
        exit()
    while True:
        print('1. Get info')
        print('2. Get info JSON')
        print('3. Save info')
        a = int(input('Choice: '))
        if a == 1:
            person.get_info()
        elif a == 2:
            person.get_info_json()
        elif a == 3:
            file_name = input('Filename: ')
            person.save_info(file_name)