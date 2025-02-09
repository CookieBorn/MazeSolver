from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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






    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
