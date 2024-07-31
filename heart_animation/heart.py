import turtle
import time

window = turtle.Screen()
window.title("from Yasinov to someone")
window.bgcolor("black")
window.setup(width=800, height=600) 

t = turtle.Turtle()
t.speed(1)
t.width(2)

def draw_heart():
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()

def draw_text():
    t.up()
    t.goto(0, -10) 
    t.color("white")
    t.write("Love Youuu", align="center", font=("Arial", 25, "bold"))

def propose_animation():
    t.hideturtle()
    t.penup()
    t.goto(0, -200)
    t.showturtle()
    t.speed(2)
    t.pendown()
    draw_heart()
    draw_text()
    t.hideturtle()

def main():
    propose_animation()
    window.mainloop()

if __name__ == "__main__":
    main()
