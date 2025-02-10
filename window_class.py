from tkinter import *
from maze import Maze

class Window:
    def __init__(self, width, height, run=None):
        self.height=height
        self.width=width
        self.run=run
        self.root=Tk()
        self.root.title("Maze")
        self.canvas=Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running=False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        label1=Label(self.root, text="Number of Rows")
        self.canvas.create_window(100,20, window=label1)

        self.num_rows_input=Entry(self.root)
        self.canvas.create_window(100, 50, window=self.num_rows_input)

        label2=Label(self.root, text="Number of Columns")
        self.canvas.create_window(100,80, window=label2)

        self.num_col_input=Entry(self.root)
        self.canvas.create_window(100, 110, window=self.num_col_input)

        label3=Label(self.root, text="Seed")
        self.canvas.create_window(100,140, window=label3)

        self.seed_input=Entry(self.root)
        self.canvas.create_window(100, 170, window=self.seed_input)

        button_run=Button(text="Run", command=self.run_maze, background="green")
        self.canvas.create_window(100,200,window=button_run)



    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running=True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running=False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def input_get(self,func):
        return int(func.get())

    def run_maze(self):

        num_col=int(self.num_col_input.get())
        num_rows=int(self.num_rows_input.get())
        seed=int(self.seed_input.get())
        size_x=(800-220)//num_col
        size_y=(600-20)//num_rows

        self.canvas.create_rectangle(200,10, (self.width)-10, (self.height)-10, fill="light grey")
        maze=Maze(200,10, num_rows,num_col, size_x,size_y, self,seed)
