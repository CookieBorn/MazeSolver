from tkinter import Tk, BOTH, Canvas
from window_class import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    p1=Point(0,300)
    p2=Point(800,300)
    p3=Point(400,600)
    p4=Point(400,0)
    l1=Line(p1,p2)
    l2=Line(p3,p4)
    win.draw_line(l2, "black")
    win.draw_line(l1, "red")
    win.wait_for_close()


main()
