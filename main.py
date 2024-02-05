import os
import sys

import pygame
import requests

height = 20.284978
width = -25.348019
type = 'sat'
params = {
    'll': ','.join([str(height), str(width)]),
    'z': 2,
    'l': type
}

map_request = "https://static-maps.yandex.ru/1.x/"
response = requests.get(url=map_request, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'] + 1 if params['z'] < 21 else params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_PAGEDOWN:
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'] - 1 if params['z'] > 0 else params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_LEFT:
                height = height - 10 if height > -180 else height
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                height = height + 10 if height < 180 else height
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()

            if event.key == pygame.K_UP:
                width = width + 10 if width < 90 else width
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_DOWN:
                width = width - 10 if width > -90 else width
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_1:
                type = 'map'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_2:
                type = 'map'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_3:
                type = 'sat,skl'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'z': params['z'],
                    'l': type
                }

                map_request = "https://static-maps.yandex.ru/1.x/"
                response = requests.get(url=map_request, params=new_params)

                if response.status_code == 200:
                    params = new_params
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

                    screen.blit(pygame.image.load(map_file), (0, 0))
                    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)