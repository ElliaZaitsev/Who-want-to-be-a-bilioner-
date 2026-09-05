import asyncio
import logging
import random
import sys

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.util import await_only

from call_back_data import Nazwa, Click
from data_base.engine import session_maker, create_db
from data_base.queries_orm import add_category, zapyt, getallcategories, deletecategory, getcategorybyname, addtowar, \
    gettowarbyname, gettowarbycategory, adduser, checkuserbyname, updatebalance, \
    updatebalance20v, user_historybuying, historytime, produkthistoryadd, pokupka, tort, pirozok
from keyboard.button import wiebuchstabiert1, wiebuchstabiert3, wiebuchstabiert6, wiebuchstabiert7, wiebuchstabiert8, \
    wiebuchstabiert9, wiebuchstabiert10, poppyplaytimeco, wiebuchstabiert11, wiebuchstabiert12, wiebuchstabiert13, \
    wiebuchstabiert14, wiebuchstabiert15, wiebuchstabiert16, wiebuchstabiert17, wiebuchstabiert18, wiebuchstabiert19, \
    wiebuchstabiert20
from keyboard.button_enums import Buttons
from profile import profile_router
from datetime import datetime, timezone
import zoneinfo
from sesion import DataBaseSession
from backrooms import back as BACK
print(BACK)
class userstate(StatesGroup):
    Admin=State()
    notmenu=State()
    PRICE=State()
    QUALITY=State()
    category=State()
    deletecategory=State()
    addtowar=State()
    confirm=State()
    PRICE1=State()
    kolbasa=State()
    stan=State()
    balancead=State()
    balanceadforadmin=State()
    balanceadmin=State()
    balanceadforadmin3=State()
    bober3000x=State()
    pokupoczkuend=State()
    historia=State()
message1="https://youtu.be/dQw4w9WgXcQ?si=f1y5X5TE1mSXfeHH"
abcd = {}
photos=["https://avatars.mds.yandex.net/i?id=08503b31163da3c2ef3ddf850800f629fec5afbb-10509529-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=a04ea04494abfdff3f0b092bd3a3f9541be29dec-8975527-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=30bac24d38a44b6e315acb40e2e4993f740a5148-6639666-images-thumbs&n=13",
        "https://i.pinimg.com/736x/5f/47/67/5f4767bc1af9ffb95e3c3d8d40886f0c.jpg",
        "https://game-tournaments.com/media/news/n42528.jpeg",
        "https://yt3.googleusercontent.com/1tjfSQs7DpW-Oa6-YAcJn2Wqav6NE__e2yhJADL4pK6WY3w4RJ76xqfE3-hYtI6FnO-_RrrddPM=s900-c-k-c0x00ffffff-no-rj"]
so_cute=["Хом'яки можуть набивати защічні мішки їжею настільки сильно, що їхня голова збільшується втричі. У разі небезпеки вони ховають у щоки навіть власних дітей, щоб перенести їх у безпечне місц",
         "Ці тваринки вміють плавати, використовуючи свої щоки як поплавці, набираючи в них повітря.",
         "Хом'яки — справжні майстри складів. У дикій природі вони можуть запасати до 90 кілограмів корму.",
         "У хом'яків 16 зубів, які не мають коренів і ростуть протягом усього життя. Тому їм необхідно гризти тверду їжу, щоб їх сточувати.",
         "Вдень вони ховаються в норах, а вночі стають дуже активними. Активність зазвичай починається близько 8 години вечора.",
         "Зір у хом'яків поганий, і вони не розрізняють кольори, але мають чудовий нюх і слух.",
         "Під час сплячки серцебиття хом'яка знижується з 400 до 4 ударів на хвилину. "]
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8351757093:AAFdHp-42aCOWBaiYKA9Z5LA3AcChvN6_t8"
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.message.middleware(DataBaseSession(session_maker))
dp.include_routers(profile_router)
@dp.message(F.text==f"Корзина покупок🛒")
async def korzyna(message: Message,state:FSMContext):
    data = await state.get_data()
    korzyna = data.get("korzyna", 0)
    spysok=data.get("spysok")
    msd = 0
    bobrinator=""
    for i in spysok:
        bobrinator+=f"{i["name"]} {i["price"]}\n"
        msd+=i["price"]


    await message.answer(bobrinator)
    await message.answer(f"сумма товарів вашої корзини рівна: {msd}")
    await message.answer(f"ваша корзина {korzyna}",reply_markup=wiebuchstabiert13())
    await state.update_data(summma=msd)
    data =await state.get_data()
    print(data)
    await state.set_state(userstate.pokupoczkuend)
