from sqlalchemy import (create_engine,
                        select,
                        or_,
                        not_,
                        and_,
                        desc,
                        func,
                        alias)
from sqlalchemy.orm import (sessionmaker,
                            aliased,
                            joinedload)
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

    #NOTE: get users wih rating from 2 to 5
    # stmt = (
    #     select(User)
    #     .where(User.rating.between(2, 5))
    # )
    # res = session.execute(stmt).scalars()
    # for row in res:
    #     print(row.rating)

    #NOTE: get users only authors wit rating > 6 (and_ == sql and)
    # v1: stmt = (
    #     select(User)
    #     .where(
    #         and_(User.role_id == 3, User.rating > 6) # < or_ can be placed inside also
    #     )
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user.rating)
    # v2: stmt = (
    #     select(User)
    #     .where(
    #         and_(User.role_id == 3, User.rating > 6) # < or_ can be placed inside also
    #     )
    #     .order_by(User.rating) # Creating clear scale list from less to high.
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user.rating)
    # v3: stmt = (
    #     select(User)
    #     .where(
    #         and_(User.role_id == 3, User.rating > 6) # < or_ can be placed inside also
    #     )
    #     .order_by(desc(User.rating)) # desc - vice versa - from high to less
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user.rating)
    # v4: stmt = (
    #     select(User)
    #     .where(
    #         and_(User.role_id == 3, User.rating > 6) # < or_ can be placed inside also
    #     )
    #     .order_by(desc(User.rating), User.last_name) # desc - vice versa - from high to less and if it matches show us last name
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user.rating, user.last_name)

#========================= Aggregation && grouping =========================

    #NOTE: func.avg + scalar() > one = scalars() > many.
    # v1: stmt = (
    #      select(func.avg(User.rating)) # SELECT AVG('user'.rating) FROM user;
    #  )
    #  res = session.execute(stmt).scalar() #Now we have scalar instead of scalars - first we using if
    #  # pulling a single stuff out of db - interpreter with number or one thing. Scalars - when pulling many things.
    #  print(res)
    # Scalar() - takes 1 thing from 1-st column and only. Scalars() - take everything from column.
    # v2: stmt = (
    #      select(User.role_id, func.avg(User.rating))
    #     .group_by(User.role_id) # SELECT user.role_id, AVG('user'.rating) FROM user GROUP BY 'user.role_id';
    #  )
    #  res = session.execute(stmt).scalars()
    #  print(res)
    # v3: stmt = (
    #      select(User.role_id,
    #             func.avg(User.rating))  # SELECT user.role_id, AVG('user'.rating) FROM user GROUP BY uer.role_id;
    #      .group_by(User.role_id)
    #  )
    #  result = session.execute(stmt).scalars()
    #  print(result)
    #  for re in res:
    #      print(re)


    #NOTE: AS - ALIAS for table
    #NOTE: With GROUPING we using - all() INSTEAD of scalars()
    # us = alias(selectable=User, name="us")
    # us = aliased(element=User, name="us") # sqlalchemy.orm - for ORM approach.
    # v1: stmt = (
    #     select(us.role_id,
    #            func.count(us.id).label("count_of_users") #Creating column which will contain result of count
