from spy_details import Spy, Chat
from steganography.steganography import Steganography
import csv
import sys  # system module

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']
spy = Spy('Bond', 'Mr.', 23, 5)
friends = []

print "Welcome to SpyChat!!"
question = "Do you want to continue as " + spy.salu + " " + spy.name + "(Y/N)?"
user_input = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    load_message()

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
            pass
        elif menu_choice == 6:
            show_menu = False
        else:
            sys.exit()


def add_status(current_status):
    if current_status is not None:
        print "Your current status message is \" " + current_status + " \"\n"
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        else:
            print "I think, you don't want to update the status !!!"

    elif default.upper() == "Y":
        index = 1
        for status in STATUS_MESSAGES:
            print "{}.{}".format(index, status)
            index = index + 1

        message_select = input("Select from the above status:\n")
        if len(STATUS_MESSAGES) >= message_select:
            updated_status_message = STATUS_MESSAGES[message_select - 1]
            print "Your status is updated."
        else:
            print "You didn't enter any status!!!"

    else:
        print "Your input is invalid !!"

    return updated_status_message


def add_friend():
    # friend_name = raw_input("Please enter your friend's name:")
    # fri = raw_input("Are they Mr. or Ms.?: ")
    # new_friend['name'] = new_friend['salu'] + " " + new_friend['name']
    # new_friend['age'] = input("What's the age?")
    # new_friend['rating'] = input("What is their spy rating?")

    newspy = Spy(raw_input("Please enter your friend's name:"), raw_input("Are they Mr. or Ms.?: "),
                 input("What's the age?"), input("What is their Spy rating?"))
    if (newspy.name.isalpha()==True or newspy.name.isalnum()==True) and newspy.age > 12:
        friends.append(newspy)
        with open("friends.csv.txt","a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([newspy.name,newspy.salu,newspy.age,newspy.rating,True])
        print "Friend Added !!"
    else:
        print "Sorry ! but we can't add this spy to your friend list. "

    return len(friends)


def select_friend():
    item = 0
    for friend in friends:
        print "{}. {}".format(item + 1, friend.name)
        item = item + 1

    select = input("With whom you want to chat? ")

    print "you choose {}".format(friends[select - 1].name)
    return select-1


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of your image?\n ")
    output_path = "hidden.jpg"
    msg = raw_input("What is the secret message to your friend? \n")
    Steganography.encode(original_image, output_path, msg)

    new_chat = Chat(msg, spy.name)
    friends[friend_choice].chats.append(new_chat)
    with open("chat.csv.txt", "a") as chats_data:
        chater = csv.writer(chats_data)
        chater.writerow([friends[friend_choice].name, new_chat.message, new_chat.sent_by,new_chat.time ])

    print "Your secret message has been sent to your friend."


def read_message():
    sender = select_friend()

    input_path = raw_input("What is the name of your secret image?\n")
    secret_text = Steganography.decode(input_path)

    new_chat = Chat(secret_text, False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"


def load_message():
    with open("friends.csv.txt", "rb") as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            spy1 = Spy(row[0],row[1],row[2],row[3])
            friends.append(spy1)


# def load_message():
#     with open("chat.csv", "rb") as Chats:
#         reader = list(csv.reader(Chats))
#
#         for row in reader[1:]:
#             spy1 = Spy(row[0],row[1],row[2],row[3])
#             friends.append(spy1)


if user_input.upper() == 'Y':

    # normal operation
    print "Welcome %s  age: %d and rating of: %.1f \nProud to have you onboard" % (spy.name, spy.age, spy.rating)

    start_chat(spy.name, spy.age, spy.rating)

else:
    name = raw_input("Hello dear ! Tell me your spy name :  \n")
    if len(name) > 0 and (name.isalpha() == True or name.isalnum() == True):
        salu = raw_input("What should I call you, Mr. or Mrs.? \n")
        name = salu + " " + name
        print "Hello, " + name

        age = input("What is your age? ")
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

            spy = Spy(name, salu, age, rating)

        else:
            print "Sorry, Your age doesn't fit to be a spy "

        print "Authentication complete.  Welcome %s, age: %d and rating of %.1f\n Proud to have you onboard." % (
            spy.name, spy.age, spy.rating)

        start_chat(spy.name, spy.age, spy.rating)

    else:
        print "Spy with this name doesn't exist !!"
