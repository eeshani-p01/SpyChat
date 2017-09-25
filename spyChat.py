from spy_details import spy_name,salu,spy_age,spy_rating
import sys #system module

print "Welcome to SpyChat!!"
question = "Want to Continue as " + salu + " " + spy_name + "(Y/N)?"
print question
user_input = raw_input("Enter your choice\n")

def start_chat(spy_name,spy_age,spy_rating):
    current_status = None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Close Application\n"
        choice = raw_input(menu_choices)

        if choice == 1:
            # pass
            add_status(current_status_message)
        elif choice == 2:
            show_menu = False
        else:
            sys.exit()          #defined in system module

def add_status(current_status_message):

    if current_status_message != None:
      print "Your current status message is " + current_status_message + "\n"
    else:
      print 'You don\'t have any status message currently \n'


if user_input == 'Y':
    #normal operation
    print "Welcome %s  age: %d and rating of: %1f Proud to have you onboard" %(spy_name, spy_age, spy_rating)

    start_chat(spy_name, spy_age, spy_rating)

else:
    spy_name = raw_input("Hello dear ! Tell me your spy name :  \n")
    if len(spy_name)>0 :
        salu = raw_input("What should I call you, Mr. or Mrs.? \n")
        spy_name = salu+" "+ spy_name
        print "Hello, " + spy_name

        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        spy_age=input("What is your age? ")
        if spy_age > 12 and spy_age < 50 :
            spy_rating = input("What is your spy rating ? ")
        else :
            print "Sorry, Your age doesn't fit to be a spy "

        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        spy_is_online = True

        print "Authentication complete.  Welcome %s  age: %d and rating of: %1f Proud to have you onboard" %(spy_name,spy_age,spy_rating)

        start_chat(spy_name, spy_age, spy_rating)

    else:
        print "This spy doesn't exist !!"
