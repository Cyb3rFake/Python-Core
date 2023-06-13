"""

https://hh.ru/vacancy/78542200

Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория
https://gitea.radium.group/radium/project-configuration во временную папку.
После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.
Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration
Обязательно 100% покрытие тестами
При выполнении в ChatGPT - обязательна переработка

"""

# import requests
#
# url  = "https://gitea.radium.group/radium/project-configuration"
# r = requests.get(url)
# headers = jso r.headers
# print(headers)
from  time import  time_ns


# def my_shiny_new_decorator(function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print('Что-то выполняющееся до вызова функции')
#         function_to_decorate()
#         print('Что-то выполняющееся после вызова функции')
#     return the_wrapper_around_the_original_function
#
# def stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()


import aiohttp
import asyncio
import os


async def download_repo_content(temp_folder):
    async with aiohttp.ClientSession() as session:
        async with session.head('https://gitea.radium.group/radium/project-configuration') as response:
            # Получаем размер контента
            content_length = response
            print(f"Content length: {content_length}")

    # Создаем временную папку (если она не существует)
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Запускаем три задачи на скачивание контента параллельно
    tasks = []
    for i in range(3):
        task = asyncio.create_task(download_partially(i, content_length, temp_folder))
        tasks.append(task)

    await asyncio.gather(*tasks)


async def download_partially(part_id, content_length, temp_folder):
    chunk_size = content_length // 3  # Размер куска
    start_byte = part_id * chunk_size
    end_byte = start_byte + chunk_size - 1

    headers = {'Range': f'bytes={start_byte}-{end_byte}'}

    async with aiohttp.ClientSession() as session:
        async with session.get('https://gitea.radium.group/radium/project-configuration', headers=headers) as response:
            data = await response.read()
            filename = os.path.join(temp_folder, f"part{part_id}.zip")
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"Part {part_id} downloaded")


if __name__ == '__main__':
    temp_folder = "./temp"
    asyncio.run(download_repo_content(temp_folder))


