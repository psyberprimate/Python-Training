#from player import player
import player
import enemy

tim = player.Player("TIMEY")

Enemy1 = enemy.Enemy("Basic enemy", 12, 1)
print(Enemy1)

# Enemy1.take_damage(4)
# print(Enemy1)

# Enemy1.take_damage(12)
# print(Enemy1)

# Troll1 = enemy.Troll("Nogg")
# print(Troll1)

# Troll2 = enemy.Troll("Ogg")
# print(Troll2)

# Troll1.grunt()
# Troll2.grunt()

# Troll2.take_damage(22)


VampireCount = enemy.Vampire("Klauss", 50)

VampireServant = enemy.Vampire("Servant", 15)

VampireKing = enemy.VampireKing("Vlad Tepes")
# VampireServant.take_damage(30)

# VampireCount.take_damage(75)

# print(VampireServant)
# print(VampireCount)

# VampireServant.take_damage(10)
# print(VampireServant)

# VampireServant.take_damage(5)
# print(VampireServant)

# VampireServant.take_damage(5)
# print(VampireServant)

# while VampireCount.alive:
#     VampireCount.take_damage(10)
#     print(VampireCount)

while VampireKing.alive:
    VampireKing.take_damage(10)
    print(VampireKing)    