from window import Window
from maze import Maze


def main():
    num_rows = 4
    num_cols = 4
    screen_x = 1600
    screen_y = 900
    win = Window(screen_x, screen_y)

    Maze(num_rows, num_cols, win, 0)

    win.wait_for_close()


main()