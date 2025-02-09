from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._cells=[]
        self._create_cells()

    def _create_cells(self):
        cell_row=[]
        i=0
        for i in range(self.num_cols):
            cell_row.append(Cell(self.win))
            i+=1
        i=0
        for i in range(self.num_rows):
            self._cells.append(cell_row)
            i+=1

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        self.cell_size_x=(self.win.width-20)//self.num_rows
        self.cell_size_y=(self.win.height-20)//self.num_cols
        self.x1=10
        self.y1=10
        x1=self.x1+(i+0.5)*self.cell_size_x-0.5*self.cell_size_x
        x2=self.x1+(i+0.5)*self.cell_size_x+0.5*self.cell_size_x
        y1=self.y1+(j+0.5)*self.cell_size_y-0.5*self.cell_size_y
        y2=self.y1+(j+0.5)*self.cell_size_y+0.5*self.cell_size_y
        cell=self._cells[i][j]
        cell.draw(x1,x2,y1,y2)
        self._animate()






    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
