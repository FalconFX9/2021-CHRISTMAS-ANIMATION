"""
Ideas: -Game of life
        -Pandemic simulator
       -Splitting collisions
       -Conical double pendulum
"""
import csv
import random
from LED import LED


def gen_led_obj():
    list_local = []
    path = "coords_2021.csv"
    file = open(path, 'r', encoding='utf-8-sig')
    lines = csv.reader(file)
    for i, coords in enumerate(lines):
        for n in range(len(coords)):
            coords[n] = float(coords[n])
        new_led = LED(i, coords, (0, 0, 0))
        list_local.append(new_led)

    return list_local


LED_LIST = gen_led_obj()


def random_colors():
    file = open("random_colors.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write_first_line(writer)
    for i in range(1000):
        if i % 15:
            for led in LED_LIST:
                led.RGB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        write_csv_line(writer, i)

    file.close()


def write_csv_line(file, frame_num):
    row = [frame_num]

    for led in LED_LIST:
        for color in led.RGB:
            row.append(color)

    file.writerow(row)


def write_first_line(file):
    row = ['FRAME_ID']
    for led in LED_LIST:
        row.append(f"R_{led.ID}")
        row.append(f"G_{led.ID}")
        row.append(f"B_{led.ID}")

    file.writerow(row)



if __name__ == "__main__":
    random_colors()

