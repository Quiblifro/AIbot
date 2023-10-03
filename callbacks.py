from typing import Optional
from aiogram.filters.callback_data import CallbackData

class CallbackFactory(CallbackData, prefix="task"):
    action: str