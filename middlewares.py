from telebot import TeleBot
from telebot.types import Message
from telebot.handler_backends import BaseMiddleware, CancelUpdate

class AntifloodMiddleware(BaseMiddleware):
    def __init__(self, bot: TeleBot, limit: float):
        self.bot = bot
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']

    def pre_process(self, message: Message, data):
        if not message.from_user.id in self.last_time:
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            self.bot.send_message(message.chat.id, 'You are sending messages too often!')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date
        
    def post_process(self, message, data, exception):
        pass


class ExtraArgsMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message', 'edited_message']
        # Always specify update types, otherwise middlewares won't work

    def pre_process(self, message: Message, data):
        data['arg1'] = "I'm the arg1 from the middleware!"
        data['arg2'] = "I'm the arg2 from the middleware!"
        
    def post_process(self, message, data, exception):
        pass
