class Person():
    def __init__(self, name:str, sec_name:str, age:int, ID:int):
        self.name = name
        self.sec_name = sec_name
        self.age = age
        self.id = ID
        print ('Init Person *{}* complete.'.format(self.name))

    def info(self):
        print ('ID: {}'.format(self.id))
        print ('Name: {}'.format(self.name))
        print ('Second name: {}'.format(self.sec_name))
        print ('Age: {}'.format(self.age))

    def change_age(self, cur_age:int):
        self.age = cur_age
        print ('Age for *{}* has been changed!'.format(self.name))

def main():
    l = []
    ID = 1
    Roman = Person('Roman', 'Ilin', 24, ID)
    l.append(Roman)
    ID += 1
    Margarita = Person('Margarita', 'Kulikova', 25, ID)
    l.append(Margarita)
    for person in l:
        person.info()

if __name__ == '__main__':
    main()