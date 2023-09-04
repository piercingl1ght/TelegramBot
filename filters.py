
from telebot import TeleBot
from telebot.types import Message
from telebot.custom_filters import SimpleCustomFilter, AdvancedCustomFilter

class MySimpleFilter(SimpleCustomFilter):
    key = "simple"
    bannedWords = ["fuck", "shit", "ass", "cunt", "dick"]
    def check(self, update: Message) -> bool:
        for word in MySimpleFilter.bannedWords:
            if word in update.text:
                return True
        return False