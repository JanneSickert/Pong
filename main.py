import GUI
import Berechnung
import time
puncher_up = False
puncher_down = False
gui = GUI.GUI()
berechnung = Berechnung.Berechnung()
puncher_down, puncher_up = gui.repaint(berechnung.get_data_object(new_game=True, right_puncher_up = puncher_up, right_puncher_down = puncher_down))
active = True
while active:
    matrix = berechnung.get_data_object(new_game=False, right_puncher_up = puncher_up, right_puncher_down = puncher_down)
    if matrix == None:
        active = False
    else:
        puncher_down, puncher_up = gui.repaint(matrix)
    time.sleep(0.3)