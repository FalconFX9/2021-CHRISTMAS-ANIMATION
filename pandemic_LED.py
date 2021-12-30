import LED
import constants as C


class pandemicLED(LED.LED):

    def __init__(self, ID, pos, RGB):
        super().__init__(ID, pos, RGB)
        self.infected = False
        self.cured = False
        self.infect_time = C.INFECT_TIME
        self.cure_time = C.CURE_DELAY
        self.never_cured = True

    def update(self):
        if self.infected:
            R = -(255 / (C.INFECT_TIME / 2)) * abs(self.infect_time - C.INFECT_TIME / 2) + 255
            if self.infect_time > C.INFECT_TIME / 2:
                G = 255 * ((self.infect_time-(C.INFECT_TIME/2))/(C.INFECT_TIME/2))
                B = 0
                self.RGB = (R, 0, G)
            else:
                G = 0
                B = 255 * abs((self.infect_time-(C.INFECT_TIME/2))/(C.INFECT_TIME/2))
                self.RGB = (R, G, B)

            if self.never_cured:
                self.RGB = (R, G, B)

            self.infect_time -= 1
        if self.infect_time == 0:
            self.infect_time = C.INFECT_TIME
            self.infected = False
            self.cured = True
            self.never_cured = False
        if self.cured:
            self.cure_time -= 1
        if self.cure_time == 0:
            self.cure_time = C.CURE_DELAY
            self.cured = False
