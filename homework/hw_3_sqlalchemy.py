#part =================== Imports ===================
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
from my_db_connector import engine
#part =================== Imports ===================

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












