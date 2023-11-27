import os

PATH = 'G:/Projects/dist'
VES_GRADE = {'0': 'Байт', '1': 'КБайт', '2': 'МБайт', '3': 'ГБайт'}
FILES = []

class File():
    def __init__(self, name, ves):
        self.name = name
        self.ves = ves

    def get_info(self, mode):
        if mode:
            print('NAME: {} VES: {}'.format(self.name, self.ves))
        else:
            print('NAME: {}\nVES: {}'.format(self.name, self.ves))

l = os.listdir(PATH)
for file in l:
    name = file
    ves = int(os.stat('{}/{}'.format(PATH, file)).st_size)
    grade = 0
    while ves > 1024:
        ves = round(ves / 1024, 2)
        grade += 1
    ves = '{} {}'.format(ves, VES_GRADE.get(str(grade)))
    file = File(name, ves)
    FILES.append(file)

for file in FILES:
    file.get_info(mode=1)
    if file.name == 'default.exe':
        print ('FOUND POOP!')