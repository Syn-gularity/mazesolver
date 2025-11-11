from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = window
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()

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

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.__draw_cell(self.num_rows-1,self.num_cols-1)
