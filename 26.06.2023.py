class Person():
    """
    The class Person represents a person.

    Attributes:
        name (str): The first name of the person.
        sec_name (str): The second name of the person.
        age (int): The age of the person.
        id (int): The unique identifier of the person.
    """

    def __init__(self, name: str, sec_name: str, age: int, ID: int):
        """
        Initializes a Person object.

        Args:
            name (str): The first name of the person.
            sec_name (str): The second name of the person.
            age (int): The age of the person.
            ID (int): The unique identifier of the person.
        """
        self.name = name
        self.sec_name = sec_name
        self.age = age
        self.id = ID
        print('Init Person *{}* complete.'.format(self.name))

    def info(self):
        """
        Prints out the information of the person.

        """
        print ('ID: {}'.format(self.id))
        print ('Name: {}'.format(self.name))
        print ('Second name: {}'.format(self.sec_name))
        print ('Age: {}'.format(self.age))

    def change_age(self, cur_age:int):
        """
        Changes the age of the person.

        Args:
            cur_age (int): The new age of the person.
        """
        self.age = cur_age
        print ('Age for *{}* has been changed!'.format(self.name))

def main() -> None:
    """
    The main function of the program.
    """
    persons = []

    roman = Person("Roman", "Ilin", 24, 1)
    persons.append(roman)

    margarita = Person("Margarita", "Kulikova", 25, 2)
    persons.append(margarita)

    for person in persons:
        person.info()

if __name__ == '__main__':
    main()