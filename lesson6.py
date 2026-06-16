numberOne = 10 # integer => instance of int class
numberOne = str(numberOne) # converting to string => instance of the text class
# print(type(numberOne))


"""
OOP: 
    - class: instance of an object, think about it like a blueprint to create stuff:
        composed of two parts: 
            - attributes
            - methods (functions/ "behaviors")
        syntax-wise:    
            - we use the key word class
    - object: instance of a class

    - core concepts: 
        - encapsulation: toggle visiblity of attributes
        - inheritance (you take up attribute and methods of a parent you can add more attributes and methods)
        - polymorphism (many forms of something)
"""

#  instance of an object 

class FootballTeam:
    # attributes
    name = "Kenya"
    players = 20 
    coache_name ="John Doe"
    description = "The ultimate African team"
    year = 2026
    game ="World Cup!"

    #  methods
    def train(self):
        print("Kenyan team is training")

    def matchDay(self):
        print("Kenyan team is psyching up!")

    def chnageKit(self):
        print("Swicth to awesome outfits!")

    def celebrate(self):
        print("We WON!!!!")

#  objects: 
teamAKenya = FootballTeam()
teamBKenya = FootballTeam()

# print(f"TEAM: {teamAKenya.name} ")
# print(f"TEAM: {teamBKenya.name}")
# teamAKenya.train()
# teamBKenya.train()

# teamAKenya.celebrate()
# teamBKenya.celebrate()

class FootballTeam:
    #  intialize the class
    def __init__(self, name, nick_name, desciption, coach_name, game):
        self.name  = name
        self.nick_name = nick_name
        self.desciption = desciption
        self.coach_name = coach_name
        self.game = game

      #  methods
    def train(self):
        # print(f"Team {name} is training!") # return an exception since name cannot be found:NameError: name 'name' is not defined
        print(f"Team {self.name} is training!")

    def matchDay(self):
        print("Kenyan team is psyching up!")

    def chnageKit(self):
        print("Swicth to awesome outfits!")

    def celebrate(self):
        print("We WON!!!!")

teamKenya = FootballTeam("Harambee Stars", "Harambee stars", "top team in Africa", "John Doe Kamau", "World Cup")
teamTanzania = FootballTeam("TZ Samahani", "Team Samahani", "features in top 20 teams in Africa", "Bwana Asubuhi", "World Cup")

teamKenya.train()
teamTanzania.train()
