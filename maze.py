from graphics import Cell
import random
import time


class Maze():
    def __init__(
        self,
        num_rows,
        num_cols,
        cell_size,
        win = None,
    ):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size = cell_size
        self.__win = win

        self.__cells = []

        self.__justdDrawAlready = Cell(win)

        self.__create_cells()
    

    def __create_cells(self):
        if self.__win is None:
            return
        
        gridWidth = self.__get_grid_width()
        gridHeight = self.__get_grid_height()

        if gridWidth > self.__win.width or gridHeight > self.__win.height:
            calc_new_cell_size_col = (self.__win.width - 40) / self.__num_cols
            calc_new_cell_size_row = (self.__win.height - 40) / self.__num_rows
            if calc_new_cell_size_col < calc_new_cell_size_row:
                self.__cell_size = calc_new_cell_size_col
                gridWidth = self.__get_grid_width()
                gridHeight = self.__get_grid_height()
            else:
                self.__cell_size = calc_new_cell_size_row
                gridWidth = self.__get_grid_width()
                gridHeight = self.__get_grid_height()

        W1 = self.__win.width / 2
        H1 = self.__win.height / 2
        W2 = gridWidth / 2
        H2 = gridHeight / 2

        x1 = W1 - W2
        y1 = H1 - H2


        i = x1
        j = y1
        while i < self.__num_cols * self.__cell_size + x1:
            while j < self.__num_rows * self.__cell_size + y1:
                i2 = i + self.__cell_size
                j2 = j + self.__cell_size
                self.__cells.append([i, j, i2, j2])
                j += self.__cell_size
            i += self.__cell_size
            j = y1
        #print(self.__cells)
        #print(len(self.__cells))
        self.__draw_cell()



    def __draw_cell(self):
        if self.__win is None:
            return
        
        i = 0
        while i < len(self.__cells):
            x1 = self.__cells[i][0]
            y1 = self.__cells[i][1]
            x2 = self.__cells[i][2]
            y2 = self.__cells[i][3]
            self.__justdDrawAlready.draw(x1,y1,x2,y2)
            i += 1
            self.__animate()



    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.005)
    

    def __get_grid_width(self):
        return self.__num_cols * self.__cell_size


    def __get_grid_height(self):
        return self.__num_rows * self.__cell_size