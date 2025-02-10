from cell import Cell
import time
import random
from tkinter import Tk, BOTH, Canvas


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self.text_box=Canvas(Tk(), width=self.win.width/4,height=self.win.height/4)
        self._cells=[]
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls(0,0)
        self._reset_cells_visited()
        self.solve()
        if self.solve() is True:
            self.win.canvas.create_oval((self.win.width/8)*3,(self.win.height/8)*3, (self.win.width/8)*5, (self.win.height/8)*5, fill="white")
            self.win.canvas.create_text(self.win.width/2,self.win.height/2, text="Solution Found!!", fill="green", font=('Helvetica 15 bold'))
        elif self.solve() is False:
            self.win.canvas.create_oval((self.win.width/8)*3,(self.win.height/8)*3, (self.win.width/8)*5, (self.win.height/8)*5, fill="white")
            self.win.canvas.create_text(self.win.width/2,self.win.height/2, text="No Solution Found!!", fill="red", font=('Helvetica 15 bold'))


    def _create_cells(self):
        for j in range(self.num_cols):
            cell_row=[]
            for i in range(self.num_rows):
                cell_row.append(Cell(self.win))
                i+=1
            self._cells.append(cell_row)
            j+=1

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1=self.x1+(i+0.5)*self.cell_size_x-0.5*self.cell_size_x
        x2=self.x1+(i+0.5)*self.cell_size_x+0.5*self.cell_size_x
        y1=self.y1+(j+0.5)*self.cell_size_y-0.5*self.cell_size_y
        y2=self.y1+(j+0.5)*self.cell_size_y+0.5*self.cell_size_y
        cell=self._cells[i][j]
        cell.draw(x1,x2,y1,y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].up_wall=False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].down_wall=False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls(self, i, j):
        self._cells[i][j].visited=True
        while 1<2:
            possible_directions_to_move=[]
            points=[]
            if i>0:
                points.append((i-1,j))
            if j>0:
                points.append((i,j-1))
            if i<self.num_cols-1:
                points.append((i+1,j))
            if j<self.num_rows-1:
                points.append((i,j+1))
            for point in points:
                if self._cells[point[0]][point[1]].visited is False:
                    possible_directions_to_move.append(point)
            if len(possible_directions_to_move)==0:
                self._draw_cell(i,j)
                return
            rand_int=random.randrange(len(possible_directions_to_move))
            rand_cell=possible_directions_to_move[rand_int]
            if rand_cell[1]<j:
                self._cells[i][j].up_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].down_wall=False
            if rand_cell[1]>j:
                self._cells[i][j].down_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].up_wall=False
            if rand_cell[0]>i:
                self._cells[i][j].right_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].left_wall=False
            if rand_cell[0]<i:
                self._cells[i][j].left_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].right_wall=False
            self._break_walls(rand_cell[0],rand_cell[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited=False

    def solve(self):
        final=self._solve_r(0,0)
        return final

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited=True
        cell=self._cells[i][j]
        end = self._cells[self.num_cols-1][self.num_rows-1]
        if end.visited is True:
            return True
        if i>0 and cell.left_wall is False and self._cells[i-1][j].visited is False:
            cell.draw_move(self._cells[i-1][j])
            final=self._solve_r(i-1,j)
            if final is True:
                return final
            else:
                cell.draw_move(self._cells[i-1][j], True)
        if j>0 and cell.up_wall is False and self._cells[i][j-1].visited is False:
            cell.draw_move(self._cells[i][j-1])
            final=self._solve_r(i,j-1)
            if final is True:
                return final
            else:
                cell.draw_move(self._cells[i][j-1], True)
        if i<self.num_cols-1 and cell.right_wall is False and self._cells[i+1][j].visited is False:
            cell.draw_move(self._cells[i+1][j])
            final=self._solve_r(i+1,j)
            if final is True:
                return final
            else:
                cell.draw_move(self._cells[i+1][j], True)
        if j<self.num_rows-1 and cell.down_wall is False and self._cells[i][j+1].visited is False:
            cell.draw_move(self._cells[i][j+1])
            final=self._solve_r(i,j+1)
            if final is True:
                return final
            else:
                cell.draw_move(self._cells[i][j+1], True)
        return False







    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
