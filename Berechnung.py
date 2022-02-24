import Data

right_puncher_up = False
right_puncher_down = False
newGame = False

start_ball_to_left = True
NR_X_ELEMENTS = (int) (Data.X_WIDTH / Data.PIXEL_SIZE)
NR_Y_ELEMENTS = (int) (Data.Y_WIDTH / Data.PIXEL_SIZE)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vektor:
    def __init__(self, point, dir_point):
        self.point = point
        self.dir_point = dir_point
    
    def get_points_in_line(self):
        pass


class Puncher:
    def __init__(self, start_x, start_y, nr_y_elements):
        self.pixel_list = []
        self.nr_y_elements = nr_y_elements
        for i in range(5):
            self.pixel_list.append(Point(start_x, start_y + i))
    
    def puncher_up(self):
        if self.pixel_list[0].y > 0:
            for i in range(len(self.pixel_list)):
                self.pixel_list[i].y = self.pixel_list[i].y - 1

    def puncher_down(self):
        if self.pixel_list[0].y < self.nr_y_elements:
            for i in range(len(self.pixel_list)):
                self.pixel_list[i].y = self.pixel_list[i].y + 1


class Berechnung:
    def __init__(self):
        start_y = (int) ((NR_Y_ELEMENTS / 2) - 5)
        self.puncher_right = Puncher(1, start_y)
        self.puncher_left = Puncher(NR_X_ELEMENTS - 1, start_y)
        self.arr = []

    def add_point_list_to_arr(self, point_list):
        for e in point_list:
            self.arr[e.x][e.y] = True

    def get_data_object(self):
        if right_puncher_up:
            self.puncher_right.puncher_up()
        if right_puncher_down:
            self.puncher_right.puncher_down()
        for x in range(NR_X_ELEMENTS):
            self.arr.append([])
            for y in range(NR_Y_ELEMENTS):
                self.arr[x].append(False)
        self.add_point_list_to_arr(self.puncher_right.pixel_list)
        self.add_point_list_to_arr(self.puncher_left.pixel_list)
        start_middle_x = (int) (NR_X_ELEMENTS / 2)
        middle_points = []
        for i in range(NR_Y_ELEMENTS):
            if (i % 2) == 0:
                middle_points.append(Point(start_middle_x, i))
        self.add_point_list_to_arr(middle_points)
        if newGame:
            pass
        return self.arr