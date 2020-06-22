import os

rooms = {
    "go": { #### go = gameover ####
        "title": "",
        "description": "",      
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room2": {
        "title": "",
        "description": "",
        "options" : {
          "n" : "go", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    }
}


inventory = {}

def showRoom(roomId): 
  global dictionary
  
  print("")
  currentRoom = rooms[roomId]
  if currentRoom == rooms["go"] :
    os.system("python credits.py")
  else :
   print(currentRoom["title"])
   print(currentRoom["description"])
   roomOptions = currentRoom["options"]
   print("Enter in what direction you want to move. You can choose from: ")
   for o in roomOptions:
     print(o)

   print("Make a choice")
   optionChosen = input("> ")
   if optionChosen not in roomOptions.keys():
     print("You can't go that way!")
     showRoom(roomId)

   roomId = roomOptions[optionChosen]

   showRoom(roomId)

showRoom("room2")
