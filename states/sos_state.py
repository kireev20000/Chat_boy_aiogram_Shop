from aiogram.dispatcher.filters.state import State, StatesGroup


class SosState(StatesGroup):
    question = State()
    submit = State()
