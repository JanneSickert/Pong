import turtle
import time

window = turtle.Screen()
window.title("M²J-Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0
# anzeige
anzeige = turtle.Turtle()
anzeige.speed(0)
anzeige.shape("square")
anzeige.color("white")
anzeige.penup()
anzeige.hideturtle()
anzeige.goto(0, 260)
anzeige.write("Spieler 1: 0  Spieler 2: 0", align="center", font=("Courier", 24, "normal"))

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# puncheer A
puncher_a = turtle.Turtle()
puncher_a.speed(0)
puncher_a.shape("square")
puncher_a.color("white")
puncher_a.shapesize(stretch_wid=5,stretch_len=1)
puncher_a.penup()
puncher_a.goto(-350, 0)

# puncher B
puncher_b = turtle.Turtle()
puncher_b.speed(0)
puncher_b.shape("square")
puncher_b.color("white")
puncher_b.shapesize(stretch_wid=5,stretch_len=1)
puncher_b.penup()
puncher_b.goto(350, 0)

# tastendruck funktionen
def puncher_a_up():
    y = puncher_a.ycor()
    y += 20
    puncher_a.sety(y)

def puncher_a_down():
    y = puncher_a.ycor()
    y -= 20
    puncher_a.sety(y)

def puncher_b_up():
    y = puncher_b.ycor()
    y += 20
    puncher_b.sety(y)

def puncher_b_down():
    y = puncher_b.ycor()
    y -= 20
    puncher_b.sety(y)

# tastendruck listener
window.listen()
window.onkeypress(puncher_a_up, "w")
window.onkeypress(puncher_a_down, "s")
window.onkeypress(puncher_b_up, "Up")
window.onkeypress(puncher_b_down, "Down")

# Main game loop
while True:
    time.sleep(0.0005)
    window.update()
    
    # ball bewegen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # seiten check

    # oben unten
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # links rechts
    if ball.xcor() > 350:
        score_a += 1
        anzeige.clear()
        anzeige.write("Spieler 1: {}  Spieler 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        anzeige.clear()
        anzeige.write("Spieler 1: {}  Spieler 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # puncher und ball kollision
    if ball.xcor() < -340 and ball.ycor() < puncher_a.ycor() + 50 and ball.ycor() > puncher_a.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < puncher_b.ycor() + 50 and ball.ycor() > puncher_b.ycor() - 50:
        ball.dx *= -1