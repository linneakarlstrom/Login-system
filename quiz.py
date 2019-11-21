def start():
    score = 0
    print("Hello there! Welcome to my quiz!\nAre you ready? If not, then I hope so.\nGood luck!")
    print("----------------------------------------")
    
    questions = [ 
    ("Imagine you're in a dark room that is empty with nothing in it. There are no windows or doors. What is the easiest way to escape? \
    \nA. Stop imagining that you are in a dark room.\nB. Die of course.\nC. Wait.\nD. Dig a hole in the ground with your bare hands.\nAnswer:", "A", "a", "Stop imagining you are in a dark room", "stop imagining you are in a dark room", "A. Stop imagining you are in a dark room"),
    ("As the Titanic headed out to sea, what did the Captain say to the first officer?\nA.'Take her to sea Mr. Murdock, lets stretch her legs'. \
    \nB.'Get away from the wheel you jerk, I'm driving'.\nC.'Pleeeeeeeeeeease don't make me go. Somtin bad goin to happen'.\nD.'My boat, tee hee, my boat, tee hee, my boat, tee hee, can I ring the bell, tee hee.' \
    \nAnswer:", "A", "a", "'Take her to sea Mr. Murdock, lets stretch her legs'", "take her to sea Mr. Murdock, lets stretch her legs", "A. 'Take her to sea Mr. Murdock, lets stretch her legs'"),
    ("If you look you cannot see me. If you can see me you cannot see anything else.\nI can make anything you want to happen, but later on everything will go back to normal. What am I?\
    \nA. Air.\nB. Nothing,\nC. Imagination.\nD. Other.\nAnswer:", "C", "c", "Imagination", "imagination", "C. Imagination" ),
    ("The titanic was powered by\nA. Thousands of hamsters' running inside little wheels. \nB. The third class passengers rowing \nC. Sixteen giant steam boilers \
    \nD. The crew members 'hocking lugies off the sterm all at once\nAnswer:", "C", "c", "Sixteen giant steam boilers", "sixteen giant steam boilers","C. Sixteen giant steam boilers"),
    ("If your car begins to hydroplane (Hydroplaning means that water separates the tires from the ground and causes it to lose traction. You feel out of control.) you should:\
    \nA. Reduce your speed and let the car decelerate.\nB. Pump the breaks repeatedly.\nC. Immediatly slam the brakes.\
    \nD. Do nothing and allow your car to turn into the plane it has always dreamed of.\nAnswer:", "D", "d", "Do nothing and allow your car to turn into the plane it has always dreamed of.", "do nothing and allow your car to turn into the plane it has always dreamed of.", \
    "D. Do nothing and allow your car to turn into the plane it has always dreamed of."),
    ("When was Albert Einstein born? \nA.In Switzerland \nB.In Germany \nC.In the United States \nD.In Israel.\nE.None of the above. \nAnswer:", "E", "e", "None of the above", "none of the above", "E.None of the above"),
    ("There are 30 cows in a field, and 28 chickens. How many didn't?", "10", "ten", "Ten", "TEN", "10 didn't"),
    ("Mental break time. This is the last question of the quiz. You deserve an easy question. What is 1 + 1?\nA. Not this one. \nB. Still not this one.\nC. Two\nD. You've gone too far, go back to C.\nAnswer:", "C", "c", "Two", "two", "C. 2", "2")
]

    for q in questions:
        answer = input(q[0])
        if answer == q[0+1] or answer == q[0+1+1] or answer == q[0+1+1+1]  or answer == q[0+1+1+1+1] or answer == q[0+1+1+1+1+1]:
            print("\nYay!Correct answer!\n")
            score += 1
        else:
            print("Awh, that answer is incorrect.\n")

    print("You got a total score of", str(score), "out of", len(questions))
    print("That means you got", str(score / len(questions) * 100),"%", " of the answers correct!")
    quit()                
