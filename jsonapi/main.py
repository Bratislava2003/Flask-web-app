import asyncio
from .jsonplaceholder_requests import get_posts, get_users


async def get_data():
    reformed_list = []
    all_data = await asyncio.gather(get_users(), get_posts())
    for data_half in all_data:
        for data_block in data_half:
            reformed_list.append(data_block)
    return reformed_list


def get_list():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.run(get_data())


if __name__ == "__main__":
    main()
