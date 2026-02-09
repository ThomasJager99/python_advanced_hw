# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
#
# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
#
# Задача 3: Определите модель продукта Product со следующими типами колонок:
#
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# price: числовое значение с фиксированной точностью
# in_stock: логическое значение


# Задача 4: Определите связанную модель категории Category со следующими типами колонок:
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# description: строка (макс. 255 символов)
# Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.

#=================== Imports ===================
from decimal import Decimal
from sqlalchemy import (create_engine,
                        Numeric ,
                        BigInteger,
                        Column,
                        String,
                        SmallInteger,
                        Boolean,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import (sessionmaker,
                            DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)
from pathlib import Path
import sqlite3

#=================== Imports ===================

#1.Create engine exemplar for SQLite db connection.

engine = create_engine(
    url=f"sqlite:///:memory:", echo=True
)

#2. Creating Session for connection via engine to db

Session = sessionmaker(bind=engine)

session = Session()

#3.Create product model 'Product'

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        #SmallInteger,
        Integer,
        index=True,
        nullable=False,
        #unique=True,
        primary_key=True,
        #autoincrement=True
    )


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] =  mapped_column(
        String(35),
        nullable=False,
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric,
        nullable=False
    )
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("category.id"),
        nullable=False
    )

    in_stock: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    category = relationship("Category", back_populates="products")

#4.Create Category table:

class Category(Base):
    __tablename__ = 'category'

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    products = relationship("Product", back_populates="category")


Base.metadata.create_all(bind=engine)


cat = Category(
    name="Electro",
    description="Tech stuff"
)
session.add(cat)
session.commit()

product = Product(
    name="Laptop",
    price=Decimal("999.99"),
    category_id=cat.id,
    in_stock=True
)

session.add(product)
session.commit()

p = session.query(Product).first()
print(p.category_id)












