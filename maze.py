from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._cells=[]
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls(0,0)
        self._reset_cells_visited()

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
            if i>1:
                points.append((i-1,j))
            if j>1:
                points.append((i,j-1))
            if i<self.num_cols-1:
                points.append((i+1,j))
            if j<self.num_rows-2:
                points.append((i,j+1))
            for point in points:
                if self._cells[point[0]][point[1]].visited is False:
                    possible_directions_to_move.append(point)
            if len(possible_directions_to_move)==0:
                self._draw_cell(i,j)
                return
            rand_int=random.randrange(0,len(possible_directions_to_move))
            rand_cell=possible_directions_to_move[rand_int]
            if rand_cell[1]<j:
                self._cells[i][j].down_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].up_wall=False
            if rand_cell[1]>j:
                self._cells[i][j].up_wall=False
                self._cells[rand_cell[0]][rand_cell[1]].down_wall=False
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






    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
