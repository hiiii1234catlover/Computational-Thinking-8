# Section 1 - Your code
from utils import *
set_background("Medieval Castles.gif")

s1 = create_sprite("shield_piece_1.gif", 100, 100)
s2 = create_sprite("shield_piece_2.gif", -100, 100)
s3 = create_sprite("shield_piece_4.gif", -100, -150)
s4 = create_sprite("shield_piece_3.gif", 100, -150)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Your Name",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()