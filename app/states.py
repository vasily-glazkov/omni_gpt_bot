from aiogram.fsm.state import State, StatesGroup

class Chat(StatesGroup):
    text = State()
    wait = State()


class Image(StatesGroup):
    text = State()
    wait = State()
