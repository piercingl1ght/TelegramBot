from telebot.handler_backends import State, StatesGroup


class ElectionStates(StatesGroup):
    start = State()
    choosing = State()
    end = State()
