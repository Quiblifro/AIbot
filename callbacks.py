from aiogram.filters.callback_data import CallbackData

class TasksCallbackFactory(CallbackData, prefix="task"):
    action: str

class ThemeCallbackFactory(CallbackData, prefix="theme"):
    theme : str 
    is_continue : bool