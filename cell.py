from tkinter.constants import FALSE
from point import Point
from line import Line



class Cell:
    def __init__(self,win, top_left_point, bottom_right_point, left_wall=True, right_wall=True, up_wall=True, down_wall=True):
        self.left_wall=left_wall
        self.right_wall=right_wall
        self.up_wall=up_wall
        self.down_wall=down_wall
        self._x1=top_left_point.x
        self._x2=bottom_right_point.x
        self._y1=top_left_point.y
        self._y2=bottom_right_point.y
        self._win=win

    def draw(self):
        bottom_left=Point(self._x1, self._y2)
        top_right=Point(self._x2, self._y1)
        top_left_point=Point(self._x1,self._y1)
        bottom_right_point=Point(self._x2, self._y2)
        if self.left_wall is True:
            line=Line(top_left_point, bottom_left)
            self._win.draw_line(line,"black")
        if self.right_wall is True:
            line=Line(top_right, bottom_right_point)
            self._win.draw_line(line,"black")
        if self.up_wall is True:
            line=Line(top_left_point, top_right)
            self._win.draw_line(line,"black")
        if self.down_wall is True:
            line=Line(bottom_right_point, bottom_left)
            self._win.draw_line(line,"black")

    def draw_move(self, to_cell, undo=False):
        self_centre=Point((self._x1+self._x2)/2,(self._y1+self._y2)/2)
        to_cell_centre=Point((to_cell._x1+to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2)
        if undo is False:
           line=Line(self_centre, to_cell_centre)
           self._win.draw_line(line, "red")
        else:
            line=Line(self_centre, to_cell_centre)
            self._win.draw_line(line, "grey")
