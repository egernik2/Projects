from jinja2 import Template

# Создаем шаблон
template = Template('''<html>
                            <body>
                                <h1>Отчёт</h1>
                                {{items}}
                            </body>
                        </html>''')

# Заполняем шаблон данными
title = 'Отчет'
items = ''
items_item1 = ''

l = {
    "database1": {
        "database": "main",
        "user": "postgres",
        "password": 6653549,
        "host": "localhost",
        "port": 5432
    },
    "database2": {
        "database": "default",
        "user": "postgres",
        "password": 6653549,
        "host": "localhost",
        "port": 5432
    }
}

for item in l:
    tmp = '''
    <h3>{}<h3>
    <ul>
        {}
    </ul>
    '''.format(item)






for item in l:
    items += '<h3>{}</h3>'.format(item)
    for i in l[item].items():
        j, k = i
        items_item1 += '<li>{} - {}</li>'.format(j, k)
    
result = template.render(items=items)

# Сохраняем результат в файл
with open('report.html', 'w') as f:
    f.write(result)