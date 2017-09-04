 # importing statements
from spy_detail import spy_name, spy_salutation, spy_age, spy_rating, spy_is_online
from spy_chat import start_chat
print "Hello!! Let\'s get started..."
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " " "(Y/N)? "
existing_user = raw_input(question)
# validating user input
if existing_user.upper() == "Y":
    # user wants to continue as default user.
    print "Auntentication complete .Welcome again.."
    print "name: "+ spy_name
    print "age: " + str(spy_age)
    print "rating of: " + str(spy_rating)
    print "Happy to have you again...."

    start_chat(spy_name,spy_age,spy_rating,)
elif existing_user.upper() == "N":
#new input
    spy_name = raw_input("Welcome to spy chat, you must enter your name here: ")
    #check the details of new user
    if len(spy_name)>0:
        spy_salutation = raw_input("should I call you Mr. or Mrs. :")
        spy_age = raw_input("What is your age")
        spy_age = int(spy_age)


        spy_spy_rating = raw_input("What is your spy rating")
        spy_spy_rating = float(spy_rating)

        spy_is_online = True
        print "Your authentication is verified %s %s\n Your seem to be a very young spy with an age of %s \n " % (spy_salutation,spy_name,spy_age)
    start_chat(spy_name,spy_age,spy_rating,)
else:print "wrong choice..!!"



