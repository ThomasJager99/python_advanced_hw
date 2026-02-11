from decimal import Decimal
from sqlalchemy import (create_engine,
                        Numeric ,
                        BigInteger,
                        Column,
                        String,
                        SmallInteger,
                        Boolean,
                        Integer,
                        ForeignKey,
                        UniqueConstraint)
from sqlalchemy.orm import (sessionmaker,
                            DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)
import json
#from models import MineralOutput
from pathlib import Path


#=== Tasks ===
#DONE: schemas.py
# 1. ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
# Создать модель минерала для системы управления поставками драгоценных камней.
# ТРЕБОВАНИЯ:
# - Уникальный идентификатор (BigInteger, автоинкремент)
# - Название минерала (строка, максимум 50 символов, уникальное)
# - Цвет минерала (строка, максимум 30 символов)
# - Твердость по шкале Мооса (число с плавающей точкой)
# ЦЕЛЬ: Создать основу для каталога минералов, которые будут поставляться в салоны.

#DONE:
# 2. models.py
# ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
# Создать Pydantic схему для безопасного вывода информации о минералах в API.
# ТРЕБОВАНИЯ:
# - Валидация всех полей модели Mineral
# - Поддержка сериализации из SQLAlchemy объектов
# - Готовность к использованию в FastAPI/Flask endpoints
# ЦЕЛЬ: Обеспечить типобезопасность и валидацию при передаче данных о минералах
#DONE: Import pydantic validation from another module


#DONE: schemas.py
# 3. ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
# Создать модель салона для системы управления сетью элитных бутиков.
# ТРЕБОВАНИЯ:
# - Уникальный идентификатор
# - Название салона (строка, максимум 50 символов)
# - Местоположение салона (строка, максимум 100 символов)
# - Ограничение уникальности: комбинация (название + местоположение) должна быть уникальной
# ЦЕЛЬ: Создать систему управления салонами, куда будут доставляться минералы.

#TODO: models.py
# 4.ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
# Создать комплексную Pydantic схему для вывода информации о салоне с его поставками.
# ТРЕБОВАНИЯ:
# - Основная информация о салоне (id, название, местоположение)
# - Список поставок с краткой информацией (id, дата, пункт назначения)
# - Вложенная структура данных для удобства API
# ЦЕЛЬ: Предоставить полную информацию о салоне и его поставках в одном запросе.

#=== Tasks ===

#DONE: Task 1

BASE_DIR = Path(__file__).absolute().parent

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        index=True
    )


class Mineral(Base):
    __tablename__ = 'minerals'

    name: Mapped[str] = mapped_column(
        String[50],
        nullable=False,
    )
    color: Mapped[str] = mapped_column(
        String[30],
        nullable=False
    )
    solid: Mapped[Decimal] = mapped_column(
        Numeric(4,2),
        nullable=False
    )

engine = create_engine(f"sqlite:///{BASE_DIR/'minerals.db'}")



#DONE: Task 3

class Salon(Base):
    __tablename__ = 'salon'

    name: Mapped[str] = mapped_column(
        String[50],
        nullable=False
    )
    location: Mapped[str] = mapped_column(
        String[100],
        nullable=False
    )
    __table_args__ = (
        UniqueConstraint("name", "location", name="uix_name_location"),
    )

Base.metadata.create_all(bind=engine)


