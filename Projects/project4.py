import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()

# TODO - create at least two variables and set their starting value. ex: cookies = 0
set_background("jungle.gif")
food = 10
health = 50
age = 1

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

def feed_pet ():
    global food
    food += 1
    x = random.randint (-200,200)
    y = 200
    c1 = create_sprite("feed_pet",x,y)
    cookieList.append(c1)
window.onkeypress(feed_pet,"space")


    



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"food: {food}\nhealth:{health}\nage:{age}:",font=("Arial",30,"normal"))
    x1+=1
    if x1 < 350:
        x =-350
    s1.goto(x1,y1)
    # TODO - put any automatic actions here
    for c1 in cookieList:
        c1.setheading(270)
        c1.forward(10)
        if get_distance(c1, s1) <100:
            food +=1
            c1.hideturtle()
    

    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()