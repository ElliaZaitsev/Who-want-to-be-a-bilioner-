from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram import F,Router

from keyboard.button import wiebuchstabiert, wiebuchstabiert4


class userstate(StatesGroup):
    menu=State()
    bezriznyci=State()
zminna=Router()
@zminna.message(F.text=="/restart keyboard")
async def nazwa(message: Message,state:FSMContext):
    await message.answer("/restart",reply_markup=wiebuchstabiert())
    await state.set_state(userstate.menu)
@zminna.message(F.text == "/?",userstate.menu)
async def nazwa(message: Message,state:FSMContext):
    await message.answer("heh?",reply_markup=wiebuchstabiert4())
    await state.set_state(userstate.bezriznyci)
@zminna.message(F.text=="котики",userstate.bezriznyci)
async def nazwa(message: Message,state:FSMContext):
    await message.answer("котики це теплі пушисті клубочки:)")