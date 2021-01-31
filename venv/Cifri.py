import telebot

bot = telebot.TeleBot("1431580607:AAEcDHkWEXr8bHJtf-HaVKGScXAcULpzS6w", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_hello_and_rules(message):
    hello = "--------------------------------\n" \
            "вводи по следующим правилам:\n" \
            "для перевода в двоичную: 2-... (...=число), например\n 2-52\n" \
            "для перевода в десятичную: 10-... (...=число), например\n 10-11000000\n" \
            "Удачи на экзе\n" \
            "--------------------------------\n"
    bot.send_message(message.chat.id, hello)

@bot.message_handler(content_types=['text'])
def send_city(message):
    print(message.text)
    answer = ''
    #answer += "Введите: (2 - перевод в двоичный; 10 - перевод в десятичный; 0 - выход)\n"
    if message.text[0:1] == '2':
        answer += "Число " + message.text[2:len(message.text)] + " в двоичной:\n"
        n = int(message.text[2:len(message.text)])
        str1 = bin(n)
        answer += str1[2:len(str1)]
    elif message.text[0:2] == '10':
        answer += "Число " + message.text[3:len(message.text)] + " в десятичной:\n"
        n = str(message.text[3:len(message.text)])
        str_1 = n
        answer += str(int(str_1, 2))
    else:
        answer += "Неккоректный ввод, попробуйте заново\n"
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)