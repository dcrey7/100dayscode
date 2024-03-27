from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

          

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
    def up(self):        
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    

    def left(self):
        
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)