import csv
from spy_details import *
#
# with open("chat.csv.txt","rb") as chats:
#     reader = list(csv.reader(chats))
#     for x in reader:
#         print x
spy = Spy('Bond', 'Mr.', 23, 5)
chats=[]
with open("chat.csv.txt", "rb") as chats_data:
    reader = list(csv.reader(chats_data))

    for row in reader[1:2]:
        # print row[1]

        chatDetails = Chat(row[1], row[2])
        print chatDetails
        chats.append(chatDetails)

print chats
for x in chats:
    print x