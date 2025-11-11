from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(5,8), Point(300,400)))
    win.wait_for_close()
    

main()
