query = 'SELECT * FROM JOPA WHERE TIME > '
print ('Старый запрос: {}'.format(query))
a = input('Введите время: ')
query += '"{}"'.format(a)
print ('Новый запрос: {}'.format(query))