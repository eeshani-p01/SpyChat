from spy_details import spy_name,salu,spy_age,spy_rating
import sys #system module

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']
friend_name=[]
friend_age=[]
friend_rating=[]
friend_is_online=[]

print "Welcome to SpyChat!!"
question = "Do you want to continue as " + salu + " " + spy_name + "(Y/N)?"
print question
user_input = raw_input("Enter your choice\n")

def start_chat(spy_name,spy_age,spy_rating):
    current_status = None
    show_menu = True

    while show_menu:
        print "What do you want to do? \n1. Add a status update \n2. Add a friend\n 3. Close Application\n"
        menu_choice = input("Enter your choice\n")

        if menu_choice == 1:
            print 'You chose to update the status'
            current_status=add_status(current_status)
        elif menu_choice == 2:
            add_friend()
        elif  menu_choice == 3:
            show_menu = False
        else
            sys.exit()


def add_status(current_status):
    if current_status !=None:
      print "Your current status message is " + current_status + "\n"
    else:
      print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper()=="Y":
        index=1
        for status in STATUS_MESSAGES:
            print "{}.{}".format(index,status)
            index=index+1
        message_select=input("Select from the above status:\n")
        if len(STATUS_MESSAGES)>=message_select:
            updated_status_message = STATUS_MESSAGES[message_select-1]
            print "Your status is updated."
        else:
            print "You didn't enter any status!!!"
    return updated_status_message

def add_friend():
    new_name = input("Please enter your friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("What's the age?")
    new_rating = input("What is their Spy rating?")
    if len(new_name)>0 and new_age>12 and new_rating>=spy_rating:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_is_online.append(True)
    else:
        print "Sorry ! but we can't add this spy to your friend list. "
    return len(friend_name)



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
