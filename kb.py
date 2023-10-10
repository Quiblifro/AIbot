from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import TasksCallbackFactory, ThemeCallbackFactory

buttons_1 = [
    [
        KeyboardButton(text="🤖 Сгенерировать задачу"),
        KeyboardButton(text="📁 Взять задачу из архива ")
    ],
]
levels = [
    [   
        KeyboardButton(text="🔙"),
        KeyboardButton(text="🔰 Just started"),
        KeyboardButton(text="📕 Junior"),
        KeyboardButton(text="👔 Middle"),
        KeyboardButton(text="🎩 Senior")
    ],
]

problem_menu = ReplyKeyboardMarkup(keyboard=buttons_1, resize_keyboard=True, input_field_placeholder="Откуда вы хотите взять задачу?")
level_menu = ReplyKeyboardMarkup(keyboard=levels, resize_keyboard=True, input_field_placeholder="Ваш уровень в python?")
def problem_nav():
    builder = InlineKeyboardBuilder()
    
    builder.button(text="⏹", callback_data=TasksCallbackFactory(action="stop"))
    builder.button(text="⏩", callback_data=TasksCallbackFactory(action="next"))

    return builder.as_markup()

def theme_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text = "условия" , callback_data=ThemeCallbackFactory(theme="условия"))
    builder.button(text = "циклы" , callback_data=ThemeCallbackFactory(theme="циклы"))
    builder.button(text = "арифметика" , callback_data=ThemeCallbackFactory(theme="арифметика"))
    builder.button(text = "списки" , callback_data=ThemeCallbackFactory(theme="списки"))
    builder.button(text = "словари" , callback_data=ThemeCallbackFactory(theme="словари"))
    builder.button(text = "работа со стороками" , callback_data=ThemeCallbackFactory(theme="строки"))
    builder.button(text = "функции", callback_data=ThemeCallbackFactory(theme="функции"))
    builder.button(text = "ООП", callback_data=ThemeCallbackFactory(theme="ООП"))
    builder.button(text = "рандомная тема", callback_data=ThemeCallbackFactory(theme="stop"))

    return builder.as_markup()