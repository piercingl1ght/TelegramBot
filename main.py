from telebot import TeleBot
from telebot.types import Message
from telebot.util import extract_arguments

bot = TeleBot("6539537760:AAGCSGXFqBdqkBE9exWJy8UU6zpnSUvn85s")


@bot.message_handler(commands=['start'])
def start_cmd(message: Message):
    msg = "Hello you are using profhome_test_bot!\nType /help for more information"
    bot.send_message(chat_id=message.chat.id, text=msg)


@bot.message_handler(commands=['help'])
def help_cmd(message: Message):
    msg = ( "/start - start using bot/hello - replies \"Hello world!\"\n"
            "/awc - replies \"ASS WE CAN\"\n"
            "/prof - replies \"home\"\n"
            "/nword - gives you n-word pass\n" )
    bot.send_message(chat_id=message.chat.id, text=msg)


@bot.message_handler(commands=['awc'])
def awc_cmd(message: Message):
    bot.send_message(chat_id=message.chat.id, text="ASS WE CAN")


@bot.message_handler(commands=['prof'])
def awc_cmd(message: Message):
    bot.send_message(chat_id=message.chat.id, text="home")


@bot.message_handler(commands=['nword'])
def awc_cmd(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Gratz!!!\nYou now have n-word pass ma nigga!")


@bot.message_handler()
def hello_world(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Sorry\nI do not understand you!")


bot.infinity_polling()