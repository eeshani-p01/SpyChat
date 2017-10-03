from spy_details import Spy
from steganography.steganography import Steganography
from datetime import datetime
import sys #system module

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']
Spy = Spy('Bond','Mr.',23,5)
friends = []

print "Welcome to SpyChat!!"
question = "Do you want to continue as " + Spy.salu + " " + Spy.name + "(Y/N)?"
print question
user_input = raw_input("Enter your choice\n")


def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True

    while show_menu:
        print "What do you want to do? \n1. Add a status update \n2. Add a friend\n3. Select a friend \n4. Send message \n5. Read message \n6. Close Application\n"
        menu_choice = input("Enter your choice\n")

        if menu_choice == 1:
            print 'You chose to update the status'
            Spy.current_status = add_status(Spy.current_status)
        elif menu_choice == 2:
            friend_no=add_friend()
            print "You have {} friends.".format(friend_no)
        elif menu_choice == 3:
            friend_selected = select_friend()
            print "you choose {}".format(friends[friend_selected]['name'])
        elif menu_choice == 4:
            send_message()
        elif menu_choice == 5:
            read_message()
        elif  menu_choice == 6:
            show_menu = False
        else:
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

    new_friend = {
        'name' : '',
        'salu' : '',
        'age' : 0,
        'rating' : 0.0
    }

    new_friend['name'] = raw_input("Please enter your friend's name:")
    new_friend['salu'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salu'] + " " + new_friend['name']
    new_friend['age'] = input("What's the age?")
    new_friend['rating'] = input("What is their Spy rating?")

    if len(new_friend['name'])>0 and new_friend['age']>12:
        friends.append(new_friend)
        print "Friend Added !!"
    else:
        print "Sorry ! but we can't add this spy to your friend list. "

    return len(friends)


def select_friend():
    item = 0
    for friend in friends :
        print "{}. {}".format(item+1,friend['name'])
        item=item+1

    select = input("With whom you want to chat? ")

    return select-1


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of your image?\n ")
    output_path = "hidden.jpg"
    msg = raw_input("What is the secret message to your friend? \n")
    Steganography.encode(original_image,output_path,msg)

    new_chat = {
        'message' : msg,
        'time' : datetime.datetime.now(),
        'sent_by_me' : True
    }
    friend[friend_choice]['chat'].append(new_chat)

    print "Your secret message has been sent to your friend."


def read_message():
    sender = select_friend()

    input_path = raw_input("What is the name of your secret image?\n")
    secret_text = Steganography.decode(input_path)
    print secret_text



if user_input.upper() == 'Y':
    #normal operation
    print "Welcome %s  age: %d and rating of: %1f Proud to have you onboard" %(Spy.name, Spy.age, Spy.rating)

    start_chat(Spy.name, Spy.age, Spy.rating)

else:
    Spy.name = raw_input("Hello dear ! Tell me your spy name :  \n")
    if len(Spy.name)>0 :
        Spy.salu = raw_input("What should I call you, Mr. or Mrs.? \n")
        Spy.name = Spy.salu+" "+ Spy.name
        print "Hello, " + Spy.name

        Spy.age = 0
        Spy.rating = 0.0
        Spy.is_online = False

        Spy.age=input("What is your age? ")
        if Spy.age > 12 and Spy.age < 50 :
            Spy.rating = input("What is your spy rating ? ")
        else :
            print "Sorry, Your age doesn't fit to be a spy "

        if Spy.rating > 4.5:
            print 'Great ace!'
        elif Spy.rating > 3.5 and Spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif Spy.rating >= 2.5 and Spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        Spy.is_online = True

        print "Authentication complete.  Welcome %s  age: %d and rating of: %1f Proud to have you onboard" %(Spy.name,Spy.age,Spy.rating)

        start_chat(Spy.name, Spy.age, Spy.rating)

    else:
        print "This spy doesn't exist !!"
