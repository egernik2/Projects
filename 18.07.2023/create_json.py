from person import Person
import json

persons = []
persons.append(Person('Ильин Роман', 25, 98000))
persons.append(Person('Маркелов Дмитрий', 25, 90000))
persons.append(Person('Новиков Иван', 23, 130000))
persons.append(Person('Чередниченко Степан', 27, 140000))

data = []

for person in persons:
    data.append(person.to_dict())

with open('18.07.2023/persons.json', 'w', encoding='CP866') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('File saved!')