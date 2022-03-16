import GUI
import Berechnung
import tkinter as tk

app = tk.Tk()
gui = GUI.GUI(Berechnung.Berechnung(), app)
gui.repaint()
app.mainloop()