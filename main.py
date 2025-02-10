from tkinter import Tk, BOTH, Canvas
from window_class import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    num_rows=5
    num_col=5
    size_x=(800-20)//num_col
    size_y=(600-20)//num_rows
    maze=Maze(10,10, num_rows,num_col, size_x,size_y,win)
    win.wait_for_close()


main()
