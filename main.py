from tkinter import Tk, BOTH, Canvas
from window_class import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    size_x=(600-20)//20
    size_y=(800-20)//30
    maze=Maze(10,10, 10,10, size_x,size_y,win)
    win.wait_for_close()


main()
