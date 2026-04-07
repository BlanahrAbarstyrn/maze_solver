from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create the main window
        self.__root = Tk() #
        self.__root.title("Maze Solver") #

        # Create a Canvas widget
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white") #
        self.__canvas.pack(fill=BOTH, expand=1) #

        self.__running = False #

        self.__root.protocol("WM_DELETE_WINDOW", self.close) #


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    

    def close(self):
        self.__running = False
    

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


class Line():
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
    

    def draw(self, tk_canvas, fill_color="black"):
        tk_canvas.create_line(
        self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
)