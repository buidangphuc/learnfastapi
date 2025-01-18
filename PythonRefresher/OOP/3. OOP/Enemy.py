class Enemy:

    '''
    Goal: Show Inheritance
    - Implement Zombie object
    - Explain Superclass / super()
    - Override talk function
    - Create SpreadDisease that Parent does not have
    - Create Ogre class
    - Implement Smash
    '''

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")  

    def get_type_of_enemy(self):
        return self.__type_of_enemy