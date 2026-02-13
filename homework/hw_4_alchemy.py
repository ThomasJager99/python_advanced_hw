#part ============= IMPORTS =============
from decimal import Decimal
import pymysql
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
from my_db_connector import engine

#part ============= IMPORTS =============











