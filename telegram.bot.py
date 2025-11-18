import telebot
import paramiko

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    print (f'Получено сообщение: {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    print (f'Отправлено сообщение: {mess}\n')

@bot.message_handler()
def get_user_message(message):
    print (f'Получено сообщение: {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    if message.text.lower() == 'sysnmp':
        with open('sysnmp.help', 'r') as f:
            mess = f.read()
        bot.send_message(message.chat.id, mess, parse_mode='html')
        print (f'Отправлено сообщение: {mess}\n')
    if message.text.lower() == 'ssh':
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        f = 0
        bot.send_message(message.chat.id, 'Выполняю попытку подключения...')
        print ('Выполняю попытку подключиться к 95.220.147.57...')
        try:
            ssh.connect(hostname='95.220.147.57', username='Пользователь', password='', timeout=5)
            bot.send_message(message.chat.id, '<b>Успешно</b>', parse_mode='html')
            print ('Подключение выполнено успешно')
            f = 1
        except Exception:
            bot.send_message(message.chat.id, 'Попытка подключения не удалась!')
            print ('Попытка подключения не удалась')
        if f == 1:
            ssh.close()

print ('Bot started')
bot.polling(none_stop=True)
