from window import Window
from maze import Maze


def main():
    num_rows = 20
    num_cols = 30
    screen_x = 800
    screen_y = 600
    cell_size = 20
    win = Window(screen_x, screen_y)

    Maze(num_rows, num_cols, cell_size, win)

    win.wait_for_close()


main()