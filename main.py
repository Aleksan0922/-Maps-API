import os
import sys

import pygame
import requests

params = {
    'll': '20.284978,-25.348019',
    'z': '2',
    'l': 'sat'
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
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)