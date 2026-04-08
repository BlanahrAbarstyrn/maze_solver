from window import Window
from maze import Maze


def main():
    num_rows = 20
    num_cols = 30
    screen_x = 1600
    screen_y = 900
    win = Window(screen_x, screen_y)

    # change None to a fixed number to have same
    # maze generate every run for testing purposes
    # or to compare solving algorithms
    maze = Maze(num_rows, num_cols, win, None)
    maze.solve()

    win.wait_for_close()


main()