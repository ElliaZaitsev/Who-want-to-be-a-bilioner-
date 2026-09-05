import random
from multiprocessing.context import BufferTooShort
from zoneinfo import ZoneInfo

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from pyexpat.errors import messages

from call_back_data import Nazwa, Click
from keyboard.button_enums import Buttons, xomiachky
from backrooms import back


def wiebuchstabiert():
    B=KeyboardButton(text="ааа")
    b = KeyboardButton(text="а то а")
    first_row=[B]
    markup = ReplyKeyboardMarkup(
        keyboard=[first_row,[b]],resize_keyboard=True)
    return markup
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
def wiebuchstabiert1():
    A=ReplyKeyboardBuilder()
    A.button(text="гарбузик")
    A.button(text="хом'ячок")
    A.button(text=Buttons.pelmen)
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert2():
    A=ReplyKeyboardBuilder()
    A.button(text=Buttons.otwarzno)
    A.button(text=Buttons.xomiachok)
    A.button(text=Buttons.rzorik)
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert3():
    A=ReplyKeyboardBuilder()
    for B in xomiachky:
        A.button(text=B)
        A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert4():
    A = ReplyKeyboardBuilder()
    A.button(text="котики")
    A.button(text="простоквашено")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert5():
    A=ReplyKeyboardBuilder()
    A.button(text="Магазин🏠")
    A.button(text="Інвентар🎒")
    A.button(text="Наші контакти☎️")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert6():
    A = ReplyKeyboardBuilder()
    A.button(text="Додати інвентар🎒",style="success")
    A.button(text="подивитись інвентар📰",style="primary")
    A.button(text="додати категорію🎫",style="success")
    A.button(text="поповнення баланса для Адміністратора💰💸",style="primary")
    A.button(text="додати товар➕🍖",style="success")
    A.button(text="історія покупок🖼️",style="primary")
    A.button(text="видалити категорію🗑️",style="danger")
    A.button(text=back,style="primary")
    A.button(text="профіль🌐",style="primary")
    A.button(text="Каталог🧾",style="primary")
    A.button(text="ні")
    return A.adjust(2).as_markup(resize_keyboard=True)
def wiebuchstabiert7():
    A=ReplyKeyboardBuilder()
    A.button(text="test1")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert8(category):
    A=ReplyKeyboardBuilder()
    A.button(text=f"Корзина покупок🛒")
    for i in category:
        A.button(text=i.name)
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert9():
    A=ReplyKeyboardBuilder()
    A.button(text="Корзина покупок🛒")
    A.button(text="подивитись категорію📋")
    A.button(text="Каталог🧾")
    A.button(text=back)
    A.button(text="поповнення баланса💰")
    A.button(text="історія покупок🖼️")
    A.button(text="профіль🌐")
    return A.adjust(2).as_markup(resize_keyboard=True)
def wiebuchstabiert10():
    A=ReplyKeyboardBuilder()
    A.button(text="ТААААКК😎😁😋😏🫠🤭🥳!!!",style="success")
    A.button(text="ні💀🤢🤬😡😵‍💫🥴🥶👿....",style="danger")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def poppyplaytimeco():
    A=ReplyKeyboardBuilder()
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert11(name):
    A=ReplyKeyboardBuilder()
    for i in name:
        A.button(text=i.name,style="primary")
    A.button(text=back)
    A.button(text="Корзина покупок🛒")
    return A.adjust(2).as_markup(resize_keyboard=True)
def wiebuchstabiert12():
    A=ReplyKeyboardBuilder()
    A.button(text="додати до корзини")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert13():
    A=ReplyKeyboardBuilder()
    A.button(text="завершити покупочоки🛍️🛒")
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert14(price):
        A = ReplyKeyboardBuilder()
        A.button(text=f"Корзина покупок🛒")
        for i in price:
            A.button(text=i.time.astimezone(ZoneInfo("Europe/Warsaw")).strftime("%d-%m-%Y %H:%M:%S"))
        A.button(text=back)
        return A.adjust(4).as_markup(resize_keyboard=True)
def wiebuchstabiert15():
    A=ReplyKeyboardBuilder()
    A.button(text=back)
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert16():
    A=ReplyKeyboardBuilder()
    A.button(text="історія покупок🖼️")
    A.button(text="поповнення баланса💰")
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert17():
    A=ReplyKeyboardBuilder()
    A.button(text="Подивитись товари💎")
    A.button(text="Подивитись кількість товарів🎩")
    return A.adjust(1).as_markup(resize_keyboard=True)
def wiebuchstabiert18():
    A=InlineKeyboardBuilder()
    A.button(text="просто посилання",url="https://youtu.be/QDia3e12czc?si=8sB1Vu8lgAoENr9g")
    A.button(text="ąęąęąęąęąęąęąęąę",callback_data="пельмені")
    A.button(text="lplpsrtkmskefghtm", callback_data="mktartk")
    A.button(text="безкінечні варенички",callback_data="сила сметани активована")
    A.button(text="посилання на fabric_loader",url="https://fabricmc.net/use/installer/?utm_source=chatgpt.com")
    return A.adjust(1).as_markup()
def wiebuchstabiert19():
    A = InlineKeyboardBuilder()
    A.button(text="посилання на fabric_loader",url="https://fabricmc.net/use/installer/?utm_source=chatgpt.com")
    A.button(text="безкінечні пельменьки", callback_data=Nazwa(id=random.randint(1,44)))
    return A.adjust(1).as_markup()
def wiebuchstabiert20(number):
    A=InlineKeyboardBuilder()
    if number!=0:
        A.button(text="-",callback_data=Click(number=number-1))
    A.button(text="+",callback_data=Click(number=number+1))
    A.button(text="скинути",callback_data=Click(number=0))
    return A.adjust(1).as_markup()