import random

from PIL import Image, ImageDraw, ImageFont

def z1():
    image = Image.open("открытка.jpg")
    k1 = (100, 50, 600, 200)
    k2 = (500, 200, 1150, 800)
    image1 = image.crop(k1)
    image2 = image.crop(k2)
    image1.save("текст открытки.jpg")
    image2.save("рисунок открытки.jpg")
    image1.show()
    image2.show()

def z2():
    hс = {
        "ДЕНЬ РОЖДЕНИЯ": "HB.jpg",
        "НОВЫЙ ГОД": "NY.jpg",
        "ДЕНЬ СТУДЕНТА": "DS.jpg",
        "ДЕНЬ СВЯТОГО ВАЛЕНТИНА": "VD.jpg",
        "МАСЛЕНИЦА": "M.jpg",
        "ПАСХА": "P.jpg"

    }
    holiday = input("Введите название праздника: ").upper()
    if holiday in hс:
        card_filename = hс[holiday]
        card_image = Image.open(card_filename)
        card_image.show()
    else:
        print("Открытки для данного праздника не найдено.")

def z3():
    card_image = Image.open("открытка.jpg")
    name = input("Введите имя человека, которого хотите поздравить: ")

    draw = ImageDraw.Draw(card_image)
    font = ImageFont.truetype("arial.ttf", 40)
    text = f"{name}, поздравляю!"

    draw.text((80, 200), text=text, font=font, fill="Red", stroke_width=2, stroke_fill=(0, 0, 0))

    card_image.save("new_holiday_card.png", "PNG")
    card_image.show()

