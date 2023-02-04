import time
import random

import weapons

m16a1 = weapons.Gun('M16A1',15)

print("Your ammo: ",m16a1.ammo)
Player = input("Do you want to add some ammo? (Y/N)")
if(Player == 'Y'):
    print("Your can't have a ammo more than 20")
    new_ammo = int(input("Add your ammo: "))
    m16a1.add_ammo(new_ammo)
else:
    print("No ammo added.")

print("Your ammo: ",m16a1.ammo)
time.sleep(2)

print("Enermy Spotted!")
time.sleep(2)
print("Shoot!!!!")
time.sleep(3)
m16a1.fire_ammo()
time.sleep(2)
print("The enermy was killed!")
time.sleep(2)
print("Your ammo: ",m16a1.ammo)