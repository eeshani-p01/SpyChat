#importing external modules
from spy_details import Spy, Chat                                       #import the details of spy and chat history
from steganography.steganography import Steganography                   #import it to encode and decode the secret messages
import csv                                                              #import to handle all the details of spy and chat into a csv file
from termcolor import cprint                                             #import to dispaly the details in colour
from colorama import Fore
import sys  # system module

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']       #default status messages
spy = Spy('Bond', 'Mr.', 23, 5)                                                 #default user of spychat
friends = []
special_msg = ["SOS", "SAVE", "HELP"]                                           #special messages variable

print "Welcome to SpyChat!!"
question = "Do you want to continue as " + spy.salu + " " + spy.name + "(Y/N)?"
user_input = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating):                                  #function to to define different feature of spychat
    show_menu = True
    load_friends()                                                              #function call to load all the friends to the friends[] from friends.csv
    load_message()                                                              #function call to load all the chats from chat.csv

    while show_menu:
        print "What do you want to do? \n1. Add a status update \n2. Add a friend\n3. Send a secret message \n4. Read a secret message \n5. Read chats from a user \n6. Close Application\n"
        menu_choice = input("Enter your choice\n")

        if menu_choice == 1:
            print 'You chose to update the status'
            spy.current_status = add_status(spy.current_status)
            print "Your current status is \n\t{}".format(spy.current_status)
        elif menu_choice == 2:
            friend_no = add_friend()
            print "You have {} friends.".format(friend_no)
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chats()
        elif menu_choice == 6:
            show_menu = False
        else:
            sys.exit()                              #helps to terminate the program if there is any other input


#function to add or update the current spy status to new or any older status
def add_status(current_status):
    if current_status is not None:
        print "Your current status message is \" " + current_status + " \"\n"       #diaplay current status if any

    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)                  #add the new status to the statusmessage[]
        else:
            print "I think, you don't want to update the status !!!"

    elif default.upper() == "Y":
        index = 1
        for status in STATUS_MESSAGES:                                      #for loop to print the old status from the list
            print "{}.{}".format(index, status)
            index = index + 1

        message_select = input("Select from the above status:\n")           #take the integer value of list to select the status
        if len(STATUS_MESSAGES) >= message_select:
            updated_status_message = STATUS_MESSAGES[message_select - 1]    #assign the status to updated variable
            print "Your status is updated."
        else:
            print "You didn't enter any status!!!"

    else:
        print "Your input is invalid !!"
        sys.exit()

    return updated_status_message                                           #return the updated status


def add_friend():
    # friend_name = raw_input("Please enter your friend's name:")
    # fri = raw_input("Are they Mr. or Ms.?: ")
    # new_friend['name'] = new_friend['salu'] + " " + new_friend['name']
    # new_friend['age'] = input("What's the age?")
    # new_friend['rating'] = input("What is their spy rating?")

    newspy = Spy(raw_input("Please enter your friend's name:"), raw_input("Are they Mr. or Ms.?: "),    #take all the imput for the friend
                 input("What's the age?"), input("What is their Spy rating?"))
    if (newspy.name.isalpha() == True or newspy.name.isalnum() == True) and newspy.age > 12:            #vlaidation of their details
        friends.append(newspy)                                                                          #add the friend to the friendlist
        with open("friends.csv.txt", "a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([newspy.name, newspy.salu, newspy.age, newspy.rating, True])                #write friend detials into the friend.csv file
        print "Friend Added !!"
    else:
        print "Sorry ! but we can't add this spy to your friend list. "

    return len(friends)                                                                                 #return the new length of the friend list


def select_friend():                                                               #select the index of friend with u want to chat
    item = 0
    for friend in friends:
        print "{}. {}".format(item + 1, friend.name)                            #display the name of al the friends in the list
        item = item + 1

    select = input("With whom you want to chat? ")

    print "you choose {}".format(friends[select - 1].name)
    return select - 1                                                           #return the index of that freind you select


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of your image?\n ")            #name of teh image in which you want to hide the message
    output_path = "hidden.jpg"                                                  #the image in which the msg will be encoded
    msg = raw_input("What is the secret message to your friend? \n")
    msg_new = msg.upper()
    msg_new = msg_new.split(" ")                                                #split the string from the spaces into a list
    for val in msg_new:
        if val in special_msg:                                                   #check is there is any special messgea
            print "You should see the message immediately, there can be emergency!!!!"

    Steganography.encode(original_image, output_path, msg)                      #encodes the msg into a new image

    new_chat = Chat(friends[friend_choice].name, msg, True)
    friends[friend_choice].chats.append(new_chat)                       #appned this chat into the friends chat
    with open("chat.csv.txt", "a") as chats_data:
        chater = csv.writer(chats_data)
        chater.writerow([new_chat.name, new_chat.message, new_chat.sent_by_me, new_chat.time])      #write the chat details into chats.csv file

    print "Your secret message has been sent to your friend."


def read_message():
    sender = select_friend()

    input_path = raw_input("What is the name of your secret image?\n")          #ask for the name of the encoded output image
    secret_text = Steganography.decode(input_path)

    new_chat = Chat(friends[sender], secret_text, False)
    friends[sender].chats.append(new_chat)                                  #append and save the messgae in the chat history of that friend
    print "Your secret message has been saved!"


def load_friends():
    with open("friends.csv.txt", "rb") as friends_data:             #open the csv file as friends_data in read mode
        reader = list(csv.reader(friends_data))                     #convert each line into list

        for row in reader[1:]:
            spy1 = Spy(row[0], row[1], row[2], row[3])              #passing values of spy_friends into SPy class variable
            friends.append(spy1)                                       #append all this details in friends liat


def load_message():
    with open("chat.csv.txt", "rb") as chats_data:              #read from chats.csv file
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            chat_details = Chat(row[0], row[1], row[2])
            spy.chats.append(chat_details)


def read_chats():                                              #read all the chat history of the user
    if len(spy.chats) < 1:
        print "You do not have any history with this friend."
    else:
        for chat in spy.chats:
            cprint(chat.name, 'red')                        #print in colour code
            print(Fore.BLACK + chat.message)                #receiver name in red , messgae in black and
            cprint(chat.time, 'blue')                       #time details in blue


#if 'y' then you are going to logged in as default user
if user_input.upper() == 'Y':
    # normal operation
    print "Welcome %s  age: %d and rating of: %.1f \nProud to have you onboard" % (spy.name, spy.age, spy.rating)

    start_chat(spy.name, spy.age, spy.rating)                   #function call to start the features of app

else:
    name = raw_input("Hello dear ! Tell me your spy name :  \n")            #ask for the newuser name
    if len(name) > 0 and (name.isalpha() == True or name.isalnum() == True):        #validating the credentials
        salu = raw_input("What should I call you, Mr. or Mrs.? \n")
        name = salu + " " + name
        print "Hello, " + name

        age = input("What is your age? ")                   #analyzing the age of the user according the ranges
        if 12 < age < 50:
            rating = input("What is your spy rating ? ")
            if rating > 4.5:
                print 'Great ace!'
            elif 3 < rating <= 4.5:
                print 'You are one of the good ones.'
            elif 2.5 <= rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            spy = Spy(name, salu, age, rating)                  #object of the new spy is formed after the validations

        else:
            print "Sorry, Your age doesn't fit to be a spy "

        print "Authentication complete.  Welcome %s, age: %d and rating of %.1f\n Proud to have you onboard." % (
            spy.name, spy.age, spy.rating)

        start_chat(spy.name, spy.age, spy.rating)           #start the spychat features

    else:
        print "Spy with this name doesn't exist !!"