@dp.message(F.text=="завершити покупочоки🛍️🛒",userstate.pokupoczkuend)
async def pokupoczku(message: Message,state:FSMContext):
    data = await state.get_data()
    print(data)
    summa3=data.get("summma")
    spysok=data.get("spysok")
    await message.answer(f"ви завершили покупочки,ви витратили {summa3} грошей",reply_markup=wiebuchstabiert9())
    async with session_maker() as session:
       chos= await updatebalance20v(telegram_id=message.from_user.id,session=session,price=summa3)
       chupakabryk=await user_historybuying(session=session,telegram_id=message.from_user.id,price=summa3,name="вкусняшка",time=datetime.now(timezone.utc))
       for i in spysok:
           await produkthistoryadd(session=session,name=i["name"],price=i["price"],uh_id=chupakabryk)
    await state.set_state(userstate.notmenu)
@dp.message(F.text==BACK,userstate.balancead)
@dp.message(CommandStart())
async def command_start_handler(message: Message,state) -> None:
    async with session_maker() as session:
        meow=await checkuserbyname(session,telegram_id=message.from_user.id)
        if not meow:
            async with session_maker() as session:
                await adduser(session,name=message.from_user.full_name,balance=0,telegram_id=message.from_user.id)
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",reply_markup=wiebuchstabiert9())
    await state.set_state(userstate.notmenu)
@dp.message(Command("Admin"),F.from_user.id.in_({78561589591}))
async def ADMINISTRATORE(message: Message):
    await message.answer("/give me 1000000$")
@dp.message(F.text.lower().in_({"здарова","пр","а салам молейкум","дратуте","i never going to give you up","|||","...___..."}))
async  def f(message: Message):
    await message.answer("дратути")
@dp.message(Command("коржик"))
async def clicker(message: Message):
    number=abcd.get(message.from_user.id,0)

    await message.answer(f"кількість кліків {number}",reply_markup=wiebuchstabiert20(number=number))
@dp.callback_query(Click.filter())
async def newarzlywa(callback: CallbackQuery,callback_data:Click):
    global abcd
    clicker_number=0
    abcd[callback.from_user.id]=callback_data.number
    await callback.message.edit_text(text=f"кількість кліків {callback_data.number}",reply_markup=wiebuchstabiert20(number=callback_data.number))



@dp.message(F.photo)
async def paparacji(message: Message):
    print(message.photo[-1])
    print(message.photo[0])
    await message.answer("моцно")
@dp.message(F.text=="photo")
async def notpaparacji(message: Message):
    await message.bot.send_chat_action(chat_id=message.chat.id,action=ChatAction.UPLOAD_DOCUMENT)
    a=random.choice(photos)
    await message.answer_photo(photo=a,caption="лови імбулічку")
@dp.message(F.text=="ааа")
async def aaa(message: Message):
    await message.answer("шо а?")
@dp.message(F.text == "а то а")
async def a_to_a(message: Message):
    await message.reply("ого ти прям жоский",reply_markup=wiebuchstabiert1())
@dp.message(F.text == "гарбузик")
async def garbyzik(message: Message):
    await message.answer("ох як же я люблю гарбузики😋!!!")
@dp.message(F.text == "хом'ячок")
async def garbyzik(message: Message):
    await message.answer("які ж хом'ячки милііііііі!🥰",reply_markup=wiebuchstabiert3())
@dp.message(F.text=="цікаві факти про хом'ячків")
async def facts_for_xomiachki(message: Message):
    b=random.choice(so_cute)
    await message.answer(text=b,caption="цікавий факт про хом'ячків👆")
