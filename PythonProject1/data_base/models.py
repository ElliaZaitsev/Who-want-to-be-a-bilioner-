from datetime import datetime

from sqlalchemy import String, Integer, Boolean, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
class Base(DeclarativeBase):
    pass
class Animals(Base):
    __tablename__ = "Notanimals"
    Name:Mapped[str]=mapped_column(
        String(50), nullable=False,)
    age:Mapped[int]=mapped_column(
        Integer, nullable=False,)
    location:Mapped[str]=mapped_column(
        String, nullable=True,)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
class Base(DeclarativeBase):
    pass
class Cars(Base):
    __tablename__ = "Automodels"
    Model:Mapped[str]=mapped_column(
        String(50), nullable=False,)
    characteristic:Mapped[str]=mapped_column(
        String, nullable=False,)
    Color:Mapped[str]=mapped_column(
        String, nullable=False,)
    Hp: Mapped[int] = mapped_column(
        Integer, nullable = False,)
    Rd:Mapped[int]=mapped_column(
        Integer, nullable=False,)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

class inventory(Base):
    __tablename__ = "Your_inventory"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), nullable=False, )
    category1: Mapped[str] = mapped_column(
        String(250), nullable=True, )
    category2: Mapped[str] = mapped_column(
        String(250), nullable=True, )
    category3: Mapped[str] = mapped_column(
        String(250), nullable=True, )
    category4: Mapped[str] = mapped_column(
        String(250), nullable=True, )
    price: Mapped[int] = mapped_column(
        Integer, nullable=False, )
    quality: Mapped[str] = mapped_column(
        String(100), nullable=False, )
class category(Base):
    __tablename__ = "My_category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), nullable=False, )
    status:Mapped[bool] = mapped_column(Boolean,default=True)
class towar(Base):
    __tablename__ = "towar"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), nullable=False, )
    category: Mapped[int] = mapped_column(
        Integer, nullable=True, )
    price: Mapped[int] = mapped_column(
        Integer, nullable=False, )
    quality: Mapped[str] = mapped_column(
        String(100), nullable=False, )
class user_balance(Base):
    __tablename__ = "balance"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), nullable=False, )
    balance: Mapped[int]=mapped_column(Integer)
    telegram_id: Mapped[int]=mapped_column(BigInteger)
class user_history(Base):
    __tablename__ = "user_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[str] = mapped_column(
        BigInteger, nullable=False, )
    name: Mapped[str] = mapped_column(
        String(50), nullable=False, )
    price: Mapped[int] = mapped_column(Integer)
    time: Mapped[datetime] = mapped_column(
    DateTime(timezone=True))
class produkthistory(Base):
    __tablename__ = "ępródUKcjąŁ"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(500), nullable=False, )
    price: Mapped[int] = mapped_column(Integer)
    counter: Mapped[int] = mapped_column(Integer)
    uh_id: Mapped[int] = mapped_column(
    ForeignKey("user_history.id")
    )
