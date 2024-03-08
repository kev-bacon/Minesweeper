from tkinter import Button, Label
import random
import settings
class Cell: 
    all = [] 
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.x = x 
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None
    
        # Append the object to the Cell.all list
        Cell.all.append(self)
    def create_btn_object(self,location):
        btn = Button(
            location, 
            width=12, 
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions) #Left click
        btn.bind('<Button-2>', self.right_click_actions) #Right click
        self.cell_btn_object = btn 
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg= "black",
            foreground="white",
            text = f"Cells Left:{settings.CELL_COUNT}",
            width=12, 
            height=4,
            font=("", 30)
        ) 
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event): 
        if self.is_mine: 
            self.show_mine()
        else: 
            if self.surronded_cells_mines_length == 0: 
                for cell in self.surronded_cells: 
                    cell.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x,y):      
        #return cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell 
    @property
    def surronded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None]        
        return cells

    @property
    def surronded_cells_mines_length(self):
        counter = 0 
        for cell in self.surronded_cells: 
            if cell.is_mine: 
                counter += 1 
        return counter

    def show_cell(self): 
        self.cell_btn_object.configure(text=self.surronded_cells_mines_length)

    def show_mine(self): 
        # a logic to interrupt the game and display a message that player has lost!
        self.cell_btn_object.configure(text="NOOO! MINE")

    def right_click_actions(self, event): 
        print(event)
        print("I am right clicked!")
        self.text = "Right-clicked"
    
    @staticmethod
    def randomize_mines(): 
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    def __repr__(self):
        return f"Cell({self.y}, {self.x})"