import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
# the goal of this game is to feed your snake and get it to age 4 and health 100 so it will turn in to a dragon 
# TODO - create at least two variables and set their starting value. ex: cookies = 0
set_background("jungle.gif")
food = 9
health = 50
age = 1
place = "right"

x1 =-350
y1 =-200

s1 = create_sprite("snake.gif",x1,y1)
cookieList = []
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -350,150)
message_sprite.hideturtle()
message_sprite.write("keep your snake alive by giving it food water and keeping it healthy")

# Section 2 - controls
# TODO - define an action. ex: def my_control()
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
# TODO - make a second control



def speak ():
    s1.write("hiss")
window.onkeypress(speak, "a")
s1.color("white")



def feed_pet ():
    global food
    # food += 1
    x = random.randint (-350,350)
    y = 200
    c1 = create_sprite("feed_pet",x,y)
    cookieList.append(c1)
window.onkeypress(feed_pet,"space")


    



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"food: {food}\nhealth:{health}\nage:{age}:",font=("Arial",30,"normal"))

    if i % 100 == 0:
        if food > 10:
            health += 1
            age += 0.1
        elif food < 10:
            health -= 1
    if i % 100 == 0:
        food -= 1

    if i % 100 == 0:
        s1.clear()


    if place == "right":
        x1+=1
    elif place == "left":
        x1-=1
    if x1 > 350:
        place = "left"
    elif x1 < -350:
        place = "right"

    s1.goto(x1,y1)
    
    
    
    # TODO - put any automatic actions here
    for c1 in cookieList:
        c1.setheading(270)
        c1.forward(10)
        if get_distance(c1, s1) <100:
            food +=2
            cookieList.remove(c1)
            c1.goto(-15000,-15000)
            c1.hideturtle()
    
    if health >= 100 and age >= 4:
        print ("you win !!!!")
        set_image(s1,"dragon")
        window.update()
        time.sleep(3)
        break
   
    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")
    time.sleep(0.01)
    window.update()