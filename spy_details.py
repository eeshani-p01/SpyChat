# # spy = {
#     'name' : 'Bond',
#     'salu' : 'Dr.',
#     'age' : 23,
#     'rating' : 4.7,
#     'is_online' : True
# }

class Spy:
    def __init__(self, name, salu, age, rating):
        self.name = name
        self.salu = salu
        self.age = age
        self.rating =rating
        self.is_online = True
        self.chats = []
        self.current_status = None