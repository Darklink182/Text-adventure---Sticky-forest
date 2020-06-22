import time
import os
import curses
import shutil


txt = " _____ _   _      _           ______                  _   ", \
"/  ___| | (_)    | |          |  ___|                | |  ", \
"\ `--.| |_ _  ___| | ___   _  | |_ ___  _ __ ___  ___| |_ ", \
" `--. \ __| |/ __| |/ / | | | |  _/ _ \| '__/ _ \/ __| __|", \
"/\__/ / |_| | (__|   <| |_| | | || (_) | | |  __/\__ \ |_ ", \
"\____/ \__|_|\___|_|\_\\__, | \_| \___/|_|  \___||___/\__|", \
"                        __/ |                             ", \
"                       |___/                              "

def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))

time.sleep(3)
os.system("clear")
print(" ")
print(" ")
print(" ")
print_center(" _____ _   _      _           ______                  _   ")
time.sleep(.2)
print_center("/  ___| | (_)    | |          |  ___|                | |  ")
time.sleep(.2)
print_center("\ `--.| |_ _  ___| | ___   _  | |_ ___  _ __ ___  ___| |_ ") 
time.sleep(.2)
print_center(" `--. \ __| |/ __| |/ / | | | |  _/ _ \| '__/ _ \/ __| __|") 
time.sleep(.2)
print_center("/\__/ / |_| | (__|   <| |_| | | || (_) | | |  __/\__ \ |_ ") 
time.sleep(.2)
print_center("\____/ \__|_|\___|_|\_\\__, | \_| \___/|_|  \___||___/\__|") 
time.sleep(.2)
print_center("                        __/ |                             ") 
time.sleep(.2)
print_center("                       |___/                              ")

print(" ")
print(" ")
time.sleep(.2)
print("Thanks for playing!")
print("If you want to replay the game, type:,'replay',", \
"if you want to watch the boring", \
"main menu again for no apparent reason, type: 'main'", \
"If you choose to ragequit, we get that,", \
"goodbye. quitter smh.")
print(" ")
print(" ")

while True:
 a = input("> ")
 if a == "replay":
   print("Have fun!")
   time.sleep(.2)
   os.system("clear")
   time.sleep(.2)
   os.system("python game.py")
   break
 if a == "main":
   print("lmao why")
   time.sleep(.2)
   os.system("clear")
   time.sleep(.2)
   os.system("python main.py")
   break

 else:
   print("That's not an option! Try again!")
   continue