@dp.message(F.text == Buttons.pelmen)
async def pelemen(message: Message):
    await message.answer("😎😎🥳🤫😋😋")


        # a=FSInputFile(r"C:\Users\HP\Desktop\f5844584c2b8f5af6459086790954eab.jpg")
    # await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=08503b31163da3c2ef3ddf850800f629fec5afbb-10509529-images-thumbs&n=13")
    # await message.answer_photo(photo="AgACAgQAAxkDAAICWWl9yy-Ip51DeYGQCyUI_mzTh-5RAAJnDWsbfNb0U7S3Dj-Aus2WAQADAgADeAADOAQ")
@dp.message(F.text==BACK,userstate.addtowar)
@dp.message(Command("Admin"), F.from_user.id.in_({7856158959}),)
async def ADMINISTRATORE(message: Message,state:FSMContext):
    await message.answer(
        "Ви зайшли в "
        "<u><b><i>ADMIN</i></b></u> :)",disable_web_page_preview=True,
        parse_mode="HTML"
    ,reply_markup=wiebuchstabiert6())
    await state.set_state(userstate.Admin)

@dp.message(Command("usemoneyprinter"))
async def moneyprinter3000x(message: Message):
    await message.answer(f"перейдіть по посиланню👉",reply_markup=wiebuchstabiert18())

@dp.message(Command("message"), F.from_user.id.in_({7856158959}))
async def ADMINISTRATORE(message: Message):
    await message.answer(
        "You don't have"
        " <u><b><i>V.I.P</i></b></u> :(",disable_web_page_preview=True,
        parse_mode="HTML"
    )

@dp.message(F.text == "Додати інвентар🎒",userstate.Admin)
async def garbyzik(message: Message,state:FSMContext):
    await message.answer("дайте назву інвентарю",reply_markup=wiebuchstabiert3())
    await state.set_state(userstate.notmenu)
# @dp.message(F.text!="",userstate.notmenu)
# async def menunot(message: Message,state:FSMContext):
#     name=message.text
#     await state.update_data(name=name)
#     await message.answer("Введіть ціну")
#     await state.set_state(userstate.PRICE)
@dp.message(userstate.PRICE)
@dp.message(userstate.PRICE)
# @dp.message(F.text,userstate.notmenu)
async def qualitys(message: Message,state:FSMContext):
    name=message.text
    await state.update_data(price=name)
    await message.answer("Введіть якість товару")
    await state.set_state(userstate.QUALITY)
@dp.message(F.text,userstate.QUALITY)
async def good(message: Message,state:FSMContext):
    await message.answer("Успіх!   ^_____^   ",reply_markup=wiebuchstabiert6())
    qua=message.text
    await state.update_data(quality=qua)
    data=await state.get_data()
    print(data)
    async with session_maker() as session:
        await add_category(session=session, name=data.get("name"), quality=data.get("quality"), category1="category", price=int(data.get("price")))
    await state.set_state(userstate.Admin)
@dp.message(F.text=="подивитись інвентар📰")
async def invenratito(message: Message,state:FSMContext):
    await message.answer("список вашого інвентаря кря :3")
    async with session_maker() as session:
        zminnaa=await zapyt(session=session)
        text=""
        for zmin in zminnaa:
            text+=zmin.name+"\n"
        await message.answer(text)
@dp.message(F.text=="перейти до покупок")
async def marketplace(message: Message,state:FSMContext):
    await state.set_state(userstate.notmenu)
    await message.answer("виберіть категорію",reply_markup=wiebuchstabiert7())
@dp.message(F.text=="додати категорію🎫",userstate.Admin)
async def addcategorycommand(message: Message,state:FSMContext):
    await state.set_state(userstate.category)
    await message.answer("введіть назву категорії")

@dp.message(userstate.category)
async def categoryreaction(message: Message,state:FSMContext):
    await message.answer("нова категорія була встановлена:)",reply_markup=wiebuchstabiert6())
    async with session_maker() as session:
        await zapyt(session,message.text)
    await state.set_state(userstate.Admin)
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await create_db()
    # And the run events dispatching
    await dp.start_polling(bot)