#            + setting the Label for it
    #            )
    #     .group_by(us.role_id)
    # )
    # result = session.execute(stmt).all() # Not using the Scolars() because it takes every 1 things from 1 column
    # # its working with usual queries - but when we are grouping result became not usual  We receive different objects
    # # list not with tuples. So because of grouping we using ALL() to take everything.
    # for group in result:
    #     print(f"user role: {group.role_id} | Count of users: {group.count_of_users}")
    # v2 - Plus HAVING : us = aliased(element=User, name="us")  # sqlalchemy.orm - for ORM approach.
    # stmt = (
    #     select(
    #         us.role_id,
    #         func.count(us.id).label("count_of_users") # LABELS exists only after created as a table
    #           # so we have labels only after queries were input.
    #     )
    #     .group_by(us.role_id)
    #     .having(func.count(us.id) > 4) # Used for count and withdraw groups more then something > 4 etc.
    # )
    # result = session.execute(stmt).all()
    # for group in result: # LABELS we have only HERE after the were created as a table.
    #     print(f"user role: {group.role_id} | Count of users: {group.count_of_users}")

    #NOTE: Subquery - just a part for bigger query
    # us = aliased(element=User, name="us")  # sqlalchemy.orm - for ORM approach.
    # mean_rate_by_author_sbq = select(
    #     func.avg(User.rating).label("user_rating")
    # ).where(User.role_id == 3).scalar_subquery() # Again if we withdraw only ONE(not many) thing itll be scalar()
    # # if withdrawing MANY we put just .subquery()
    # main_query = select(User.rating > mean_rate_by_author_sbq) # Main query where we are using previously don subquery
    # result = session.execute(main_query).scalars()
    # for user in result:
    #     print(user.last_name, user.rating)
    # Teacher:
    # Подзапрос
    # mean_rate_by_author_sbq = select(
    #     func.avg(User.rating).label("user_rating")
    # ).where(User.role_id == 3).scalar_subquery()
    # Главный зпрос
    # main_query = select(User).where(User.rating > mean_rate_by_author_sbq)
    # result = session.execute(main_query).scalars()
    # print(result)
    # for user in result:
    #     print(user.last_name, user.rating)

    #NOTE:


    #NOTE: U (UPDATE): further explanations needed.
    # user = session.get(User, 2)
    # user.rating = 7
    # session.commit()

   #part ========= JOIN =========

    #NOTE: JOIN - .join() - when filtration needed.
    # .joinedload()
    # .subqueryload()
    # .selectinload()
    # taking user as 'author'
    # v1: stmt = (
    #     select(User)
    #     # .koin(Role)
    #     .join(Role, Role.id == User.role_id)
    #     # .join(User.role_id)
    #     .where(Role.name == 'author')
    # )
    # result = session.execute(stmt).scalars()
    # for user in result:
    #     print(user.first_name, user.role_id)

    #NOTE: her users with their news feed.
    # stmt = (
    #     select(User)
    #     .join(Role, Role.id == User.role_id) # Withdraw just table without data
    #     .outerjoin(News, User.id == News.author_id)
    #     .options(joinedload(User.news)) # withdraw table with actual data innit
    #     .where(Role.name == 'author')
    # )
    # result = session.execute(stmt).scalars()
    # for user in result:
    #     print(user.last_name, user.news)

    #part ======================== Practice 3 ========================
    #NOTE: Напишите запрос, который возвращает пользователя с конкретным именем (например, "Alice").
    # stmt = (
    #     select(User)
    #     .where(User.first_name == "Alice")
    # )
    # res = session.execute(stmt).scalars()
    # for user in res:
    #     print(user)

    #NOTE: Напишите запрос для вывода всех пользователей, рейтинг которых больше 6.
    # stmt = (
    #     select(User)
    #     .where(User.rating > 6)
    #     #.order_by(User.rating)
    #     .order_by(desc(User.rating))
    # )
    # result = session.execute(stmt).scalars()
    # for user in result:
    #     print(user.rating, user.first_name)

    #NOTE: Обновить рейтинг пользователя "Anna" до 3.4 если такой есть. Напишите запрос для обновления данных.
    # stmt = (
    #     select(User)
    #     .where(User.first_name == "Anna", User.rating)
    # )
    # result = session.execute(stmt).scalars().first()
    # results = session.execute(stmt).scalars()
    # #print(result)
    # if result:
    #     result.rating = 3.4
    #     session.commit()
    #     print(result.first_name, result.rating)
    # for user in results:
    #     print(f"Name: {user.first_name} - Rating: {user.rating}")

    #NOTE: Создайте запрос, который найдет максимальный и минимальный рейтинг среди пользователей.
    # Используйте функции func.max() и func.min().
    # stmt = (
    #     select(
    #         func.min(User.rating).label('min_rating'),
    #         func.max(User.rating).label('max_rating')
    #     )
    # )
    # result = session.execute(stmt).all()
    # print(result)
    # # print(list(result))
    # print(result[0].min_rating)
    # print(result[0].max_rating)

    #NOTE: Напишите запрос, который группирует пользователей по рейтингу и подсчитывает
    # количество пользователей в каждой группе.
    # stmt = (
    #     select(User.rating,
    #            func.count(User.id).label('user_count')
    #            )
    #     .group_by(User.rating)
    # )
    # result = session.execute(stmt).all()
    # #print(result)
    # for user in result:
    #     print(user.rating, user.user_count)

