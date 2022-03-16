import Data
import tkinter as tk

class GUI:
    def move_puncher(self, event):
        if event.char == "s":
            self.puncher_down = True
            self.puncher_up = False
        elif event.char == "w":
            self.puncher_down = False
            self.puncher_up = True
            
    def __init__(self, berechnung, root):
        self.app = root
        self.app.geometry(str(Data.X_WIDTH) + "x" + str(Data.Y_HEIGHT))
        self.app.title("Pong")
        self.app.bind("<KeyPress>", self.move_puncher)
        self.puncher_down = False
        self.puncher_up = False
        self.berechnung = berechnung
        aField = self.berechnung.get_data_object(right_puncher_up = self.puncher_up, right_puncher_down = self.puncher_down)
        self.elements_x = int(Data.X_WIDTH / Data.PIXEL_SIZE)
        self.elements_y = int(Data.Y_HEIGHT / Data.PIXEL_SIZE)
        self.canvas = tk.Canvas(self.app, bg = Data.BACKGROUND_COLOR, height = Data.Y_HEIGHT, width=Data.X_WIDTH)
        self.canvas.pack()
        for x in range(self.elements_x):
            for y in range(self.elements_y):
                if aField[x][y]:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(
                                        x*Data.PIXEL_SIZE,
                                        y*Data.PIXEL_SIZE,
                                        x*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        y*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        fill = color)
            
    def repaint(self):
        aField = self.berechnung.get_data_object(right_puncher_up = self.puncher_up, right_puncher_down = self.puncher_down)
        self.canvas.delete()
        for x in range(self.elements_x):
            for y in range(self.elements_y):
                if aField[x][y]:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(
                                        x*Data.PIXEL_SIZE,
                                        y*Data.PIXEL_SIZE,
                                        x*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        y*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        fill = color
                                        )
        self.app.after(1, self.repaint)