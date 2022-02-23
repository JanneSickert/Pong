import Data

right_puncher_up = False
right_puncher_down = False
nr_x_elemets = (int) (Data.X_WIDTH / Data.PIXEL_SIZE)
nr_y_elemets = (int) (Data.Y_WIDTH / Data.PIXEL_SIZE)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        start_y = (int) ((nr_y_elemets / 2) - 5)
        self.puncher_right = Puncher(1, start_y)
        self.puncher_left = Puncher(nr_x_elemets - 1, start_y)

    def getDataObject(self):
        if right_puncher_up:
            self.puncher_right.puncher_up()
        if right_puncher_down:
            self.puncher_right.puncher_down()
        arr = []
        for x in range(nr_x_elemets):
            arr.append([])
            for y in range(nr_y_elemets):
                arr[x].append(False)
        for i in range(len(self.puncher_right.pixel_list)):
            arr[self.puncher_right.pixel_list[i].x][self.puncher_right.pixel_list[i].y] = True
        for i in range(len(self.puncher_left.pixel_list)):
            arr[self.puncher_left.pixel_list[i].x][self.puncher_left.pixel_list[i].y] = True
        start_middle_x = (int) (nr_x_elemets / 2)
        middle_points = []
        for i in range(nr_y_elemets):
            if (i % 2) == 0:
                middle_points.append(Point(start_middle_x, i))
        for e in middle_points:
            arr[e.x][e.y] = True
        return arr