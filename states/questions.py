from aiogram.dispatcher.filters.state import State, StatesGroup


class AnswerState(StatesGroup):
    answer = State()
    submit = State()
