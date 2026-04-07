from cell import Cell
import random
import time


class Maze():
    def __init__(
        self,
        num_rows,
        num_cols,
        win = None,
        seed = None
    ):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__win = win

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
    

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)


    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        
        margin = 64
        grid_width = self.__win.width - margin
        grid_height = self.__win.height - margin

        gw_c_size = grid_width / self.__num_cols
        gh_c_size = grid_height / self.__num_rows

        win_w = self.__win.width / 2
        win_h = self.__win.height / 2
        grid_w = grid_width / 2
        grid_h = grid_height / 2

        start_point_x1 = win_w - grid_w
        start_point_y1 = win_h - grid_h

        x1 = start_point_x1 + i * gw_c_size
        y1 = start_point_y1 + j * gh_c_size
        x2 = x1 + gw_c_size
        y2 = y1 + gh_c_size
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()


    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.0005)
    

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
