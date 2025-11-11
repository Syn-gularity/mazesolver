from graphics import Point, Line

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
        left = Line(Point(self.__x1,self.__y1),Point(self.__x1, self.__y2))
        right = Line(Point(self.__x2,self.__y1),Point(self.__x2, self.__y2))
        top = Line(Point(self.__x1,self.__y1),Point(self.__x2, self.__y1))
        bottom = Line(Point(self.__x1,self.__y2),Point(self.__x2, self.__y2))
        if self.has_left_wall:
            self.__win.draw_line(left)
        else:
            self.__win.draw_line(left,"white")
        if self.has_right_wall:
            self.__win.draw_line(right)
        else:
            self.__win.draw_line(right,"white")
        if self.has_top_wall:
            self.__win.draw_line(top)
        else:
            self.__win.draw_line(top,"white")
        if self.has_bottom_wall:
            self.__win.draw_line(bottom)
        else:
            self.__win.draw_line(bottom,"white")
    
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