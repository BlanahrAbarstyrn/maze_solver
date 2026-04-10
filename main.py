from window import Window
from maze import Maze


def main():
    screen_x = 1600
    screen_y = 900


    def on_submit(num_rows, num_cols):
        # change None to a fixed number to have same
        # maze generate every run for testing purposes
        # or to compare solving algorithms
        maze = Maze(num_rows, num_cols, win, None)
        maze.solve()


    win = Window(screen_x, screen_y, on_submit)
    win.wait_for_close()


main()