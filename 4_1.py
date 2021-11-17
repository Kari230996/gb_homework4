# 4.1

from PIL import Image


screenshot = int(input('Укажите номер скриншота от 1 - 4 '))

screenshot_1 = Image.open('01.jpg') # Первый скриншот, установка pillow
screenshot_2 = Image.open('02.jpg') # Второй скриншот, создание и активирование виртуального окружения
screenshot_3 = Image.open('03.jpg') # Третий скриншот, установка pillow в виртуальный окружение
screenshot_4 = Image.open('04.jpg') # Четвертый скриншот, деактивация ВО

if screenshot == 1:
    screenshot_1.show()
elif screenshot == 2:
    screenshot_2.show()
elif screenshot == 3:
    screenshot_3.show()
elif screenshot == 4:
    screenshot_4.show()
else:
    print('Файл не найден')

