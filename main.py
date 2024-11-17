import telebot
import random

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7910185627:AAHujjf9DRMthgQBbgd2vmm-Yby5JgSyaS4")

def double_letter(s):
    return ''.join([c * 2 for c in s])

def secret_function(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return a + b

# Обработчик команды '/start', '/hello, /heh'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

# Обработчик команды '/double'
@bot.message_handler(commands=['double'])
def handle_double(message):
    text = message.text.split(maxsplit=1)
    if len(text) > 1:
        response = double_letter(text[1])
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Please provide a string to double.")

# Обработчик команды '/secret'
@bot.message_handler(commands=['secret'])
def handle_secret(message):
    args = message.text.split()
    if len(args) == 3:
        a, b = args[1], args[2]
        try:
            a, b = int(a), int(b)
        except ValueError:
            pass
        response = secret_function(a, b)
        bot.reply_to(message, str(response))
    else:
        bot.reply_to(message, "Please provide two arguments.")

# Обработчик команды '/flipcoin'
@bot.message_handler(commands=['flipcoin'])
def handle_flip_coin(message):
    result = flip_coin()
    bot.reply_to(message, f"Выпало: {result}")

# Функция для подкидывания монетки
def flip_coin():
    flip = random.randint(0, 1)
    return "ОРЕЛ" if flip == 0 else "РЕШКА"

# Запуск бота
bot.polling()