@dp.message(F.text=="подивитись категорію📋",userstate.notmenu)
async def pregladcategorii(message: Message,state:FSMContext,session):
    # async with session_maker() as session:
    bober= await getallcategories(session)
    await message.answer("виберіть категорію:)",reply_markup=wiebuchstabiert8(bober))
@dp.message(F.text=="видалити категорію🗑️",userstate.Admin)
async def deletecategory1(message: Message,state:FSMContext):
    async with session_maker() as session:
        bober= await getallcategories(session)
    await message.answer("виберіть категорію яку ви хочете видалити",reply_markup=wiebuchstabiert8(bober))
    await state.set_state(userstate.deletecategory)
@dp.message(userstate.deletecategory)
async def deleter(message: Message,state:FSMContext):
    async with session_maker() as session:
        await deletecategory(session,message.text)
        await message.answer("ви успішно видалили категорію",reply_markup=wiebuchstabiert6())
        await state.set_state(userstate.Admin)
@dp.message(F.text=="додати товар➕🍖",userstate.Admin)
async def dodatytowar(message: Message,state:FSMContext):
    async with session_maker() as session:
        bober= await getallcategories(session)
    await message.answer("виберіть категорію товару який ви хочете додати",reply_markup=wiebuchstabiert8(bober))
    await state.set_state(userstate.addtowar)
@dp.message(userstate.addtowar)
async def dodatytowar2(message: Message,state:FSMContext):
    async with session_maker() as session:
        A=await getcategorybyname(session,message.text)
    if A:
        await message.answer("введіть назву товару",reply_markup=poppyplaytimeco())
        await state.update_data(category_id=A.id)

        await state.set_state(userstate.PRICE1)

    else:
        await message.answer("ви ввели некоректну категорію")
@dp.message(userstate.PRICE1)
async def price(message: Message,state:FSMContext):
    async with session_maker() as session:
        towar = await gettowarbyname(name=message.text,session=session)
    if towar:
        await message.answer("такого товару не існує!")
    else:
        await message.answer("введіть ціну товару")
        await state.update_data(towar_name=message.text)
        await state.set_state(userstate.confirm)
@dp.message(F.text=="ТААААКК😎😁😋😏🫠🤭🥳!!!")
async def bulbul(message: Message,state:FSMContext):
    await message.answer("УРАААА :DDDD!!! ви додали товар XDDDDD з вас 150000000$:) ...")
    await state.set_state(userstate.Admin)
    data=await state.get_data()
    category=data.get("category_id")
    towar_name=data.get("towar_name")
    towar_price = data.get("towar_price")
    async with session_maker() as session:
        await addtowar(session,price=int(towar_price),category=category,name=towar_name)
    await message.answer(towar_name+towar_price,reply_markup=wiebuchstabiert6())
@dp.message(F.text=="ні💀🤢🤬😡😵‍💫🥴🥶👿....",)
async def kaszpak(message: Message,state:FSMContext):
    await message.answer("тобі капець....🤭🤭🤭EHEHHEHEHAHAIAHIAAAHIAHAHHEHEH")
    await state.set_state(userstate.Admin)
@dp.message(userstate.confirm)
async def idk(message: Message,state:FSMContext):
    if message.text.isdigit():
        if int(message.text)<=2000000000:
            await message.answer("пропуск sehr gut:D")
            await message.answer("чи ви впевнені що хочете додати товар??????????????",reply_markup=wiebuchstabiert10())
            await state.update_data(towar_price=message.text)
        else:
            await message.answer("ах ти ПЕЛЬМЕЕНЬ!!!😡😡😡")
    else:
        await message.answer("ах ти ПЕЛЬМЕЕНЬ!!!😡😡😡")
@dp.message(F.text=="Каталог🧾")
@dp.message(F.text==BACK,userstate.stan)
async def krakivskakolbosa(message: Message,state:FSMContext):
    async with session_maker() as session:
        category = await getallcategories(session)
        await message.answer("Ковбаса закінчилась:(",reply_markup=wiebuchstabiert8(category))
        await state.set_state(userstate.kolbasa)
