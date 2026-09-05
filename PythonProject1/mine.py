import asyncio
import datetime
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from data_base.engine import create_db
from keyboard.button import wiebuchstabiert5


class userstate(StatesGroup):
    menu=State()
    bezriznyci=State()
TOKEN = "8351757093:AAHxljjrTSvumR5MxhNmPLkyqlRaD77iOp0"
dp=Dispatcher()
@dp.message(F.text=="/start")
async def command_start_handler(message: Message,state: FSMContext) -> None:
    await state.set_state(userstate.menu)
    time=datetime.datetime.now().time()
    time2=time.strftime("%H:%M:%S")
    print(time)
    print(time2)
    data = await state.get_data()
    print(data)
    await state.update_data(p2w=time2)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",reply_markup=wiebuchstabiert5())


@dp.message(F.text=="топ лідерів на авторинку",userstate.menu)
async def car_leader(message: Message,state: FSMContext):
    await message.answer("Toyota (Японія): Утримує перше місце, продаючи понад 9-10 млн автомобілів на рік. Найпопулярніші моделі — Toyota RAV4 та Corolla.\n"
                         "Volkswagen Group (Німеччина): Стабільно займає другу позицію.\n"
                         "BYD (Китай): Здійснює найагресивніше зростання, займаючи 3-4 місце у світі та лідируючи в сегменті електромобілів.\n"
                         "Honda (Японія): Стабільно в топі за продажами та надійністю."
                         "Hyundai/Kia (Південна Корея): Тримають високі позиції, активно конкуруючи з японськими та європейськими брендами.\n")
@dp.message(F.text=="історія як з'явились автомобілі",userstate.menu)
async def auto_history(message: Message,state: FSMContext):
    await message.answer("Історія автомобіля розпочалася не в один день, але офіційним днем народження вважається 29 січня 1886 року, коли німецький інженер Карл Бенц запатентував триколісний Motorwagen із бензиновим двигуном внутрішнього згоряння. До цього десятиліттями створювалися парові вози (перший у 1769 р.), а паралельно з Бенцом працювали Готтліб Даймлер та інші винахідники. ")
@dp.message(F.text=="яка машина найшвидша")
async def mfc(message: Message,state: FSMContext):
    data=await state.get_data()
    print(data)
@dp.message(F.text == "Магазин🏠", userstate.menu)
async def shop(message: Message, state: FSMContext):
    await message.answer("***")
@dp.message(F.text == "Інвентар🎒", userstate.menu)
async def inventory(message: Message, state: FSMContext):
    await message.answer("***")
@dp.message(F.text == "Наші контакти☎️", userstate.menu)
async def inventory(message: Message, state: FSMContext):
    await message.answer("наші контакти: breaver05@gmail.com номер: +1 310-867-0051\n"
                         "тех-підтримка: cat@08gmail.com номер:  +1 212-832-2000\n")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await create_db()
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
