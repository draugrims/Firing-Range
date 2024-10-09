import keyboard 
from asciiart import m1911

magazine = 2
rounds = 7
firearm = 'M1911'

print(m1911)
print("Current Firearm: " + firearm)
print("Magazine capacity: 7")
print("Press X to fire: ")

while True:
    if rounds > 0:
        keyboard.wait('x')
        rounds -=1
        print(rounds)
    else:
        print("Out of ammo. Press R to reload: ")
        keyboard.wait('r')
        rounds = 7
        print(firearm + " reloaded.")
        print("Press X to fire: ")
    