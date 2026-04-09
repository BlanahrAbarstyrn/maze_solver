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
        # if statement needed to be moved above
        # calling other methods, otherwise the
        # seed could not be made static for testing
        if seed is not None:
            random.seed(seed)
        
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__win = win

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()


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
        
        # Not part of guided project
        # Find maximum size of grid less margin
        margin = 64
        grid_width = self.__win.width - margin
        grid_height = self.__win.height - margin

        # find maximum cell size
        # (guided project had cell size as a predetermined fixed value)
        gw_c_size = grid_width / self.__num_cols
        gh_c_size = grid_height / self.__num_rows

        # have maze grid utilize the full window and be centered
        # find center of window
        win_w = self.__win.width / 2
        win_h = self.__win.height / 2
        # find center of grid
        grid_w = grid_width / 2
        grid_h = grid_height / 2

        # subtract to find the x/y starting point for cell 0,0
        start_point_x1 = win_w - grid_w
        start_point_y1 = win_h - grid_h

        # resume guided project
        # logic to send to the draw method to create full grid
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
        # may need to set up conditionals for timer to speed up
        # or slow down based on the grid size
        time.sleep(0.0005)
    

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    

    def __break_walls_r(self, i, j):
        # mark current cell visited
        self.__cells[i][j].visited = True

        #print(type(self.__cells[i + 1][j]))
        #print(dir(self.__cells[i + 1][j]))


        while True:

            # build list of unvisited neighbors
            unvisited_neighbor_cells = []

            # left   (i - 1, j)
            # right  (i + 1, j)
            # up     (i, j - 1)
            # down   (i, j + 1)

            if i - 1 >= 0 and self.__cells[i - 1][j].visited == False:
                unvisited_neighbor_cells.append((i - 1, j))
            if i + 1 <= self.__num_cols - 1 and self.__cells[i + 1][j].visited == False:
                unvisited_neighbor_cells.append((i + 1, j))
            if j - 1 >= 0 and self.__cells[i][j - 1].visited == False:
                unvisited_neighbor_cells.append((i, j - 1))
            if j + 1 <= self.__num_rows - 1 and self.__cells[i][j + 1].visited == False:
                unvisited_neighbor_cells.append((i, j + 1))

            # if none, draw and return
            if unvisited_neighbor_cells == []:
                self.__draw_cell(i, j)
                return
            
            # choose one random neighbor
            # random.randrange(start, stop[, step])
            # Python interprets below as random.randrange(0, len(unvisted_neighbor_cells)), step is optional
            index_choice = random.randrange(len(unvisited_neighbor_cells))
            next_cell = unvisited_neighbor_cells[index_choice]
            #print(next_cell)

            # remove walls between current cell and neighbor

            # next_cell is a tuple, so to access the values use [0] and [1]
            # next_cell does not have .has_xxx_wall access, so must use self.__cells
            # to access next_cell's location

            # did we move left?
            if next_cell[0] < i and next_cell[1] == j:
                self.__cells[i - 1][j].has_right_wall = False
                self.__cells[i][j].has_left_wall = False

            # did we move right?
            if next_cell[0] > i and next_cell[1] == j:
                self.__cells[i + 1][j].has_left_wall = False
                self.__cells[i][j].has_right_wall = False

            # did we move up?
            if next_cell[1] < j and next_cell[0] == i:
                self.__cells[i][j - 1].has_bottom_wall = False
                self.__cells[i][j].has_top_wall = False

            # did we move down?
            if next_cell[1] > j and next_cell[0] == i:
                self.__cells[i][j + 1].has_top_wall = False
                self.__cells[i][j].has_bottom_wall = False

            # recurse into neighbor
            self.__break_walls_r(next_cell[0], next_cell[1])



    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
        #print(f"visiting {i}, {j}")
        self.__animate()

        # mark current cell as visited
        self.__cells[i][j].visited = True

        # if exit cell has been reached, return
        if i == self.__num_cols -1 and j == self.__num_rows -1:
            return True
        
        # left   (i - 1, j)
        # right  (i + 1, j)
        # up     (i, j - 1)
        # down   (i, j + 1)


        # trying left
        if i > 0 and self.__cells[i - 1][j].visited == False and self.__cells[i][j].has_left_wall == False:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], False)
            if self._solve_r(i - 1, j):
                return True
            self.__cells[i - 1][j].draw_move(self.__cells[i][j], True)
        
        # trying right
        if i < self.__num_cols -1 and self.__cells[i + 1][j].visited == False and self.__cells[i][j].has_right_wall == False:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], False)
            if self._solve_r(i + 1, j):
                return True
            self.__cells[i + 1][j].draw_move(self.__cells[i][j], True)
        
        # trying up
        if j > 0 and self.__cells[i][j - 1].visited == False and self.__cells[i][j].has_top_wall == False:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], False)
            if self._solve_r(i, j - 1):
                return True
            self.__cells[i][j - 1].draw_move(self.__cells[i][j], True)

        # trying down
        if j < self.__num_rows - 1 and self.__cells[i][j + 1].visited == False and self.__cells[i][j].has_bottom_wall == False:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], False)
            if self._solve_r(i, j + 1):
                return True
            self.__cells[i][j + 1].draw_move(self.__cells[i][j], True)

        return False