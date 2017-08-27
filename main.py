print 'Let\'s get started...'
spy_name = raw_input('what is your name ? : ')

if len(spy_name) > 0 :
    #LOGIC WILL BE HERE IF CONDITION IS TRUE.
    spy_salutation =raw_input('what should we call you ? :')
    spy_name =spy_salutation +' '+spy_name
    print 'welcome ' + spy_name + ' glad to have you back with us..'
else :
    print ('spy has a invalid user name... ? try again please')


