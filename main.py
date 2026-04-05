from window import Window
from maze import Maze


def main():
    num_rows = 10
    num_cols = 14
    screen_x = 800
    screen_y = 600
    cell_size = 50
    win = Window(screen_x, screen_y)

    maze = Maze(num_rows, num_cols, cell_size, win)

    win.wait_for_close()


main()