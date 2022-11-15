import asyncio
from db_cfg import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from jsonplaceholder_requests import get_posts, get_users
from models import User, Post

async_engine: AsyncEngine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=True
)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=True
)


async def get_data():
    reformed_list = []
    all_data = await asyncio.gather(get_users(), get_posts())
    for data_half in all_data:
        for data_block in data_half:
            reformed_list.append(data_block)
    return reformed_list


async def create_user(session: AsyncSession, user_name: str, username: str, email: str):
    user = User(user_name=user_name, username=username, email=email)
    session.add(user)
    return user


async def create_post(session: AsyncSession, body: str, title: str, user_id: int):
    post = Post(title=title, body=body, user_id=user_id)
    session.add(post)
    return post


async def async_main():

    all_data = await get_data()

    names = all_data[0]
    usernames = all_data[1]
    emails = all_data[2]

    bodies = all_data[5]
    titles = all_data[4]
    user_ids = all_data[3]

    async with Session() as db_session:
        async with db_session.begin():
            for i in range(len(all_data[0])):
                namev = names[i]
                usernamev = usernames[i]
                emailv = emails[i]
                await create_user(db_session, namev, usernamev, emailv)

            for d in range(len(all_data[3])):
                bodyv = str(bodies[d])
                titlev = str(titles[d])
                user_idsv = int(user_ids[d])
                await create_post(db_session, bodyv, titlev, user_idsv)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
