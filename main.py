from tkinter import Tk, BOTH, Canvas
from window_class import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze=Maze(0,0, 20,30, 0,0,win)
    win.wait_for_close()


main()
