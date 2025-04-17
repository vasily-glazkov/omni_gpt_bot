from app.database.models import async_session
from app.database.models import User, AiType, AiModel, Order
from sqlalchemy import select, update, delete, desc
from decimal import Decimal


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, balance='0'))
            await session.commit()


async def get_user(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))


async def calculate(tg_id, summ, model_name):
    async with async_session() as session:
        try:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            model = await session.scalar(select(AiModel).where(AiModel.name == model_name))
            print('SUMM', summ)
            new_balance = Decimal(Decimal(user.balance) - Decimal(Decimal(model.price) * Decimal(summ)))
            print('NEW BALANCE ==>', new_balance)
            await session.execute(update(User).where(User.id == user.id).values(balance=str(new_balance)))
            await session.commit()
        except Exception as e:
            await  session.rollback()
            print('Error: ', e)
