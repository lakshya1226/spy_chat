# function for start the chat with both the user default as well as new user..
from add_status import add_status
from add_friend import add_friend
def start_chat(spy_name,spy_age,spy_rating):
    from globals import current_status_message
    # validating user detail
    if not (spy_age > 12 and spy_age < 50) :
            error_message = "invalid age..Provide correct details"
            print error_message
    else:
            welcome_message = "Auntentication Complete..Welcome Spy"
            print welcome_message

            show_menu=True
            while show_menu:
                menu_choices = "what do you want to do ? \n " \
                            "1.Add a status updation \n " \
                            "2.Add a friend \n " \
                            "3.Send a secret message \n " \
                            "4.Read a sceret message \n " \
                            "5.Read chat from user \n " \
                            "6.Close aplication \n "
                result = int(input(menu_choices))
                # validating the user inputs
                if(result == 1):
                    current_status_message = add_status(current_status_message)
                elif(result == 2):
                    add_friend()