@dp.message(F.text==BACK,userstate.kolbasa)
async def Zdzblo(message: Message,state:FSMContext):
    await message.answer("ви в головному меню",reply_markup=wiebuchstabiert9())
    await state.clear()
    await state.set_state(None)
@dp.message(F.text,userstate.kolbasa)
async def Zdzblo(message: Message,state:FSMContext):
    await message.answer("я стомився від польши:(")
    async with session_maker() as session:
        JAZABUW = 1
        absolute_cinema = await getcategorybyname(session, message.text)
    if absolute_cinema:
        text="ваші товари\n"
        await message.answer("така категорія є!!!!!!!")
        async with session_maker() as session:
            bobrichkin=await gettowarbycategory(session,absolute_cinema.id)
            await state.update_data(category_id=absolute_cinema.id)


            # for towar in bobrichkin:
                # text+=str(JAZABUW)+". "+towar.name+"\n"
                # text+=f"{JAZABUW}. {towar.name}\n"
                # JAZABUW+=1
            for slowo, towar in enumerate (bobrichkin,start=1):
                text+=f"{slowo}. {towar.name}\n"

            await message.answer(text,reply_markup=wiebuchstabiert11(bobrichkin))
        await state.set_state(userstate.stan)
    else:
        await message.answer("неа не ма такого")
@dp.message(F.text,userstate.stan)
async def enchuldigurkatzemahoradie(message: Message,state:FSMContext):
    async with session_maker() as session:
        o = await gettowarbyname(name=message.text,session=session)
    text=f"назва товару:🪧 {o.name} \nціна:💵 {o.price}"
    towarinfo={"name":o.name,"price":o.price}
    data = await state.get_data()
    spysok = data.get("spysok", [])
    spysok.append(towarinfo)
    await state.update_data(spysok=spysok)
    await message.answer(text,reply_markup=wiebuchstabiert12())
    await state.set_state(userstate.bober3000x)
@dp.message(F.text=="додати до корзини")
async def korzyna2(message: Message,state:FSMContext):
    data=await state.get_data()
    spysok=data.get("spysok",[])


    categoryid=data.get("category_id")
    async with session_maker() as session:
        bobrichkin = await gettowarbycategory(session, categoryid)
        await state.update_data(category_id=categoryid)
        text=""
        # for towar in bobrichkin:
        # text+=str(JAZABUW)+". "+towar.name+"\n"
        # text+=f"{JAZABUW}. {towar.name}\n"
        # JAZABUW+=1
        for slowo, towar in enumerate(bobrichkin, start=1):
            text += f"{slowo}. {towar.name}\n"

        await message.answer(text, reply_markup=wiebuchstabiert11(bobrichkin))

        data = await state.get_data()
        korzyna = data.get("korzyna", 0)
        korzyna += 1
        await state.update_data(korzyna=korzyna)
    await state.set_state(userstate.stan)
@dp.message(F.text=="поповнення баланса💰")
async def bobrik(message: Message,state:FSMContext):
    await message.answer("введіть кілкість грошей яких ви хочете поповнити",reply_markup=wiebuchstabiert15())
    await state.set_state(userstate.balancead)

@dp.message(F.text,userstate.balancead)
async def balance(message: Message,state:FSMContext):
    if message.text.isdigit():
        await message.answer("ваша заявка подана адміністрації на розглядання",reply_markup=wiebuchstabiert9())
        await message.bot.send_message(chat_id=7856158959,text=f"користувач {message.from_user.id} хоче поповнити баланс на {message.text}")
        await state.set_state(userstate.notmenu)
    else:
        await message.answer("я подам на вас негатавний отзив я посталвю вам 1 зірочку і я забаню вас на сервері планета вам капець")
@dp.message(F.text=="поповнення баланса для Адміністратора💰💸")
async def balanceadmin(message: Message,state:FSMContext):
    await state.set_state(userstate.balanceadforadmin)
    await message.answer("введіть ID користувача якому ви хочете поповнити баланс")
