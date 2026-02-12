from sqlalchemy import (create_engine,
                        select)
from sqlalchemy.orm import sessionmaker
from db_connector import DBConnector
from social_blogs_models import *


engine = create_engine(
    url="mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/social_blogs",
    echo=True,
    future=True
)

# Session = sessionmaker(bind=engine)
# session = Session()
# session.close()

with DBConnector(engine) as session:


    #NOTE: CRUD operations:
    #  Create
    #  Read
    #  Update
    #  Delete

    # NOTE: C (CREATE):
    #  data = {"name": "NewRole"}
    #  new_role = Role(**data)
    #  session.add(new_role)
    #  session.commit()

    #NOTE: R (READ)
    #NOTE: Read one:
    # user = session.get(User, 11)
    # print(user)
    # print(user.email)
    # print(user.first_name)
    # print(user.created_at)

    #NOTE: READ many:
    # all_authors =( #stmt - (STATEMENT)
    #     select(User) # SELECT * FROM 'user' WHERE
    #     .where(User.role_id == 3) # WHERE role_id = 3
    # )
    # #Getting from DB [Row(User()), Row(User()), ...]
    # response = session.execute(all_authors).scalars() #scalars helping to unpack info in list [User(), User(), User()]
    # data = [
    #     {
    #         "id": user.id,
    #         "name": user.first_name,
    #         "role": user.role_id
    #     }
    #     for user in response
    # ]
    # print(data)

    #NOTE: get users with rating > 5.
    # v1(Old one):
    # result = session.query(User).filter(User.rating > 5).all()
    # v2:
    # stmt = (
    #     select(User)
    #     .where(User.rating > 5) # Creating the queries
    # )
    # res = session.execute(stmt).scalars() # Pushing it inside the DB
    # print(res)
    # for obj in res:
    #     print(obj.email, obj.rating) # Getting back the queries

    #NOTE: Get users with last name started at 'M'
    # v1 :
    # stmt = (
    #     select(User)
    #     .where(User.last_name.like("M%"))
    # )
    # v2:
    # last_name_pattern = "M%"
    # stmt = (
    #     select(User)
    #     .where(User.last_name.like(last)name_pattern))
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user.last_name)


    # NOTE: U (UPDATE):






