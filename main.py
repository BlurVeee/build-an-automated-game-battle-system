import random
import os,time

def Dice(side):
  number = random.randint(1,side)
  return number

def Roll():
  Dice_6 = Dice(6)
  Dice_12 = Dice(12)
  health = (Dice_6 * Dice_12 / 2) + 10
  return health
  
def Roll_2():
  Dices_6 = Dice(6)
  Dices_12 = Dice(12)
  strength =  (Dices_6 * Dices_12 / 2 ) + 12
  return strength 
  

print("Welcome to your character builder")
print()
name = input("Name your character: ")
print(name, "is a nice name")
print()
time.sleep(0.7)
type = input("Select your character body type (Elf, Humain, dragon or Orc): ")
time.sleep(0.3)
print("That a interesting choice")
print()
health = int(Roll())
strength = int(Roll_2())
print(name, " of the", type, "specie")
time.sleep(0.6)
print("HEALTH:", health)
time.sleep(0.6)
print("STRENGTH:", strength)
time.sleep(1)
print()
print()
print("Who is", name, "fighting")
print()
print()
time.sleep(1)
print("Welcome to your character builder")
print()
name_1 = input("Name your character: ")
print(name_1, "is a nice name")
print()
time.sleep(0.7)
type_1 = input("Select your character body type (Elf, Humain, dragon or Orc): ")
time.sleep(0.3)
print("That a interesting choice")
print()
health_1 = int(Roll())
strength_1 = int(Roll_2())
print(name_1, " of the", type_1, "specie")
time.sleep(0.6)
print("HEALTH:", health_1)
time.sleep(0.6)
print("STRENGTH:", strength_1)
print()
time.sleep(0.5)
print("IT IS BATTLE TIME")
time.sleep(4)
os.system("clear")



round =+ 1

while True:
  time.sleep(4)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  
  C1Roll = Dice(6)
  C2Roll = Dice(6)
  
  dmg = abs(strength - strength_1) + 1 
  
  if C1Roll > C2Roll:
    time.sleep(0.8)
    print(name, "Get the hit on", name_1, "doing", dmg,"damage in round", round)
    time.sleep(1)
    print()
    health_1 -= dmg
    print(name)
    print("HEALTH:",health)
    print()
    print(name_1)
    print("HEALTH:",health_1)
    
  
    
  
  elif C2Roll > C1Roll:
    time.sleep(0.8)
    print(name_1, "Get the hit on", name, "doing", dmg,"damage in round", round)
    print()
    health -= dmg
    time.sleep(1.)
    print(name)
    print("HEALTH:",health )
    print()
    print(name_1)
    print("HEALTH:",health_1)
    print()
    


  elif C2Roll == C1Roll:
    time.sleep(0.8)
    print("Both characters missed there attack on round", round)
      
    
  if health <= 0:
    print()
    time.sleep(2)
    print(name_1, "has deafeated", name)
    time.sleep(1)
    print(name_1, "IS THE WINNER AFTER", round, "OF FIGHTING", name)
    break
    
  elif health_1 <= 0:
    print()
    time.sleep(2)
    print(name, "has deafeated", name_1)
    time.sleep(1)
    print(name, "IS THE WINNER AFTER", round, " ROUND OF FIGHTING", name_1)
    break

  elif health_1 and health > 0:
    print()
    print("both", name, "and", name_1, "are standing ready the next round")
    round += 1

  