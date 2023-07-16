from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT= 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()

    def creat_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    
    def move(self):

        for seg_num in range(len(self.segments)-1 ,  0,  -1 ):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y )
        self.segments[0].forward(MOVE_DISTANCE)    
       

    def up(self):
        if self.segments[0].heading() != DOWN:
         self.segments[0].setheading(UP)
       
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
         self.segments[0].setheading(LEFT)
    
    def down(self):
        if self.segments[0].heading() != UP:
          self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
          self.segments[0].setheading(RIGHT)


    def increse_length(self):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.segments[-1].position())
            self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        