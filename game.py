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
     "garden-gem": { ### item: gem ###
        "title": "Garden",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "cottage-key": { ### item: key ###
        "title": "Inside Cottage",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room1": {
        "title": "Starting point",
        "description": "You walked up to a sign at the end of the road, the forest sounding this sign is filled with dangerous animals, the sticky cobwebs hanging between the trees indicate that there are spiders living here, I hope you don’t have arachnophobia. The sign points in two directions, one points to north and one points to west. The path leading North leads to the center of the forest where more beast live, and the path leading West leads to an abandoned cottage that was made by a hunter decades ago",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room2": {
        "title": "Gate",
        "description": "You arrive at the center of the dense forest after fighting of some spiders and sticky monsters, you are standing in front of a stone gate which clearly needs a key to open. You can’t walk around it since it is blocked off with a stone wall which circles around the center of the forest.",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room3": {
        "title": "Outside Church",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room4": {
        "title": "",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room5": {
        "title": "",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
     "room6": {
        "title": "",
        "description": "",
        "options" : {
          "n" : "", 
          "o" : "",
          "z" : "",
          "w" : ""
        }
    },
                        
}


inventory = []

def showRoom(roomId): 
  global dictionary
  
  print("")
  currentRoom = rooms[roomId]
  if currentRoom == rooms["go"] :
    print("𝔾 𝕒 𝕞 𝕖  𝕠 𝕧 𝕖 𝕣")
    print("You will be directed to the credits screen in a sec!")
    os.system("python credits.py")
  
  if currentRoom == rooms["garden-gem"] :
    inventory.append("gem")
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]

  if currentRoom == rooms["cottage-key"] :
    inventory.append("key")
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]
    
  else :
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]

    i = len(roomOptions)
    if i > 4 : 
      print("Enter your direction or action. You can choose from: ")
      for o in roomOptions:
        print(o)
    else:
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

showRoom("room1")