@dp.message(F.text,userstate.balanceadforadmin)
async def balanceforadmin(message: Message,state:FSMContext):
    if message.text.isdigit():
        await state.set_state(userstate.balanceadforadmin3)
        await state.update_data(telegram_id=message.text)
        await message.answer("введіть суму грошей яку ви хочете поповнити")
    else:
        await message.answer("не існує данного id")
@dp.message(F.text,userstate.balanceadforadmin3)
async def balanceforadmin2(message: Message,state:FSMContext):
    data=await state.get_data()
    telegram_id=data.get("telegram_id")
    if message.text.isdigit():
        await state.set_state(userstate.balanceadmin)
        async with session_maker() as session:
            await updatebalance(session=session,telegram_id=int(telegram_id),balance=int(message.text))
            await message.answer("ви успішно поповнили баланс")
    else:
        await message.answer("error")
@dp.message(F.text=="абоба")
async def aboba(message: Message,state:FSMContext):
    async with session_maker() as session:
        history = await historytime(session=session,telegram_id=message.from_user.id)
    await message.answer("абоба",reply_markup=wiebuchstabiert14(history))
    # await message.answer(f"ви додали {i.name} до корзини")
@dp.message(F.text=="історія покупок🖼️")
async def buying_history(message: Message,state:FSMContext):
    await state.set_state(userstate.historia)
    async with session_maker() as session:
        mk16=await historytime(session=session,telegram_id=message.from_user.id)
        await message.answer(text="ваші покупочки",reply_markup=wiebuchstabiert14(mk16))
@dp.message(F.text,userstate.historia)
async def inevergoingtogiveyouup(message: Message, state:FSMContext, towary=None):
    reply_markup = wiebuchstabiert17()
    text=message.text
    try:
        date=datetime.strptime(text,"%d-%m-%Y %H:%M:%S")

    except Exception as e:
        print(e)
        await message.answer("неправиильна дата😡😡😡")
        return
    date=date.replace(tzinfo=zoneinfo.ZoneInfo("Europe/Warsaw"))
    dt_utc = date.astimezone(zoneinfo.ZoneInfo("UTC"))
    print(date)
    print(dt_utc)
    async with session_maker() as session:
        akpukop=await pokupka(session=session,telegram_id=message.from_user.id,time=dt_utc)
        # print(akpukop.price)
        # print(akpukop.id)
        if akpukop:
            abab=f"ви витратили {akpukop.price}"
            await message.answer(abab)
            pokuplist=await tort(session=session,uh_id=akpukop.id)
            # print(len(pokuplist))
            # for towar in pokuplist:
            text = ""
            for towar in pokuplist:

                text += f"{towar.name} - {towar.price}\n"
            await message.answer(text)


        else:
            await message.answer("такої покупки не знайдено")
@dp.message(F.text=="профіль🌐")
async def profile(message: Message,state:FSMContext):
    await  message.answer(text="ваш профіль🌐:",reply_markup=wiebuchstabiert16())
@dp.callback_query(F.data=="сила сметани активована")
async def kapitoshka(callback:CallbackQuery,state:FSMContext):
    await callback.message.edit_text("сила сметани активована", reply_markup=wiebuchstabiert19())
@dp.callback_query(Nazwa.filter())
async def kapitoshka3345789(callback:CallbackQuery,state:FSMContext,callback_data:Nazwa):
    async with session_maker() as session:
        pirozok20=await pirozok(session=session,id=callback_data.id)
        if pirozok20:
            await callback.message.edit_text(text=f"{pirozok20.name}", reply_markup=wiebuchstabiert19())
        else:
            await callback.message.edit_text(text=f"я не буду писати текст🤬💢 {callback_data.id}", reply_markup=wiebuchstabiert19())
@dp.callback_query()
async def kapitoshka(callback:CallbackQuery,state:FSMContext):
    await callback.answer()
    if callback.data=="пельмені":
        await callback.message.answer("якийсь текст в лапках")
    elif callback.data=="mktartk":
        await callback.message.answer("капітошка")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())