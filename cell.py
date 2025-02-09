
from point import Point
from line import Line



class Cell:
    def __init__(self,win=None, left_wall=True, right_wall=True, up_wall=True, down_wall=True):
        self.left_wall=left_wall
        self.right_wall=right_wall
        self.up_wall=up_wall
        self.down_wall=down_wall
        self._x1=None
        self._x2=None
        self._y1=None
        self._y2=None
        self._win=win

    def draw(self,x1,x2,y1,y2):
        if self._win is None:
            return
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        bottom_left=Point(self._x1, self._y2)
        top_right=Point(self._x2, self._y1)
        top_left_point=Point(self._x1,self._y1)
        bottom_right_point=Point(self._x2, self._y2)
        if self.left_wall is True:
            line=Line(top_left_point, bottom_left)
            self._win.draw_line(line,"black")
        elif self.left_wall is False:
            line=Line(top_left_point, bottom_left)
            self._win.draw_line(line,"light grey")
        if self.right_wall is True:
            line=Line(top_right, bottom_right_point)
            self._win.draw_line(line,"black")
        elif self.right_wall is False:
            line=Line(top_right, bottom_right_point)
            self._win.draw_line(line,"light grey")
        if self.up_wall is True:
            line=Line(top_left_point, top_right)
            self._win.draw_line(line,"black")
        elif self.up_wall is False:
            line=Line(top_left_point, top_right)
            self._win.draw_line(line,"light grey")
        if self.down_wall is True:
            line=Line(bottom_right_point, bottom_left)
            self._win.draw_line(line,"black")
        elif self.down_wall is False:
            line=Line(bottom_right_point, bottom_left)
            self._win.draw_line(line,"light grey")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        self_centre=Point((self._x1+self._x2)//2,(self._y1+self._y2)//2)
        to_cell_centre=Point((to_cell._x1+to_cell._x2)//2,(to_cell._y1+to_cell._y2)//2)
        if undo is False:
           line=Line(self_centre, to_cell_centre)
           self._win.draw_line(line, "red")
        else:
            line=Line(self_centre, to_cell_centre)
            self._win.draw_line(line, "grey")
