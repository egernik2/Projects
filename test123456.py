import pymorphy2
morph = pymorphy2.MorphAnalyzer()
fio = 'Ильин Роман Григорьевич'
second_name, first_name, middle_name = fio.split(' ')
second_name = morph.parse(second_name)[0]
print (second_name)