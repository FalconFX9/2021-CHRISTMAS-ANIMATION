"""
Ideas: -Game of life
        -Pandemic simulator
       -Splitting collisions
       -Conical double pendulum
"""
import csv
import random
from LED import LED
from pandemic_LED import pandemicLED
import constants as C


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


def gen_pand_led_obj():
    list_local = []
    path = "coords_2021.csv"
    file = open(path, 'r', encoding='utf-8-sig')
    lines = csv.reader(file)
    for i, coords in enumerate(lines):
        for n in range(len(coords)):
            coords[n] = float(coords[n])
        new_led = pandemicLED(i, coords, (0, 0, 0))
        list_local.append(new_led)

    return list_local


LED_LIST = gen_pand_led_obj()


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
    led.infect_time = C.INFECT_TIME / 2
    led.infected = True
    file = open("pandemic.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write_first_line(writer)
    infected_LEDs = [led]

    for i in range(2000):
        not_infected_LEDs = [led for led in LED_LIST if led not in infected_LEDs]
        new_infects = []
        for led in infected_LEDs:
            a, b, c = led.pos
            for led_2 in not_infected_LEDs:
                x, y, z = led_2.pos
                infect_reach = 0.2
                r = -(infect_reach/(C.INFECT_TIME/2)) * abs(led.infect_time - C.INFECT_TIME / 2) + infect_reach
                if (x - a)**2 + (y - b)**2 + (z - c)**2 < r ** 2 and (not led_2.infected or not led_2.cured):
                    led_2.infected = True
                    new_infects.append(led_2)
                if not new_infects:
                    closest_led = not_infected_LEDs[0]
                    sd = ((a * closest_led.pos[0])**2 + (b * closest_led.pos[1])**2 + (c * closest_led.pos[2])**2)**(1/2)
                    for led_n in not_infected_LEDs:
                        x2, y2, z2 = led_n.pos
                        shortest_distance = ((a * x2)**2 + (b * y2)**2 + (c * z2)**2)**(1/2)
                        if sd > shortest_distance:
                            sd = shortest_distance
                            closest_led = led_n
                    closest_led.infected = True
                    new_infects.append(closest_led)


        new_infects = list(set(new_infects))
        infected_LEDs.extend(new_infects)
        for led in LED_LIST:
            led.update()
            if led.cured and led in infected_LEDs:
                infected_LEDs.remove(led)

        write_csv_line(writer, i+1)
        print(i)
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

