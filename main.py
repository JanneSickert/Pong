import GUI
import Berechnung

gui = GUI.GUI()
berechnung = Berechnung.Berechnung()

gui.repaint(berechnung.get_data_object())