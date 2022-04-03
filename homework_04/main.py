"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import sys

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import Base, User, Post, Session, engine


def get_users_from_data(data: list[dict]):
    users: list[User] = []
    for doc in data:
        users.append(User(
            id=doc.get("id"),
            name=doc.get("name"),
            username=doc.get("username"),
            email=doc.get("email")
        ))
    return users


def get_posts_from_data(data: list[dict]):
    posts: list[Post] = []
    for doc in data:
        posts.append(Post(
            id=doc.get("id"),
            user_id=doc.get("userId"),
            title=doc.get("title"),
            body=doc.get("body")
        ))
    return posts


async def feed_users(session: AsyncSession, users: list[User]):
    for user in users:
        session.add(user)
    return session


async def feed_posts(session: AsyncSession, posts: list[Post]):
    for post in posts:
        session.add(post)
    return session


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    users_list = get_users_from_data(users_data)
    posts_list = get_posts_from_data(posts_data)
    async with Session() as session:
        session = await feed_users(session, users_list)
        await session.commit()
        session = await feed_posts(session, posts_list)
        await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())
