from turtle import Turtle
import random
import string

INT_X = -300
INT_Y = -70

class Matrix:

    def __init__(self,no_of_rows, no_of_cols):
        self.rows = no_of_rows
        self.cols = no_of_cols
        self.line = Turtle()
        self.line.penup()
        self.line.goto(INT_X,INT_Y)
        self.setup_turtle()
        self.create_matrix()


    def draw_square(self):
        for _ in range(4):
            self.line.fd(50)
            self.line.left(90)

    
    def move_next_row(self):
        self.line.penup()
        self.line.left(90)
        self.line.fd(50)
        self.line.left(90)
        self.line.fd(self.cols*50)
        self.line.right(180)
        self.line.pendown()


    def setup_turtle(self):
        self.line.speed(0)
        self.line.pd()
        self.line.ht()
        self.line.pensize(3)
        self.line.color('white')


    def create_matrix(self):
        self.values = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.draw_square()
                self.line.fd(50)
            self.move_next_row()


    # def fill_values(self):
    #     alphabet = string.ascii_uppercase
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             auto_choice = random.choice(alphabet)
    #             self.values[i][j] = auto_choice 


    def fill_values(self, alpha):
        print("Getting random values")
        alphabet = list(alpha)
        for i in range(self.rows):
            for j in range(self.cols):
                auto_choice = random.choice(alphabet)
                self.values[i][j] = auto_choice 
                alphabet.remove(auto_choice)

                print(f"Auto choice: {auto_choice}")


        self.display_matrix()

        


    def display_matrix(self):
        self.line.penup()
        self.line.goto(INT_X,INT_Y)

        for i in range(self.rows):
            for j in range(self.cols):
                x_axis = INT_X + j * 50+17
                y_axis = INT_Y + i * 50+17
                self.line.goto(x_axis, y_axis)
                self.line.write(self.values[i][j], align="center", font=("Arial", 12, "normal"))