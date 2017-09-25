from spy_details import spy_name,salu,spy_age,spy_rating

print "Welcome to SpyChat!!"
question = "Want to Continue as " + salu + " " + spy_name + "(Y/N)?"
print question
user_input = raw_input("Enter your choice\n")

if user_input == 'Y':
    #normal operation
    pass    # a keyword to just pass the execution

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

    else:
        print "This spy doesn't exist !!"
