from graphics import Window, Line, Point, Cell, Maze

def main():
    win = Window(800, 600)

    """c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50,50,75,75)
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(75,50,100,75)
    c1.draw_move(c2, True)"""

    maze = Maze(10, 10, 3, 2, 10, 10, win)


    win.wait_for_close()
    

main()
