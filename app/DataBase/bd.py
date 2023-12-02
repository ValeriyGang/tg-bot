from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text

import os


async_engine = create_async_engine( #Создание соединения
    url=os.environ.get("ASYNCPG2")
    #echo=True, # Просмотр логов и запросов к sql
    #pool_size=5 # Максимальное кол-во соединений
    #max_overflow=10 # Дополнитьльные соединения 
)

sync_engine = create_engine( #Создание соединения
    url=os.environ.get("PSYCOPG2")
    #echo=True, # Просмотр логов и запросов к sql
    #pool_size=5 # Максимальное кол-во соединений
    #max_overflow=10 # Дополнитьльные соединения 
)

with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.first()=}")

#async def get_123():
#    async with async_engine.connect() as conn:
#        res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
#        print(f"{res.first()=}")
