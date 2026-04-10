from tkinter import Tk, BOTH, Canvas, Entry, Button, Label


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create the main window
        self.__root = Tk()
        self.__root.title("Maze Solver")


        # Create a Canvas widget
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.add_entry_fields()

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def add_entry_fields(self):
        # Create Game Title
        self.__canvas.create_text(
            780, 40,
            text="MAZE SOLVER",
            font=("Georgia", 36, "bold"),
            fill="blue"
        )

        # Create field labels
        label_rows = Label(self.__root, text="Qty of Rows:", anchor='w', font=('Arial', 12), bg="white", fg="grey")
        label_cols = Label(self.__root, text="Qty of Columns:", anchor='w', font=('Arial, 12'), bg="white", fg="grey")
        self.__canvas.create_window(90, 865, window=label_rows)
        self.__canvas.create_window(325, 865, window=label_cols)

 
        # Create the entry widgets
        self.entry_rows = Entry(self.__root, width = 5, font=('Arial', 18))
        self.entry_cols = Entry(self.__root, width = 5, font=('Arial', 18))

        # Embed it on the canvas
        self.__canvas.create_window(190, 865, window=self.entry_rows)
        self.__canvas.create_window(440, 865, window=self.entry_cols)

        # Set default values to entry fields
        self.entry_rows.insert(20, "20")
        self.entry_cols.insert(30, "30")

        submit_button = Button(
            self.__root,
            text="Submit",
            command=self.get_entry_text,
            bg="#4CAF50",   # Green background
            fg="white",       # White text
            activebackground="#45a049" # Darker green when clicked
            )
        self.__canvas.create_window(540, 865, window=submit_button)
    

    def get_entry_text(self):
        print("Rows: ", self.entry_rows.get())
        print("Columns: ", self.entry_cols.get())


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