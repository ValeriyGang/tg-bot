from sqlalchemy import create_engine, Column, Integer, VARCHAR, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

metadata_obj = MetaData()
engine = create_engine(os.environ.get("DATABASE_URL"))

# Создание модели данных (класса)
Base = declarative_base()

# Создание таблицы
class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, nullable=True, unique=True)
    nickname = Column(VARCHAR(30), nullable=True)

    def __repr__(self):
        return f'{self.user_id} {self.nickname}'

# Создание таблицы в базе данных
Base.metadata.create_all(engine)

# Создание сеанса SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
