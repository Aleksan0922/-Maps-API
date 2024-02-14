import os
import sys

import pygame
import requests

height = 20.284978
width = -25.348019
type = 'sat'
params = {
    'll': ','.join([str(height), str(width)]),
    'pt': '',
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


def update():
    global params
    map_request = "https://static-maps.yandex.ru/1.x/"
    response = requests.get(url=map_request, params=new_params)

    if response.status_code == 200:
        params = new_params
        params['z'] = new_params['z']
        params['pt'] = new_params['pt']
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

        screen.blit(pygame.image.load(map_file), (0, 100))
        pygame.display.flip()


def get_ll_and_coords(adress):
    toponym_to_find = adress

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        sys.exit(1)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]['pos']
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return (toponym_longitude, toponym_lattitude)


# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 550))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 100))
# Переключаем экран и ждем закрытия окна.
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(10, 10, 500, 32)
button_box = pygame.Rect(520, 10, 80, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if button_box.collidepoint(event.pos):
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': '',
                    'z': params['z'],
                    'l': type
                }

                update()
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    toponym_coodrinates = get_ll_and_coords(text)

                    width, height = float(toponym_coodrinates[1]), float(toponym_coodrinates[0])
                    z = 5

                    new_params = {
                        'll': ','.join([str(height), str(width)]),
                        'pt': params['pt'],
                        'z': z,
                        'l': type
                    }

                    map_request = "https://static-maps.yandex.ru/1.x/"
                    response = requests.get(url=map_request, params=new_params)

                    while response.status_code != 200:
                        map_request = "https://static-maps.yandex.ru/1.x/"
                        response = requests.get(url=map_request, params=new_params)
                        z += 1

                    new_params = {
                        'll': ','.join([str(height), str(width)]),
                        'pt': params['pt'],
                        'z': z,
                        'l': type
                    }

                    if params['pt'] != '':
                        new_params['pt'] = new_params['pt'] + '~' + ','.join([str(height), str(width)])
                    else:
                        new_params['pt'] = ','.join([str(height), str(width)])

                    active = False
                    color = color_inactive
                    update()
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            elif event.key == pygame.K_PAGEUP:
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'] + 1 if params['z'] < 21 else params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_PAGEDOWN:
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'] - 1 if params['z'] > 0 else params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_LEFT:
                height = height - 10 if height > -180 else height
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_RIGHT:
                height = height + 10 if height < 180 else height
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_UP:
                width = width + 10 if width < 90 else width
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_DOWN:
                width = width - 10 if width > -90 else width
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_1:
                print(params)
                type = 'map'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_2:
                type = 'sat'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
            elif event.key == pygame.K_3:
                type = 'sat,skl'
                new_params = {
                    'll': ','.join([str(height), str(width)]),
                    'pt': params['pt'],
                    'z': params['z'],
                    'l': type
                }

                update()
    screen.fill(pygame.Color('black'))
    txt_surface = font.render(text, True, color)
    button_surface = font.render('Сброс', True, 'red')
    screen.blit(pygame.image.load(map_file), (0, 50))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    screen.blit(button_surface, (button_box.x + 5, button_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.draw.rect(screen, 'red', button_box, 2)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)