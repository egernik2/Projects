import json

answers = {}

for i in range(1, 11):
    answer = input(f"Введите ответ на задание {i} для синей команды: ")
    answers[f"blue_{i}"] = answer
    answer = input(f"Введите ответ на задание {i} для красной команды: ")
    answers[f"red_{i}"] = answer

with open("answers.json", "w") as f:
    json.dump(answers, f, indent=2)
print('Сохранено!')