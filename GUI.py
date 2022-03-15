import tkinter as tk
import Data

class GUI:
    def __init__(self):

        self.app = tk.Tk()
        self.app.geometry(str(Data.X_WIDTH) + "x" + str(Data.Y_HEIGHT))
        self.app.title("Pong")
    def repaint(self, aField):
        elements_x = int(Data.X_WIDTH / Data.PIXEL_SIZE)
        elements_y = int(Data.Y_HEIGHT / Data.PIXEL_SIZE)
        self.canvas = tk.Canvas(self.app, bg = Data.BACKGROUND_COLOR, height = Data.Y_HEIGHT, width=Data.X_WIDTH)
        self.canvas.pack()
        for x in range(elements_x):
            for y in range(elements_y):
                if aField[x][y]:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(
                                        x*Data.PIXEL_SIZE,
                                        y*Data.PIXEL_SIZE,
                                        x*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        y*Data.PIXEL_SIZE+Data.PIXEL_SIZE, 
                                        fill = color, 
                                        tag = str(x)+":"+str(y))
        self.app.mainloop()

NR_X_ELEMENTS = int(Data.X_WIDTH/ Data.PIXEL_SIZE)
NR_Y_ELEMENTS = int(Data.Y_HEIGHT/Data.PIXEL_SIZE)
arr = []
counter = 0
for x in range(NR_X_ELEMENTS):
            arr.append([])
            for y in range(NR_Y_ELEMENTS):
                counter += 1
                if counter%2 == 0:
                    arr[x].append(False)
                else:
                    arr[x].append(True)


gui = GUI()
gui.repaint(arr)