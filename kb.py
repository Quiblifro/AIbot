from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import TasksCallbackFactory, ThemeCallbackFactory
themes = [
    'условия', "циклы", "арифметика", "списки", "словари", "работа со стороками", "функции", "ООП", "рандомная тема"
]
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

def theme_menu(selected=[]):
    markup = InlineKeyboardBuilder()

    for theme in themes:
        theme_text = theme
        
        if theme in selected:
            theme_text += ' ❌'
        markup.button(text = theme_text , callback_data=ThemeCallbackFactory(theme=theme , is_continue=False))
        
    markup.adjust(2)
    markup.button(text = "дальше⏩", callback_data=ThemeCallbackFactory(theme = '', is_continue=True))
    return markup.as_markup()