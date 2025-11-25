from kwork import Kwork
from kwork.types import Project

import logging
import asyncio
import aiohttp
import urllib.parse

from config import LOGIN, PASSWORD, PHONE_LAST, TOKEN, MY_ID, PORJECTS_IDS, TIME_DELAY

logging.basicConfig(level=logging.INFO)


async def login() -> Kwork:
    return Kwork(login=LOGIN, password=PASSWORD, phone_last=PHONE_LAST)


async def notify_in_telegram(project: Project) -> None:
    async with aiohttp.ClientSession() as session:
        msg = f"❗Новый проект на Kwork❗\n\n" \
              f"Название: {project.title}\n" \
              f"Цена: {project.price}₽\n" \
              f"Допустимо до: {project.possible_price_limit}₽\n\n" \
              f"Описание: {project.description}\n\n" \
              f"Ссылка: https://kwork.ru/projects/{project.id}/view"

        msg = urllib.parse.quote(msg)

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?&chat_id={MY_ID}&text={msg}"
        await session.get(url)


class DataBase:

    @staticmethod
    def check_in_db(id_project: int) -> bool:

        with open('base.txt', "r", encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            if int(line) == id_project:
                return True

        return False

    @staticmethod
    def add_in_db(id_project: int):
        with open('base.txt', "a", encoding='utf-8') as f:
            f.write(f"{id_project}\n")


async def main():
    api: Kwork = await login();

    print('Начал свою работу...')

    try:
        while True:
            projects: Project = await api.get_projects(PORJECTS_IDS)

            # Проходимся по каждому проекту, если есть нвоый то отправляем уведомление в Telegram
            for project in projects:
                if DataBase.check_in_db(project.id) == False:
                    await notify_in_telegram(project)
                    DataBase.add_in_db(project.id)
                    await asyncio.sleep(0.3)

            await asyncio.sleep(TIME_DELAY)

    finally:
        await api.close()


asyncio.run(main())