from tkinter import Tk, BOTH, Canvas
from window_class import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    p1=Point(10,10)
    p2=Point(400,300)
    p3=Point(790,590)
    cell=Cell(win, p1,p2,True,False,True, False)
    cell2=Cell(win,p2,p3,False,True,False,True)
    cell.draw()
    cell2.draw()
    win.wait_for_close()


main()
