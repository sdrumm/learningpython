# Tell the story to keep going
stop = False

# As long as they don't want to quit
while stop is False:
    # Gather the information from the user
    age = raw_input("Enter an age. Please put young, middle-aged or old: ")

    # Force the user to answer with young, middle-aged or old
    while age.lower() not in ['young', 'middle-aged', 'old']:
        age = raw_input("Enter an age: Please put young, middle-aged or old: ")

    career = raw_input("Enter a career: ")
    nationality = raw_input("Enter a nationality: ")
    personality = raw_input("Enter a personality: ")
    knowledge = raw_input("Enter a knowledge: ")
    motive = raw_input("Enter a motive: ")
    plan = raw_input("Enter a plan: ")
    charm = raw_input("Enter the charm: ")
    weapon = raw_input("Enter a weapon: ")
    friend = raw_input("Enter a friend: ")
    win = raw_input("Will he win in the end? Please enter yes or no: ")

    # Force the user to answer with yes or no
    while win.lower() not in ['yes', 'no']:
        win = raw_input("Will he win in the end? Please enter yes or no: ")

    # Use the user information to make a story
    print 'Remi was a ' + age + ' independent ' + career + ' from the ' \
    + nationality + '. He was kicked out of the Russian intelligence agency for being too ' \
    + personality + '. He learned ' + knowledge + ' about the world, and ' \
    + motive + ', decided to ' + plan + '. He charmed all the leaders with his ' \
    + charm + ', and ripped their throats out with his ' + weapon + '.' \

    # Determine the end of the story
    if win.lower() == "yes":
        print "He now rules the world with his best friend and paramour " + friend
    else:
        print "But Putin threw him into jail with Pussy Riot."

    # Prompt user to decide whether to keep playing
    stop_input = raw_input("Wanna play again? Please enter yes or no: ")

    # Forces the user to respond with yes or no
    while stop_input.lower() not in ['yes', 'no']:
        stop_input = raw_input("Wanna play again? Please enter yes or no: ")

    # Tells story whether to stop or continue
    if stop_input.lower() == "yes":
        stop = False
    elif stop_input.lower() == "no":
        stop = True
