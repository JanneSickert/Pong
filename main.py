import GUI
import Berechnung
import time

gui = GUI.GUI()
berechnung = Berechnung.Berechnung()

active = True
while active:
    matrix = berechnung.get_data_object()
    if matrix == None:
        active = False
    else:
        gui.repaint(matrix)
    time.sleep(0.3)
