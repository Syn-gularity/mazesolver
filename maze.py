from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = window
        self.__seed = random.seed()
        if seed:
            random.seed(seed)
        

        self.__cells = []

        self.__create_cells()
        time.sleep(100)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(self.__win))
            self.__cells.append(row)
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cell(i,j)

    def __draw_cell(self,i,j):
        x = self.x1 + j*self.cell_size_x
        y = self.y1 + i*self.cell_size_y
        self.__cells[i][j].draw(x,y,x+self.cell_size_x,y+self.cell_size_y)
        self.__animate()

    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.__draw_cell(self.num_rows-1,self.num_cols-1)

    def __reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__cells[i][j].visited = False

    def __break_walls_r(self,i,j): #0left,1top,2right,3bottom
        print(self.__cells[i][j].visited)
        self.__cells[i][j].visited = True
        while True:
            print(f"x: {i} y: {j}")
            #if i == 0 and j == 0:
            #    break
            frontier = []
            if j>0 and not self.__cells[i][j-1].visited:
                frontier.append((i,j-1))
            if i>0 and not self.__cells[i-1][j].visited:
                frontier.append((i-1,j))
            if j<self.num_cols-1 and not self.__cells[i][j+1].visited:
                frontier.append((i,j+1))
            if i<self.num_rows-1 and not self.__cells[i+1][j].visited:
                frontier.append((i+1,j))
            if len(frontier) == 0:
                self.__draw_cell(i,j)
                return
            direction = random.randrange(len(frontier))
            (new_i, new_j) = frontier[direction]
            if i>new_i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
            elif i<new_i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
            elif j<new_j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False
            else:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
            if self.__cells[new_i][new_j].visited:
                break
            self.__break_walls_r(new_i,new_j)

            """
            
            direction = random.randint(0,3)
            #print(direction)
            if direction == 0 and j>0 and not self.__cells[i][j-1].visited:
                self.__cells[i][j].has_left_wall = False
                self.__draw_cell(i,j)
                self.__cells[i][j].visited = True
                self.__break_walls_r(i,j-1)
                valid = True
            elif direction == 1 and i>0 and not self.__cells[i-1][j].visited:
                self.__cells[i][j].has_top_wall = False
                self.__draw_cell(i,j)
                self.__cells[i][j].visited = True
                self.__break_walls_r(i-1,j)
                
                valid = True
            elif direction == 2 and j<self.num_cols-1 and not self.__cells[i][j+1].visited:
                self.__cells[i][j].has_right_wall = False
                self.__draw_cell(i,j)
                self.__cells[i][j].visited = True
                self.__break_walls_r(i,j+1)
                valid = True
            elif direction == 3 and i<self.num_rows-1 and not self.__cells[i+1][j].visited:
                self.__cells[i][j].has_bottom_wall = False
                self.__draw_cell(i,j)
                self.__cells[i][j].visited = True
                self.__break_walls_r(i+1,j)
                valid = True"""

            
