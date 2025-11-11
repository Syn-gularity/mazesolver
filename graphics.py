from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return
        if self.has_left_wall:
            left = Line(Point(self.__x1,self.__y1),Point(self.__x1, self.__y2))
            self.__win.draw_line(left)
        if self.has_right_wall:
            right = Line(Point(self.__x2,self.__y1),Point(self.__x2, self.__y2))
            self.__win.draw_line(right)
        if self.has_top_wall:
            top = Line(Point(self.__x1,self.__y1),Point(self.__x2, self.__y1))
            self.__win.draw_line(top)
        if self.has_bottom_wall:
            bottom = Line(Point(self.__x1,self.__y2),Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom)
    
    def __mid2Points(self, x1,y1,x2,y2):
        return Point((x1+x2)/2, (y1+y2)/2)

    def draw_move(self, to_cell, undo=False):
        if self.__win == None:
            return
        mid1 = self.__mid2Points(self.__x1,self.__y1,self.__x2,self.__y2)
        mid2 = self.__mid2Points(to_cell.__x1,to_cell.__y1,to_cell.__x2,to_cell.__y2)
        line = Line(mid1,mid2)
        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")

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


