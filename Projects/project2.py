print ("hello and welcome to this quiz. today you will find out how well you know your best friend")
points = 0
questions = 0
bonus_point = 0

answer1 = input("How long have you know your best friends A 1 year,B 10 years, or C less than a year")
if answer1 == "A" or answer1 == "a":
    points +=200
elif answer1 == "B" or answer1 == "b":
    points +=300
elif answer1 == "C" or answer1 == "c":
    points +=100

answer2 = input("how often do you talk A every day,B once a month, or C once a week")
if answer2 == "A" or answer2 == "a":
    points +=300
elif answer2 == "B" or answer2 == "b":
    points +=100
elif answer2 == "C" or answer2 == "c":
    points +=200

answer3 = input("if I asked you 10 questions about them how many do you think you would get right A 1 questions B 5 questions C all questions ")
if answer3 == "A" or answer3 == "a":
    points +=100
elif answer3 == "B" or answer3 == "b":
    points +=200
elif answer3 == "C" or answer3 == "c":
    points +=300

answer4 = input("How much do you trust them A kind of B I would tell them anything C not a lot")
if answer4 == "A" or answer2 == "a":
    points +=200
elif answer4 == "B" or answer4 == "b":
    points +=300
elif answer4 == "C" or answer4 == "c":
    points +=100

    answer5 = input("if they were being picked on would you stand up for them A yes B no C maybe")
if answer5 == "A" or answer5 == "a":
    points +=300
elif answer5 == "B" or answer5 == "b":
    points +=100
elif answer5 == "C" or answer5 == "c":
    points +=200

    answer6 = input("have you ever seen them cry and vice versa A idk B no C yes")
if answer6 == "A" or answer6 == "a":
    points +=200
elif answer6 == "B" or answer6 == "b":
    points +=100
elif answer6 == "C" or answer6 == "c":
    points +=300

    answer7 = input("do you feel as hough you got each others backs A No B yes C maybe")
if answer7 == "A" or answer7 == "a":
    points +=100
elif answer7 == "B" or answer7 == "b":
    points +=300
elif answer7 == "C" or answer7 == "c":
    points +=200

if points > 1900: 
    print("If you want to know what true, unwavering support and genuine fun look like, just spend five minutes with these two, you might say to a group. Each of you brings a totally unique energy, but together, it's something truly special. One of you is the steady rock, the voice of reason that I always turn to, while the other is the spontaneous spark, the one who reminds me not to take everything so seriously. Its that perfect balance between the two of you—the reliability mixed with the adventure—that makes your friendship so incredible to witness and even better to be a part of. I genuinely couldn't ask for a better duo to have in my corner.")
elif points <= 1900 and points > 900:
    print("It's genuinely great to see you two chatting. The dynamic you have is really special, and you clearly bring a lot of joy and good energy to each others lives. It just feels like it's been a while since you both carved out some dedicated time just to hang out and catch up. You should seriously prioritize getting a date on the calendar soon—you deserve that friend time!")
elif points <= 900 and points > 0:
    print(" you two really need to get to know each other")
else:
    print("you did something wrong")

