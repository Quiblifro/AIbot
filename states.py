from aiogram.fsm.state import StatesGroup, State

class MenuState(StatesGroup):
    isgenerated = State()
    level = State()
    theme = State()
