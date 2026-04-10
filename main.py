from window import Window
from maze import Maze


def main():
    screen_x = 1600
    screen_y = 900


    def on_submit(num_rows, num_cols):
        # change None to a fixed number to have same
        # maze generate every run for testing purposes
        # or to compare solving algorithms
        if num_rows < 2:
            num_rows = 2
        if num_rows > 20:
            num_rows = 20
        if num_cols < 2:
            num_cols = 2
        if num_cols > 30:
            num_cols = 30
        maze = Maze(num_rows, num_cols, win, None)
        maze.solve()


    win = Window(screen_x, screen_y, on_submit)
    win.wait_for_close()


main()