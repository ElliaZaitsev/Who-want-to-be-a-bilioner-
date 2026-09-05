from sys import prefix

from aiogram.filters.callback_data import CallbackData
class Nazwa(CallbackData,prefix="Nazwa"):
    id: int
    level: int=0

class Click(CallbackData,prefix="nowNazwa"):
    number: int