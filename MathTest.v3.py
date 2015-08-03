# This is a Math Test
import random
from random import randint

# ---- Start Functions ----#

def question_type_1():
    q1v1 = randint(111, 9999)
    q1v2 = randint(111, 9999)
    print "{}*{} = ".format(q1v1, q1v2)
    tr.write("{}*{} = \n".format(q1v1, q1v2))
    tr.write("Answer: {}\n".format(q1v1*q1v2))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if (int(anw)) == (int(q1v1*q1v2)):
        print " "
        tr.write("\n\n")
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")

def question_type_2():
    q2v1 = randint(1000, 99999)
    q2v2 = randint(1000, 99999)
    print "{}+{} = ".format(q2v1, q2v2)
    tr.write("{}+{} = \n".format(q2v1, q2v2))
    tr.write("Answer: {}\n".format(q2v1+q2v2))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if(int(anw)) == (int(q2v1+q2v2)):
        print " "
        tr.write("\n\n")
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")

def question_type_3():
    q3v1 = randint(1000, 99999)
    q3v2 = randint(1000, 99999)
    q3list = [q3v1, q3v2]
    print "{}-{} = ".format(max(q3list), min(q3list))
    tr.write("{}-{} = \n".format(max(q3list), min(q3list)))
    tr.write("Answer: {}\n".format(max(q3list)-min(q3list)))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if(int(anw)) == (int(max(q3list)-min(q3list))):
        print " "
        tr.write("\n\n")
        return True
    else:
        tr.write("Incorrect\n\n")
        print " "

def question_type_4():
    q4v1 = randint(3, 99)
    q4v2 = randint(3, 99)
    q4v3 = q4v1*q4v2
    print "{}/{}=".format(q4v3, q4v1)
    tr.write("{}/{} = \n".format(q4v3, q4v1))
    tr.write("Answer: {}\n".format(q4v2))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if(int(anw)) == (int(q4v2)):
        print " "
        tr.write("\n\n")
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")
def question_type_5():
    q5v1 = randint(2, 9)
    q5v2 = randint(3, 5)
    print "{}^{}=".format(q5v1, q5v2)
    tr.write("{}^{} = \n".format(q5v1, q5v2))
    tr.write("Answer: {}\n".format(q5v1**q5v2))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format((anw)))
    if(int(anw)) == (int(q5v1**q5v2)):
        score += 10
        tr.write("\n\n")
        print " "
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")

def question_type_6():
    q6v1 = randint(11, 999)
    q6v2 = (randint(11, 999))
    print "{}+({}) = ".format(q6v1, (q6v2*-1))
    tr.write("{}+(-{}) =".format(q6v1, q6v2))
    tr.write("Answer: {}\n".format((q6v1-q6v2)))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if(int(anw)) == (int(q6v1-q6v2)):
        tr.write("\n\n")
        print " "
        return True
    else:
        tr.write("Incorrect\n\n")
        print " "

def question_type_7():
    q7v1 = randint(11, 9999)
    q7v2 = (randint(1111, 9999))*.01
    print "{}*{:.2f} = ".format(q7v1, q7v2)
    print "If whole number include \'.0\'."
    tr.write("{}*{:.2f} = \n".format(q7v1, q7v2))
    tr.write("Answer: {:.2f}\n".format((q7v1*q7v2)))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format((anw)))
    if anw == str(float(q7v1*q7v2)):
        tr.write("\n\n")
        print " "
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")

def question_type_8():
        q8v1 = (randint(1111, 9999))*.1
        q8v2 = (randint(1111, 9999))*.001
        print "{}+{} = ".format(q8v1, q8v2)
        tr.write("{}+{} = \n".format(q8v1, q8v2))
        tr.write("Answer: {}\n".format(q8v1+q8v2))
        while True:
            try:
                anw = int(raw_input("Answer: "))
                break
            except ValueError:
                print "Please enter the numerical value."
        tr.write("Your Answer: {}\n".format(float(anw)))
        if anw == str(float(q8v1+q8v2)):
            tr.write("\n\n")
            return True
            print " "
        else:
            tr.write("Incorrect\n\n")
            print " "

def question_type_9():
        q9v1 = randint(11, 25)
        q9v2 = q9v1**2
        print "What is the square root of {}?\n".format(q9v2)
        tr.write("What is the square root of {}?\n".format(q9v2))
        tr.write("Answer: {} \n".format(q9v1))
        while True:
            try:
                anw = int(raw_input("Answer: "))
                break
            except ValueError:
                print "Please enter the numerical value."
        tr.write("Your Answer: {}\n".format(anw))
        if int(anw) == int(q9v1):
            tr.write("\n\n")
            print " "
            return True
        else:
            tr.write("Incorrect\n\n")
            print " "

def is_prime(x):
    if x == 2:
        return True
    else:
        for i in range(2, int(x**.5)+1):
            if x%i == 0:
                return False
    return True

