import GUI
import Data
import Berechnung

data = Data.Data()
gui = GUI.GUI()
berechnung = Berechnung.Berechnung()

gui.repaint(berechnung.getDataObject())

print(data.court)