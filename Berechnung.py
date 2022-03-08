from contextlib import nullcontext
import Data
import math
import random

NR_X_ELEMENTS = (int) (Data.X_WIDTH /  Data.PIXEL_SIZE)
NR_Y_ELEMENTS = (int) (Data.Y_HEIGHT / Data.PIXEL_SIZE)
PUNCER_SIZE = (int) (NR_Y_ELEMENTS / 8)

right_puncher_up = False
right_puncher_down = False
newGame = False
current_ball_way = []
current_ball_way_index = 0
border_points = []
ball_point = None

class Point:
    """
    Speichert x und y und repräsentiert somit einen Punkt.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def short_vektor(self, factor):
        self.x = self.x / factor
        self.y = self.y / factor
    
    def turn_around(self):
        self.y = self.y * (-1)
    
    def is_same(self, point):
        return (self.x == point.x and self.y == point.y)


class Strecke:
    """
    Eine Strecke ist ein Array von Punkten. Diese Punkte werden nach und nach angezeigt.
    So das es so ausieht als wenn sich der Ball bewegen würde.
    """
    def __init__(self, point, dir_point):
        self.point = point
        self.dir_point = dir_point

    def get_points_in_line(self):
        diagonale = math.sqrt(math.pow(NR_X_ELEMENTS, 2) + math.pow(NR_Y_ELEMENTS, 2))
        richtungsvektor = Point(self.dir_point.x - self.point.x, self.dir_point.y - self.point.y)
        richtungsvektor.short_vektor(diagonale)
        i = 0
        p = []
        b = True
        while b:
            x = self.point.x + i * richtungsvektor.x
            y = self.point.y + i * richtungsvektor.y
            b1 = x >= 0 and x < NR_X_ELEMENTS
            b2 = y >= 0 and y < NR_Y_ELEMENTS
            b = b1 and b2
            if not b:
                break
            p.append(Point(round(x), round(y)))
        return p



class Puncher:
    """
    Der Schläger besteht aus einem Array von Punkten. Mit dem befehl puncer_up oder down,
    werden alle Punkte auf dem Schläger bewegt.
    """
    def __init__(self, start_x, start_y):
        self.pixel_list = []
        for i in range(PUNCER_SIZE):
            self.pixel_list.append(Point(start_x, start_y + i))
    
    def puncher_up(self):
        if self.pixel_list[0].y > 0:
            for i in range(len(self.pixel_list)):
                self.pixel_list[i].y = self.pixel_list[i].y - 1

    def puncher_down(self):
        if self.pixel_list[0].y < PUNCER_SIZE:
            for i in range(len(self.pixel_list)):
                self.pixel_list[i].y = self.pixel_list[i].y + 1

    def is_point_on_pixel_list(self, point):
        for e in self.pixel_list:
            if point.is_same(e):
                return True
        return False


class Berechnung:
    """
    Hier werden alle Spielereignisse berechnet. Wie zum Beispiel der Abprall am Schläger oder an der Wand,
    oder wenn ein Ball am Schläger vorbei geht. Zusätzlich wird die Mittelinie berechnet.
    """
    def __init__(self):
        start_y = (int) ((NR_Y_ELEMENTS / 2) - 5)
        self.puncher_right = Puncher(1, start_y)
        self.puncher_left = Puncher(NR_X_ELEMENTS - 1, start_y)
        self.arr = []

    def add_point_list_to_arr(self, point_list):
        for e in point_list:
            self.arr[e.x][e.y] = True

    def have_hit_puncher(self, point):
        b1 = self.puncher_right.is_point_on_pixel_list(current_ball_way[current_ball_way_index])
        b2 = self.puncher_left.is_point_on_pixel_list(current_ball_way[current_ball_way_index])
        b = b1 or b2
        return b

    def have_hit_border(self, point):
        b1 = point in border_points[2]
        b2 = point in border_points[3]
        b = b1 or b2
        return b

    def get_data_object(self, new_game = True):
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
        if new_game:
            ra = round(random.random())
            move_ball_to = random.choice(border_points[ra])
            rx = move_ball_to.x
            ry = move_ball_to.y
            middle = Point(NR_X_ELEMENTS / 2, NR_Y_ELEMENTS / 2)
            strecke = Strecke(middle, Point(rx, ry))
            current_ball_way = strecke.get_points_in_line()
            current_ball_way_index = 0
            new_game = False
        if self.have_hit_puncher(current_ball_way[current_ball_way_index]):
            if rx < (NR_X_ELEMENTS / 2):
                current_ball_way_dir = random.choices(border_points[1])
            else:
                current_ball_way_dir = random.choices(border_points[0])
            s = Strecke(current_ball_way[current_ball_way_index], current_ball_way_dir)
            current_ball_way = s.get_points_in_line()
            current_ball_way_index = 1
        ball_point = current_ball_way[current_ball_way_index]
        if self.have_hit_border(ball_point):
            s = Strecke(ball_point, current_ball_way_dir.turn_around())
            current_ball_way = s.get_points_in_line()
            current_ball_way_index = 1
        self.add_point_list_to_arr([ball_point])
        if ball_point.y > self.puncher_left.pixel_list[random.randint(PUNCER_SIZE - 1)]:
            self.puncher_left.puncher_down()
        else:
            self.puncher_left.puncher_up()
        current_ball_way_index += 1
        return self.arr

# Hier im Konstruktor werden die Enden des Spielfelds berechnet.
# border_points 0 und 1 sind die Enden wo der Ball abprallt.
# 2 und 3 die Enden wo Punkte erziehlt werden können.
for i in range(4):
    border_points.append([])
for i in range(NR_X_ELEMENTS):
    border_points[0].append(Point(i, 0))
for i in range(NR_X_ELEMENTS):
    border_points[1].append(Point(i, NR_Y_ELEMENTS - 1))
i = 1
while i < (NR_Y_ELEMENTS - 1):
    border_points[2].append(Point(0, i))
    i = i + 1
i = 1
while i < (NR_Y_ELEMENTS - 1):
    border_points[3].append(Point(NR_X_ELEMENTS - 1, i))
    i = i + 1