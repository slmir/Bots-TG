from pyowm import OWM
from pyowm.utils import config
import telebot

bot = telebot.TeleBot("1493614394:AAGt2X4WqTvfPNr7GUDhimQhSBLpbh7LLUE", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_weather(message):
    print(message.text)
    photo = open('C:/Users/Вячеслав/PycharmProjects/TestWeatherBot/1.jpg', 'rb')

    if message.text == "Слава+Катя=?":
        bot.send_photo(message.chat.id, photo)
        answer = "Мой создатель оставил сообщение для тебя\n\n" \
            "Катя, я счастлив, что уже почти 2 года знаком с тобой," \
                 "и всем сердцем люблю тебя, родная\n" \
                 "─▄█▀█▄──▄███▄─\n▐█░██████████▌\n─██▒█████████─\n──▀████████▀──\n─────▀██▀─────"
    else:
        config_dict = config.get_default_config()
        config_dict['language'] = "ru"
        owm = OWM('0e9163d3d6c0fb02ddf0b1ca5363fda2', config_dict)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']

        S = str(w)
        i = S.find("detailed_status", 80)
        status = S[(i + 16):(len(S) - 1)]
        answer = "В городе " + str(message.text) + " сейчас " + status
        answer += "\nТемпература около " + str(temp) + " градусов цельсия" + "\n"

        if temp < 0:
            answer += "Уже меньше нуля, одевайся теплее!"
        elif temp < 10:
            answer += "Достаточно холодно, понадобится шапка!"
        elif temp < 20:
            answer += "Не так холодно, но не жара."
        else:
            answer += "Уфф, одевай че по кайфу, жарко!"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
