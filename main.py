from telebot import TeleBot
from telebot.types import Message
from telebot.util import extract_arguments
from telebot.handler_backends import State, StatesGroup
from telebot.custom_filters import StateFilter
from middlewares import AntifloodMiddleware
from filters import MySimpleFilter
from states import ElectionStates

bot = TeleBot("token", use_class_middlewares=True)

bot.add_custom_filter(StateFilter(bot))
bot.setup_middleware(AntifloodMiddleware(bot, 2.0))
bot.add_custom_filter(MySimpleFilter())


@bot.message_handler(commands=['start'], simple=False)
def start_cmd(message: Message):
    msg = ( "Hello you are using profhome_test_bot!\n" 
            "Type /help for more information\n\n"
            "Choose your president Patrick Bateman or Tomas Shelby\n"
            "type /choose Patrick or /choose Tomas")
    bot.set_state(user_id=message.from_user.id, state=ElectionStates.choosing, chat_id=message.chat.id)
    bot.send_message(chat_id=message.chat.id, text=msg)


@bot.message_handler(commands=['help'], simple=False)
def help_cmd(message: Message):
    msg = ( "/start - start using bot/hello - replies \"Hello world!\"\n"
            "/awc - replies \"ASS WE CAN\"\n"
            "/prof - replies \"home\"\n"
            "/nword - gives you n-word pass\n" )
    bot.send_message(chat_id=message.chat.id, text=msg)


@bot.message_handler(commands=['choose'], state=ElectionStates.choosing, simple=False)
def choose_cmd(message: Message):
    text = message.text.split()
    reply = ""
    if (text[1] == "Tomas"):
        reply = "Great choice!\nYou have choosen the notorious gangster from Birmingham.\nTommy Shelby!"
    elif (text[1] == "Tomas"):
        reply = "Great choice!\nYou have choosen the American Psycho.\nPatrick Bateman!"
    else:
        bot.send_message(chat_id=message.chat.id, text="No candidate with such name!\nTry again!")
        return

    bot.set_state(user_id=message.from_user.id, state=ElectionStates.end, chat_id=message.chat.id)
    bot.send_message(chat_id=message.chat.id, text=reply)


@bot.message_handler(commands=['choose'], state=ElectionStates.end, simple=False)
def elected_cmd(message: Message):
    bot.send_message(chat_id=message.chat.id, text="You have already participated in the 2077 USA elections!\nSee you next time!")


@bot.message_handler(simple=True)
def hello_world(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Stop using bad words!")


@bot.message_handler()
def hello_world(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Sorry!\nI dont't understand you!")


bot.infinity_polling()