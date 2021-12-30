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


def pandemic_sim():
    for led in LED_LIST:
        led.RGB = (0, 255, 0)

    led = random.choice(LED_LIST)
    led.RGB = (255, 0, 0)
    file = open("pandemic.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write_first_line(writer)
    infected_LEDs = [led]
    for i in range(1000):
        if i % 20 == 0 and len(infected_LEDs) < 500:
            new_infects = []
            for led in infected_LEDs:
                a, b, c = led.pos
                for led_2 in LED_LIST:
                    x, y, z = led_2.pos
                    r = 0.3
                    if (x - a)**2 + (y - b)**2 + (z - c)**2 < r **2 and led_2 not in infected_LEDs:
                        led_2.RGB = (255, 0, 0)
                        new_infects.append(led_2)
            new_infects = list(set(new_infects))
            infected_LEDs.extend(new_infects)

        write_csv_line(writer, i+1)
        print(len(infected_LEDs))
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
    pandemic_sim()

