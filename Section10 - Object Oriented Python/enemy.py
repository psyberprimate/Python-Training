import random


class Enemy(object):

    def __init__(self, name : str ="Enemy", hit_points : int = 0, lives : int = 1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        damage_overflow = remaining_points
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"{self._name} takes {damage} damage!")
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{} loses a life".format(self._name))
            else:
                print(f"{self._name} dies from the damage")
                self.alive = False                  

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)
    

class Troll(Enemy):
    ##pass
    def __init__(self, name : str):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}! {0.name} stopm you".format(self)) 
        print(f"Me {self._name}! {self._name} eat you!")    


class Vampire(Enemy):
    
    def __init__(self, name : str, hit_points : int):
        super().__init__(name=name, lives = 3, hit_points=hit_points)

    def take_damage(self, damage):
        if not self.dodges():
            return super().take_damage(damage=damage)

    def dodges(self):

        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges the blow *****".format(self))
            return True
        else:
            return False
        

class VampireKing(Vampire):

    def __init__(self, name : str):
        super().__init__(name=name, hit_points = 140)
        

    def take_damage(self, damage):
        super().take_damage(damage // 4)           