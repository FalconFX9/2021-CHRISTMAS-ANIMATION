class LED:
    def __init__(self, ID, pos, RGB):
        self.ID = ID  # int from 0 to LED_NUM-1 inclusive
        self.pos = pos  # tuple in the form (x, y, z)
                        # X, Y and Z are in GIFT format
                        # X and Y are between -1 and 1 inclusive, with 0 being the trunk of the tree
                        # Z is in meters from the bottom of the tree
        self.RGB = RGB  # tuple in the form (R, G, B), where all 3 values are ints from 0 to 255 inclusive
