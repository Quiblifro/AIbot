from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import NotesCallbackFactory

buttons_1 = [
    [
        KeyboardButton(text="🤖 Сгенерировать задачу"),
        KeyboardButton(text="📁 Взять задачу из архива ")
    ],
]
levels = [
    [   
        KeyboardButton(text="back"),
        KeyboardButton(text="🔰Just started"),
        KeyboardButton(text="📕 Junior"),
        KeyboardButton(text="👔 Middle"),
        KeyboardButton(text="🎩 Senior"),
    ],
]
problem_menu = ReplyKeyboardMarkup(keyboard=buttons_1, resize_keyboard=True, input_field_placeholder="Откуда вы хотите взять задачу?")
level_menu = ReplyKeyboardMarkup(keyboard=levels, resize_keyboard=True, input_field_placeholder="Ваш уровень в python?")


def problem_nav(id):
    builder = InlineKeyboardBuilder()
    
    builder.button(text="⏹", callback_data=NotesCallbackFactory(action="stop"))
    builder.button(text="⏩", callback_data=NotesCallbackFactory(action="next"))

    return builder.as_markup()