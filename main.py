print "hello!"

print "Let\'s get started..."

spy_name = raw_input("welcome to spy chat, you must tell me your spy name first :")

if len(spy_name) > 0 :

    #LOGIC WILL BE HERE IF CONDITION IS TRUE.

    spy_salutation =raw_input("what should we call you ? mr. or miss ?: ")

    spy_name =spy_salutation +' '+spy_name

    print "alright " + spy_name + ". I want know more about you before we proceed..."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = raw_input("what is your age? ")

    print type(spy_age)

    spy_age = int(spy_age)

    if spy_age > 12 and spy_age < 50:

        spy_rating = raw_input("what is your spy rating?")
        spy_rating = float(spy_rating)


        if spy_rating > 4.5:
            print "Great ace!"
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print "You are one of the good ones..."
        elif spy_rating >=2.5 and spy_rating  <= 3.5:
            print "You can always do better"
        else:
            print "We can always use someday to help in the office.."

        spy_online = True

        print "Auntentication complete. Welcome " + spy_name + "age: " + str(spy_age) + " and rating of: " + str(spy_rating) + "glad to have you back with us.."
    else:

        print "Sorry : you are not of correct age to be a spy.."

else :

    print ("spy has a invalid user name... ? try again please")