def question_type_10():
    q10v1 = randint(2, 199)
    print "Is {} a prime number?(Yes or No)".format(q10v1)
    while True:
        try:
            a1 = raw_input("Answer: ")
            break
        except ValueError:
            print "Please enter the numerical value."     
    tr.write("Is {} a prime number?\n".format(q10v1))
    tr.write("Your Answer: {}\n".format(a1))
    anw = a1.lower()
    if anw == "yes" and is_prime(q10v1) == True:
        tr.write("\n\n")
        print " "
        return True
    elif anw == "no" and is_prime(q10v1) == False:
        tr.write("\n\n")
        print " "
        return True
    else:
        tr.write("Incorrect\n\n")
        print " "

def word_problem_1():
    name = ["David", "Pam", "Paul", "Dan", "Susan", "Mathew"]
    n = randint(0, 4)
    wp0v1 = randint(2, 5)
    wp0v2 = randint(5, 10)
    print """
    {0} is riding a train that is going {1} miles a minute.
    The train has been on the rails for {2} hours.  How many miles
    has {0} travelled?
    """.format(name[n], wp0v1, wp0v2)
    tr.write("""
    {0} is riding a train that is going {1} miles a minute.
    The train has been on the rails for {2} hours.  How many miles
    has {0} travelled?\n
    """.format(name[n], wp0v1, wp0v2))
    tr.write("Answer: {}\n".format(((wp0v1*60)*wp0v2)))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
        
    tr.write("Your Answer: {}\n".format(anw))
    if anw == int((wp0v1*60)*wp0v2):
        return True
        print " "
    else:
        tr.write("Incorrect\n\n")
        print " "

def word_problem_2():
    name = ["Paul", "Russell", "Melissa", "Margery", "Craig", "Simon"]
    animal1 = ["gorillas", "lions", "ocelots"]
    animal2 = ["hyena", "baboons", "tigers"]
    animal3 = ["giraffes", "ant eaters", "cheetahs"]
    w1v1 = randint(2, 10)
    w1v2 = randint(2, 10)
    w1v3 = randint(2, 10)
    w1v4 = randint(2, 10)
    w1v5 = randint(2, 10)
    w1v6 = randint(2, 10)
    v1 = randint(0, 5)
    v2 = randint(0, 2)
    v3 = randint(0, 2)
    v4 = randint(0, 2)

    print """
    Zoo Keeper {0} has {1} {2} that eat {3} lbs of food each,
    {4} {5} that eat {6} lbs of food each and {7} {8} that eats
    {9} lbs of food each per day.
    How many pounds of food does Zoo Keeper {0} need?
    """.format(name[v1], w1v1, animal1[v2], w1v2, w1v3, animal2[v3],
        w1v4, w1v5, animal3[v4], w1v6)

    tr.write("""
    Zoo Keeper {0} has {1} {2} that eat {3} lbs of food each,
    {4} {5} that eat {6} lbs of food each and {7} {8} that eats
    {9} lbs of food each per day.
    How many pounds of food does Zoo Keeper {0} need?
    """.format(name[v1], w1v1, animal1[v2], w1v2, w1v3, animal2[v3],
        w1v4, w1v5, animal3[v4], w1v6))

    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."

    tr.write("Your Answer: {}\n".format(anw))
    if anw == int((w1v1*w1v2)+(w1v3*w1v4)+(w1v5*w1v6)):
        return True
        print " "
    else:
        tr.write("Incorrect\n\n")
        print " "

def word_problem_3():
    name = ["Wendel", "Wendy", "Damian", "Corrina", "Geoffrey", "Isabel", "Leroy", "Caroline"]
    n = randint(0, 7)
    if n%2 == 0:
        g = "he"
    else:
        g = "she"
    m1 = randint(20, 100)
    r1 = randint(3, 6)*5
    m2 = randint(20, 100)
    r2 = randint(5, 15)
    m3 = randint(20, 100)
    r3 = randint(2, 4)

    print """
    {0} is going on a trip.  {0} drives {1} miles and then stops
    {2} minutes for some food.  {0} then drives {3} miles and stops
    for {4} minutes to stretch his legs.  Then after {5} miles {6}
    stops at a friend's house and stays there for {7} hours for dinner.
    How many minutes did {0} stop for breaks and dinner?
    """.format(name[n], m1, r1, m2, r2, m3, g, r3)
    tr.write("""
    {0} is going on a trip.  {0} drives {1} miles and then stops
    {2} minutes for some food.  {0} then drives {3} miles and stops
    for {4} minutes to stretch his legs.  Then after {5} miles {6}
    stops at a friend's house and stays there for {7} hours for dinner.
    How many minutes did {0} stop for breaks and dinner?
    """.format(name[n], m1, r1, m2, r2, m3, g, r3))

    tr.write("Answer: {}\n".format((r1+r2+(r3*60))))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if anw == int(r1+r2+(r3*60)):
        print " "
        return True
    else:
        tr.write("Incorrect\n\n")
        print " "

