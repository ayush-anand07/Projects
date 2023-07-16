from turtle import Turtle, update, write 
from food import Food


class ScoreBoard(Turtle):

    def __init__(self):
        super(). __init__()
        self.hideturtle()
        self.color("white") 
        self.score = 0
        self.data= open(r"C:\Users\ayush\OneDrive\Desktop\PYTHON\Intermediate\snake\data.txt")
        self.high_score = int(self.data.read())
        self.penup()
        self.goto(x=0, y= 250)
        self.write(arg= (f"Score: {self.score}"), align="Center", font=("Arial", 24, "normal"))
        self.data.close()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="Center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.data= open(r"C:\Users\ayush\OneDrive\Desktop\PYTHON\Intermediate\snake\data.txt", mode= "w")
            self.data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

   
   
   
    def update_score(self):
        self.score+=1
        self.clear()
        self.write(arg= (f"Score: {self.score}"), align="Center", font=("Arial", 24, "normal"))
        

        

        
        
