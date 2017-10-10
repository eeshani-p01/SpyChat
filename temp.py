import csv
from spy_details import *

# #
with open("chat.csv.txt","rb") as chats:
    reader = list(csv.reader(chats))
    for x in reader:
        print x[3]
# spy = Spy('Bond', 'Mr.', 23, 5)
# chats=[]
# with open("chat.csv.txt", "rb") as chats_data:
#     reader = list(csv.reader(chats_data))
#
#     for row in reader[1:2]:
#         # print row[1]
#
#         chatDetails = Chat(row[1], row[2])
#         print chatDetails
#         chats.append(chatDetails)
#
# print chats
# for x in chats:
#     print x
# def load_friends():
# with open("friends.csv.txt", "rb") as friends_data:
#     reader = list(csv.reader(friends_data))
#
#     for row in reader[1:]:
#         spy1 = Spy(row[0],row[1],row[2],row[3])
#         print spy1.name
#         # print row
#         # friends.append(spy1)
