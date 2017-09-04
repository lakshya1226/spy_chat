# function for start the chat with both the user default as well as new user..
def start_chat(spy_name,spy_age,spy_rating):
    print "Enter your choice"
    show_menu = True
    while show_menu:
            menu_choices = "what do you want to do ? \n " \
                            "1.Add a status updation \n " \
                            "2.Add a friend \n " \
                            "3.Send a secret message \n " \
                            "4.Read a sceret message \n " \
                            "5.Read chat from user \n " \
                            "6.Close aplication \n "

            result = int(input(menu_choices))
