from turtle import Turtle, Screen

STARTING_POSITION = (0,0)

class Snake:
    def __init__(self):
        self.segments = []
        self.distance = 20
        self.dir = 0
        self.current_dir = 0
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(3):
            seg = Turtle("square")
            seg.goto(0,0)
            seg.color("white")
            seg.penup()
            seg.backward(i * 20)
            self.segments.append(seg)
        self.head = self.segments[0]


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):

            if i != 0:
                next = self.segments[i - 1].position()
                self.segments[i].goto(next[0], next[1])
        self.head.setheading(self.dir)
        self.current_dir = self.dir
        self.head.forward(self.distance)

    def set_dir(self,next_dir):
        inverse = {"270": 90, "90": 270, "0": 180 , "180": 0}
        if self.current_dir != inverse[f"{next_dir}"]:
            self.dir = next_dir

    def check_wall(self):
        return self.head.xcor() < -290 or self.head.xcor() > 290 or self.head.ycor() < -290 or self.head.ycor() > 290

    def check_tail(self):
        touching_tail = False
        tail_arr = self.segments[2:]
        for seg in tail_arr:
            if self.head.distance(seg) < 15:
                touching_tail = True
        return touching_tail

    def eat_food(self):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        self.segments.append(seg)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

