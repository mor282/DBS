

class CrewMember:
    def __init__(self,profile_tuple):
        self.id = profile_tuple[0]
        self.name = profile_tuple[1]
        self.gender = profile_tuple[2]
        self.age = profile_tuple[3]
        self.main_department = profile_tuple[4]
        self.popularity = profile_tuple[5]
        self.biography = profile_tuple[6]
        self.pic = profile_tuple[7]


def print_profile(self):
    print("Name: {self.name}")
    print("main_department: {self.main_department}")
    print("popularity: {self.popularity}")
    
