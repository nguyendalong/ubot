import constants


class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def check_location(self, arr_str):
        len_arr = len(arr_str)
        for i in range(len_arr):
            if arr_str[i] == constants.TURN_LEFT:
                if self.direction == constants.NORTH:
                    self.direction = constants.WEST
                elif self.direction == constants.SOUTH:
                    self.direction = constants.EAST
                elif self.direction == constants.EAST:
                    self.direction = constants.NORTH
                elif self.direction == constants.WEST:
                    self.direction = constants.SOUTH
            if arr_str[i] == constants.TURN_RIGTH:
                if self.direction == constants.NORTH:
                    self.direction = constants.EAST
                elif self.direction == constants.SOUTH:
                    self.direction = constants.WEST
                elif self.direction == constants.EAST:
                    self.direction = constants.SOUTH
                elif self.direction == constants.WEST:
                    self.direction = constants.NORTH
            if arr_str[i] == constants.GO_straight:
                is_top = False
                str_number = ""
                while not is_top:
                    j = i
                    if (j < len_arr - 1):
                        j = j + 1

                    if arr_str[j].isdigit():
                        str_number += arr_str[j]
                    if j == len_arr - 1 or not arr_str[j].isdigit():
                        is_top = True
                    i = j
                number = int(str_number)
                if self.direction == constants.NORTH:
                    self.y += number
                elif self.direction == constants.SOUTH:
                    self.y -= number
                elif self.direction == constants.EAST:
                    self.x += number
                elif self.direction == constants.WEST:
                    self.x -= number

        return self


input_str_road = input("Please enter string: \n")
input_str_road = str(input_str_road)
arr_road = list(input_str_road)

ro = Robot(0, 0, constants.NORTH)
ro.check_location(arr_road)
print('X:' + str(ro.x) + ' Y:' + str(ro.y) + ' Direction: ' + ro.direction)
