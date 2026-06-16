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

# teamKenya.train()
# teamTanzania.train()



class Vehicle:
    #  initialization
    def __init__(self, owner, model, yom, color, is_petrol, is_four_wheel_drive, is_hybrid, is_electric, log_book_ref):
        self.model = model
        self.owner = owner
        self.yom = yom
        self.color = color
        self.is_petrol = is_petrol
        self.is_four_wheel_drive = is_four_wheel_drive
        self.is_hybrid = is_hybrid
        self.is_electric = is_electric
        self.__log_book_ref = log_book_ref # encapsulation, wehreby we are restricting access to an attribute locally 

    def drive(self):
        print(f"{self.owner}'s Vehicle, {self.model}, goo vrooom! ")

    def description(self):
        print(f"""
        Vehicle of model {self.model} was manufactured in the year {self.yom} it is color {self.color}
         and consumes {'PETROL' if self.is_petrol else 'DIESEL'}. It is {'4x4' if self.is_four_wheel_drive else '2WD'}
         """)

    def getLogBook(self):
        print(f"{self.owner}'s log book humber is {self.__log_book_ref}")

johnsCar = Vehicle("John", "Honda",2017,"black", True, True, False, False,"JKLOGBK-12345634363")
marysCar = Vehicle("Mary","Hyundai", 2020, "pink", True, False, True, True,"MWLOGBK-99999990909")

# johnsCar.drive()
# print(johnsCar.color)
# print(johnsCar.__log_book_ref) #AttributeError: 'Vehicle' object has no attribute '__log_book_ref'
# marysCar.getLogBook() # this will work
# johnsCar.getLogBook() # this will work
# marysCar.drive()


#  inheritance => the parent is Vehicle and the child is Tuktuk
class TukTuk(Vehicle):
    def __init__(self, owner, model, yom, color, is_petrol, is_four_wheel_drive, is_hybrid, is_electric, log_book_ref, purpose, is_registered_on_uber):
        super().__init__(owner, model, yom, color, is_petrol, is_four_wheel_drive, is_hybrid, is_electric, log_book_ref)
        self.purpose = purpose
        self.is_registered_on_uber =is_registered_on_uber 

# polymorphism
    def drive(self):
            print(f"{self.owner} is riding a Tuktuk of model  {self.model} !! ")


redTuktuk = TukTuk("Jerry", "HONDA",2014,"RED", True, False, False, False,"JKLOGBK-12345TKTK","MZIGO", False)
blueTuktuk = TukTuk("MICKEY", "TVS",2017,"BLUE", True, False, False, False,"MKLOGBK-UKUK34363", "TRANSPORTING PEOPLE", True)


redTuktuk.description()
blueTuktuk.description()
print("==============================================")
redTuktuk.drive()
blueTuktuk.drive()
print(redTuktuk.purpose)