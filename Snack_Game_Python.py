# import random 
import time 
# import turtle its a pygame package
import turtle  
#import random 
import random
delay= 0.1

#score
score=0
high_score=0
# screen displey


we=turtle.Screen()
# screen setting 
we.title("Snack_Game by Sasikumar.R")
we.bgcolor("orange")
we.setup(height=600,width=600)
we.tracer(0)  # animation on and off


#snack head add
head=turtle.Turtle()
head.speed(0)
head.color('black')
head.shape('square')
head.penup()
head.goto(0,0)
head.direction ='stop'
 
#snack food
food=turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(0,100)
 
segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0   High Score:0",align='center',font=("courier", 24 ,"normal"))


#function
def go_up():
    if head.direction !="down":
         head.direction ="up"
    
def go_down():
    if head.direction !="up":
         head.direction ="down"
 
def go_left():
    if head.direction !="right":
         head.direction ="left"
    
def go_right():
    if head.direction !="left":
         head.direction ="right"
            
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
         
         
         
#keyboard moveing
we.listen()
we.onkeypress(go_up,"w")        
we.onkeypress(go_down,"s")        
we.onkeypress(go_left,"a")        
we.onkeypress(go_right,"d")      
  
#main game loop
while True:
    we.update()
    
    #check for border stop
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ='stop'
        
        #hide the segments
        for segment in segments:
          segment.goto(1000,1000)
          
        #cler segments
        segments.clear()
        
        #reset the score
        score=0
        
        #reset the delay
        delay=0.1
        pen.clear()
        pen.write("Score:{}  high Score:{}".format(score,high_score),align="center",font=("courier", 24 ,"normal"))
        
    #check for a collism with  the food 
    if head.distance(food) < 20:
    # move the food at randam place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
     
     #add segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        
        #short and delay
        delay -=0.001
        
     #increase the score    
        score +=1
        if score >high_score:
           high_score =score
        
        pen.clear()
        pen.write("Score:{}  high Score:{}".format(score,high_score),align="center",font=("courier", 24 ,"normal"))
    
    #move the segment first reverse oreder
    for index in range(len(segments) -1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    
    #move segment 0 to where the head is 
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #check for  head collish when body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            
             #hide the segment
            for segment in segments:
             segment.goto(1000,1000)
            
             #cler segments
            segments.clear()
             #reset the score
            score=0
            #reset the delay
            delay=0.1
            pen.clear()
            pen.write("Score:{}  high Score:{}".format(score,high_score),align="center",font=("courier", 24 ,"normal"))
            
    time.sleep(delay)
    
we.mainloop()  # screen (without close) show - time- module 