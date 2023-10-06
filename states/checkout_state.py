from aiogram.dispatcher.filters.state import State, StatesGroup


class CheckoutState(StatesGroup):
    check_cart = State()
    name = State()
    address = State()
    confirm = State()
