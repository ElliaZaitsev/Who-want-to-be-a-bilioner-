from sqlalchemy import select, delete

from data_base.engine import session_maker
from data_base.models import Animals, Cars, inventory, category, towar, user_balance, user_history, produkthistory

from datetime import timedelta
async def add_animal(session,name,vik,location):
    jakas_zminna=Animals(Name=name,age=vik,location=location)
    session.add(jakas_zminna)
    await session.commit()
async def getallanimals(session):
    aaaa=select(Animals)
    result = await session.execute(aaaa)
    return result.scalars().all()
async def getanimal(session,name):
    aaaa=select(Animals).where(Animals.Name==name)
    result = await session.execute(aaaa)
    return result.scalars().all()
    # return result.scalar_one_or_none()
async def add_cars(session,Model,characteristic,Color,Hp,data):
    jakas_zminna1=Cars(Model=Model,characteristic=characteristic,Color=Color,Hp=Hp,Rd=data)
    session.add(jakas_zminna1)
    await session.commit()
async def add_category(session,name,price,quality,category1=None,category2=None,category3=None,category4=None):
    A=inventory(name=name,price=price,quality=quality,category1=category1,category2=category2,category3=category3,category4=category4)
    session.add(A)
    await session.commit()
async def zapyt(session,name):
    PASS=category(name=name)
    session.add(PASS)
    await session.commit()
async def getallcategories(session):
    aaaa = select(category)
    result = await session.execute(aaaa)
    return result.scalars().all()
async def deletecategory(session,name):
    A=delete(category).where(category.name==name)
    await session.execute(A)
    await session.commit()
async def getcategorybyname(session,name):
    aaaaaaaaaaaa=select(category).where(category.name==name)
    result = await session.execute(aaaaaaaaaaaa)
    return result.scalar_one_or_none()
async def addtowar(session,name,price,category):
    AAAAAAAAAAAAA=towar(category=category,price=price,name=name,quality="якийсь текст будь який")
    session.add(AAAAAAAAAAAAA)
    await session.commit()
async def ytn(session):
    bobbobriwich = select(towar)
    result = await session.execute(bobbobriwich)
    return result.scalars().all()
async def gettowarbyname(session,name):
    GTAV=select(towar).where(towar.name==name)
    result = await session.execute(GTAV)
    return result.scalar_one_or_none()
async def gettowarbycategory(session,categoryid):
    aaaaaaaaaaaa = select(towar).where(towar.category == categoryid)
    result = await session.execute(aaaaaaaaaaaa)
    return result.scalars().all()
async def checkuserbyname(session,telegram_id):
    GTAIV = select(user_balance).where(user_balance.telegram_id == telegram_id)
    result = await session.execute(GTAIV)
    return result.scalar_one_or_none()
async def adduser(session,name,balance,telegram_id):
    userad=user_balance(balance=balance,telegram_id=telegram_id,name=name)
    session.add(userad)
    await session.commit()
async def find_userbytelegramid(session,telegram_id):
    terminator3000x = select(user_balance).where(user_balance.telegram_id == telegram_id)
    result = await session.execute(terminator3000x)
    return result.scalar_one_or_none()
async def updatebalance(session,telegram_id,balance):
    user = await find_userbytelegramid(session=session,telegram_id=telegram_id)
    if user:
        user.balance+=balance
        await session.commit()
async def updatebalance20v(session,telegram_id,price):
    user = await find_userbytelegramid(session=session, telegram_id=telegram_id)
    if user:
        user.balance-=price
        await session.commit()
async def user_historybuying(session,telegram_id,price,name,time):
    historybuying=user_history(telegram_id=telegram_id,price=price,name=name,time=time)
    session.add(historybuying)
    await session.commit()
    await session.refresh(historybuying)
    return historybuying.id
async def pokupka(session,telegram_id,time):
    kompot=(select(user_history)
    .where(user_history.telegram_id==telegram_id,user_history.time.between(time,time + timedelta(seconds=1)))
            .order_by(user_history.time.desc()))
    result = await session.execute(kompot)
    return result.scalar_one_or_none()
async def historytime(session,telegram_id):
    kompot=select(user_history).where(user_history.telegram_id==telegram_id).order_by(user_history.time.desc())
    result = await session.execute(kompot)
    return result.scalars().all()
async def produkthistoryadd(session,name,price,uh_id):
    addprodukthistory=produkthistory(name=name,price=price,counter=1,uh_id=uh_id)
    session.add(addprodukthistory)
    await session.commit()
async def tort(session,uh_id):
    agent_tort=select(produkthistory).where(produkthistory.uh_id==uh_id)
    result = await session.execute(agent_tort)
    return result.scalars().all()
async def pirozok(session,id):
    pirozok2=select(towar).where(towar.id==id)
    result = await session.execute(pirozok2)
    return result.scalar_one_or_none()
async def NOOOOOOOOOOOOOOOOOOOO(session,price):
    ni=select(user_history).where(user_history.price>price)
    result = await session.execute(ni)
    return len(result.scalars().all())
