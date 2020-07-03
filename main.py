import time
import os
import sys
import cursor

os.system('clear')

time.sleep(2)

print("\t**********************************************")
print("\t***  Hi there! - Welcome to Sticky Forest  ***")
print("\t**********************************************")

time.sleep(.2)
print('Before we begin, we should probably introduce ourselves!')
time.sleep(.2)
print(' ')
time.sleep(.2)
print('Sticky Forest is a text based adventure game')
time.sleep(.2)
print('This project was made on assignment for dhr. Logtenberg')
time.sleep(.2)
print('For the subject Informatica at Sint-Maartenscollege, Voorburg')
time.sleep(.2)
print(' ')
time.sleep(.2)
print('A production by')
print('Daniël Sylvester Prévoo & Julian Bakx')
time.sleep(.2)
for e in range(5):
  time.sleep(.2)
  print(' ')


print("To start the game type 'start'")
print("First time? We advice you to type 'new' before starting!")



while True:
 d = input()
 if d == "start":
   print("(i) = investigate \
   (r) = return \
   (n, s, w, e) = north, south, west, east \
   (exa) = examine \
   (exp) = explore \
   (u) = unlock \
   (c) = continue ")
   time.sleep(.2)
   os.system("python game.py")
   break
 if d == "new":
   print(' ')
   print("(i) = investigate \
   (r) = return \
   (n, s, w, e) = north, south, west, east \
   (exa) = examine \
   (exp) = explore \
   (u) = unlock \
   (c) = continue \
   You can now type 'start' to begin!")
   continue
 else:
   print("That's not an option! Try again!")
   continue