def word_problem_4():
    name = ["Harry", "Gail", "Mark", "Rachel", "Lance", "Willow"]
    n = randint(0, 5)
    books = randint(10, 30)
    buy_price = randint(10, 30)
    sell_price = randint(35, 50)
    print """
    {0} bought {1} books. She paid ${2} for each book. She later sold
    all {1} books for ${3} each. What is the difference between the total
    amount of money {0} sold the books for and the total amount of
    money she paid for the books?
    """.format(name[n], books, buy_price, sell_price)
    tr.write("""
    {0} bought {1} books. She paid ${2} for each book. She later sold
    all {1} books for ${3} each. What is the difference between the total
    amount of money {0} sold the books for and the total amount of
    money she paid for the books?
    """.format(name[n], books, buy_price, sell_price))

    tr.write("Answer: {}\n".format(int((books*sell_price)-(books*buy_price))))
    while True:
        try:
            anw = int(raw_input("Answer: "))
            break
        except ValueError:
            print "Please enter the numerical value."
    tr.write("Your Answer: {}\n".format(anw))
    if anw == int((books*sell_price)-(books*buy_price)):
        print " "
        tr.write("\n\n")
        return True
    else:
        print " "
        tr.write("Incorrect\n\n")

# --- End Functions ---- #


print "Oh no, mean Mr. Headley has sprung a surprise math test on us!"
print "Better get ready!  If we fail this we will never get into Harvard!"
print " "
student = raw_input("What is your first name?")

#Create Test Restults file.
rfile = "test_results_%s.txt" %(student)
print " "
tr = open(rfile, "w")
tr.write("POP QUIZ! \n")
tr.write("These are the test results for {} \n".format(student))
tr.write("\n")
score = 0
count = 0
for question in range(8):
    q = randint(1, 10) 

    if q == 1:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_1() == True:
            score += 10
        else:
           pass

    elif q == 2:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_2() == True:
            score += 10
        else:
            pass

    elif q == 3:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_3() == True:
            score += 10
        else:
            pass

    elif q == 4:
        count += 1
        print "Question",count
        tr.write("Question {} \n".format(count))
        if question_type_4() == True:
            score += 10
        else:
            pass

    elif q == 5:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_5() == True:
            score += 10
        else:
            pass

        

    #Question type 6
    elif q == 6:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_6 ()== True:
            score += 10
        else:
            pass

    elif q == 7:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_7() == True:
            score += 10
        else:
            pass

    elif q == 8:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_8() == True:
            score += 10
        else:
            pass

    elif q == 9:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_9() == True:
            score += 10
        else:
            pass


    #Question Type 10
    elif q == 10:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {} \n".format(count))
        if question_type_10() == True:
            score += 10
        else:
            pass

#Word Problems
wp = range(4)

random.shuffle(wp)
p = 0
for wordproblem in range(2):

    if wp[p] == 0:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {}\n".format(count))
        if word_problem_1() == True:
            score += 10
        else:
            pass


    if wp[p] == 1:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {}\n".format(count))
        if word_problem_2() == True:
            score += 10
        else:
            pass

    if wp[p] == 2:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {}\n".format(count))
        if word_problem_3() == True:
            score += 10
        else:
            pass

    if wp[p] == 3:
        count += 1
        print "\nQuestion {}".format(count)
        tr.write("Question {}\n".format(count))
        if word_problem_4() == True:
            score += 10
        else:
            pass

    p += 1


#Bonus Question!
while True:
    try:
        anw = int(raw_input("BONUS QUESTION!!!  How many zeroes in a googol?\
(Answer in numbers): "))
        tr.write("BONUS QUESTION!!! How many zeroes in a googol?\n")
        tr.write("Your Answer: {}\n".format(anw))
        if anw == 100:
            score += 5
            print " "
            break
        else:
            print " "
            tr.write("Incorrect")
            break
    except ValueError:
        print "Please enter the numerical value."

if score > 100:
    score = 100

tr.write("\n YOUR SCORE IS: {}% \n".format(score))

print "You got {}% of the questions right!".format(score)
if score >= 90:
    print "You got an A!  You are going to Harvard!"
    tr.write("You got an A!  You are going to Harvard!")
elif score >= 80:
    print "You got a B!  Carnegie Melon will still take you!"
    tr.write("You got a B!  Carnegie Melon will still take you!")
elif score >= 70:
    print "You got a C!  Emerson College will take anybody!"
    tr.write("You got a C!  Emerson College will take anybody!")
elif score >= 60:
    print "You got a D!  There is no shame in community college!"
    tr.write("You got a D! There is no shame in community college!")
else:
    print "You Failed!  Stop sleeping in class!"
    tr.write("You Failed!  Stop sleeping in class!")

tr.close()


