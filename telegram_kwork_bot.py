# import logging
# import asyncio
# from kwork import Kwork
# from kwork.types import User, Connects, Actor # Убедитесь, что все необходимые типы импортированы
# from kwork.exceptions import KworkException # Импортируем KworkException для специфичной обработки
#
# # Настраиваем логирование для вывода отладочной информации
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# async def main():
#     api = None  # Инициализируем api как None. Это важно.
#     try:
#         logging.info("Попытка создания экземпляра Kwork API.")
#         # !!!! ЗАМЕНИТЕ "login" и "password" на ваши актуальные данные !!!!
#         # Если вы используете phone_last или proxy, раскомментируйте соответствующую строку.
#         api = Kwork(login="ВАШ_ЛОГИН", password="ВАШ_ПАРОЛЬ")
#         # api = Kwork(login="ВАШ_ЛОГИН", password="ВАШ_ПАРОЛЬ", phone_last="0102")
#         # api = Kwork(login="ВАШ_ЛОГИН", password="ВАШ_ПАРОЛЬ", proxy="socks5://208.113.220.250:3420")
#         logging.info("Экземпляр Kwork API создан.")
#
#         me: Actor = await api.get_me()
#         logging.info(f"Получен профиль пользователя: {me.username}")
#         print(f"Мой профиль: {me}")
#
#         categories = await api.get_categories()
#         logging.info(f"Получено {len(categories)} категорий.")
#         # print("Категории:")
#         # for cat in categories:
#         #     print(f"  - {cat.name} (ID: {cat.id})")
#
#         # Получение проектов с биржи по id категорий
#         # Убедитесь, что эти ID категорий существуют и актуальны
#         logging.info("Попытка получения проектов из категорий [11, 79].")
#         projects = await api.get_projects(categories_ids=[11, 79])
#         logging.info(f"Получено {len(projects)} проектов.")
#         print("Полученные проекты:")
#         for project in projects:
#             print(f"  - {project.name} (ID: {project.id})")
#
#     except KworkException as e:
#         logging.error(f"Kwork API Ошибка: {e}", exc_info=True)
#         # Здесь вы можете добавить логику для обработки конкретных ошибок Kwork
#         if "Подтвердите, что вы не робот" in str(e):
#             logging.critical("Kwork требует подтверждения, что вы не робот. "
#                              "Пожалуйста, проверьте ваши учетные данные, "
#                              "используйте phone_last, если необходимо, "
#                              "или попробуйте использовать прокси.")
#         # Дополнительная обработка других KworkExceptions
#     except Exception as e:
#         logging.error(f"Произошла непредвиденная ошибка: {e}", exc_info=True)
#     finally:
#         if api:
#             logging.info("Попытка закрыть API-соединение.")
#             await api.close()
#             logging.info("API-соединение закрыто.")
#         else:
#             logging.warning("API-соединение не было инициализировано или успешно создано, поэтому закрытие пропущено.")
#
#
# # Рекомендуемый способ запуска асинхронного кода в Python 3.7+
# if __name__ == "__main__":
#     logging.info("Запуск основной программы.")
#     try:
#         asyncio.run(main())
#     except RuntimeError as e:
#         logging.error(f"Ошибка запуска asyncio: {e}")
#     logging.info("Программа завершена.")
#
