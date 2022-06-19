from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 180
LEFT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segemnt(position)


    def add_segemnt(self, position):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)

    def extend_snake(self):
        self.add_segemnt(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.segments[0].heading() != DOWN:
            if self.segments[0].heading() == RIGHT:
                self.segments[0].right(90)
            else:
                self.segments[0].left(90)
    def down(self):
        if self.segments[0].heading() != UP:
            if self.segments[0].heading() == RIGHT:
                self.segments[0].left(90)
            else:
                self.segments[0].right(90)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            if self.segments[0].heading() == DOWN:
                self.segments[0].right(90)
            else:
                self.segments[0].left(90)


    def right(self):
        if self.segments[0].heading() != LEFT:
            if self.segments[0].heading() == DOWN:
                self.segments[0].left(90)
            else:
                self.segments[0].right(90)
