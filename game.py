import os
import time

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
        "description": "You decide to store the gem in your backpocket. You look around but you can't find anything more here. Your only option is to return to the front of the cottage.",
        "options" : {
          "return" : "room13", 
        }
    },
     "cottage-key": { ### item: key ###
        "title": "Attic",
        "description": "You grabbed it getting the feeling that it might be useful. You look around but you can't find anything more here. Your only option is to return downstairs.",
        "options" : {
          "return" : "room14", 
        }
    },
     "room1": {
        "title": "Starting point",
        "description": "You walked up to a sign at the end of the road, the forest sounding this sign is filled with dangerous animals, the sticky cobwebs hanging between the trees indicate that there are spiders living here, I hope you don’t have arachnophobia. The sign points in two directions, one points to north and one points to west. The path leading North leads to the center of the forest where more beast live, and the path leading West leads to an abandoned cottage that was made by a hunter decades ago",
        "options" : {
          "n" : "room2", 
          "w" : "room13",
          "examine" : "room20"
        }
    },
     "room2": {
        "title": "Gate",
        "description": "You arrive at the center of the dense forest after fighting of some spiders and sticky monsters, you are standing in front of a stone gate which clearly needs a key to open. You can’t walk around it since it is blocked off with a stone wall which circles around the center of the forest.",
        "options" : {
          "s" : "room1", 
        }
    },
     "room3": {
        "title": "Outside Church",
        "description": "After you unlocked the gate and walked into the enclosed space you see a rundown church at the center of the clearing. The church is surprisingly not rundown and all the windows are intact. You can either enter the church or explore the church's surroundings.",
        "options" : {
          "return" : "room2", 
          "enter" : "room4",
          "explore" : "room7",
        }
    },
     "room4": {
        "title": "Inside Church",
        "description": "As you enter the church you see that everything is moved out of it. There is only a empty space inside and the floor is clear of any obstacles. You see two doors leading to different places. One to the left of you leads to the balcony and the other at the other side of the church leads to the back of the church.",
        "options" : {
          "return" : "room3", 
          "balcony" : "room5",
          "backroom" : "room10",
        }
    },
     "room5": {
        "title": "Balcony",
        "description": "You walk up the cramped stairs, when you reached the top of the chairs you see the Balcony from where you can see the church’s floor from an higher viewpoint, on the floor which you couldn’t see when you stood on the ground floor is a pentagram drawn in blood,  Having read to many fictions you get an idea..",
        "options" : {
          "return" : "room4", 
          "pentagram" : "room6",
        }
    },
     "room6": {
        "title": "Pentagram",
        "description": "Feeling drawn to it by some evil force you cannot resist dropping your blood on the Pentagram. And offering your soul to the devil.",
        "options" : {
          "drop" : "go", 
        }
    },
     "room7": {
        "title": "Graveyard",
        "description": "After you walked around the church you reach the graveyard that is located behind the church, you see a graveyard that looks like any other graveyard but the feeling you get from it is different, more mysterious than others. This gets your attention and you decide to look around. You are not afraid of what might lurk in the dark but you are still cautious nonetheless.",
        "options" : {
          "return" : "room3", 
          "examine" : "room8",
        }
    },
     "room8": {
        "title": "Graveyard",
        "description": " You decide to examine the graveyard in better detail, something is telling you to do so, and this feeling has yet to betray you. Following this feeling you see a statue of someone you are somewhat familiar with but you don’t know who. After looking at the statue for sometime you notice that the statue has a note stuck on its back.",
        "options" : {
          "read" : "note", 
          "return" : "room7",
        }
    },
     "note": {
        "title": "Dream",
        "description": "You read the note, the note said read that the statue was of a man named Daan. You recall the name, the name belonged to a man who was well known for his schemes. Knowing who’s grave or whatever this place is you step back, but before you could do anything you blink and the statue is gone, so is the note. And soon after you fall unconscious.",
        "options" : {
          "wake" : "room9", 
        }
    },
     "room9": {
        "title": "Dream",
        "description": "After waking up from what seems like an eternity you see the familiar sign that you walked past at the beginning of entering this forest. You feel around for familiar objects that you collected on your way to the graveyard and they are still there. Nothing feels off so you look around to see if anything's changed, everything is in the same place as you left it, nothing has changed except that when you looked at the central area of the forest that the gate and the church are gone.",
        "options" : {
          "inspect" : "room18", 
        }
    },
     "room10": {
        "title": "Backroom",
        "description": "You walk across the church to reach the door that leads to the back of the church. When you open the door the door has some resistance but nothing you can't handle. After pushing the door open you hear some boxes fall to the ground. The only thing you see in the backroom are empty boxes with nothing in it, you realise that being in here is a waste of time.",
        "options" : {
          "return" : "room4", 
        }
    },
     "room11": {
        "title": "Garden",
        "description": "All the plants have been eaten or died out, the part that the plants are eaten isn’t weid, but the pat about them being dead is. Looking closer to see the cause of death you notice the ground has also lost its life, dark and scorched earth.",
        "options" : {
          "return" : "room13", 
          "examine" : "room12",
        }
    },
     "room12": {
        "title": "Garden",
        "description": "You decide to look for the cause of this loss of life, there should be plenty of water accessible here so that is not the case and there are no burn marks on any plants so how can the ground be scorched like that? Whilst investigating you notice something reflecting light into your eyes, you look at it and find a red gem. The shape of the gem looks a bit familiar, but you can't remember from where? Do you put it back down or store it for later?",
        "options" : {
          "store" : "garden-gem", 
          "throw" : "room11",
        }
    },
     "room13": {
        "title": "Outside Cottage",
        "description": "You arrive at the abandoned cottage, staring at the broken windows and run down walls like a dumb idiot you notice that the door is slightly opened",
        "options" : {
          "e" : "room1", 
          "enter" : "room14",
          "explore" : "room11",
        }
    },
     "room14": {
        "title": "Inside Cottage",
        "description": "You decide to force the old door open to enter the cottage, my oh my what will you find?",
        "options" : {
          "leave" : "room13", 
          "examine" : "room15",
          "ransac" : "room19",
        }
    },
     "room15": {
        "title": "Metal door",
        "description": "You look closely at the door, examining the rusty lock. The lock is barely intact",
        "options" : {
          "break" : "room16", 
          "return" : "room14",
        }
    },
     "room16": {
        "title": "Stairs",
        "description": "The lock is rusty, maybe you can smash it open. You grab a fallen down chair and smash the lock like an idiot. The lock breaks but so does the chair. The door opens and you see stairs leading to the attic",
        "options" : {
          "climb" : "room17", 
          "return" : "room14",
        }
    },
     "room17": {
        "title": "Attic",
        "description": "You walked up the stairs that lead to the attic, once you arrived at the top of the stairs you see a dusty and old attic. Every box is covered in dust and some are webbed by spider webs. After your coughing fit you notice you almost missed a shiny silver box with a key in it. ",
        "options" : {
          "explore" : "cottage-key", 
          "return" : "room14",
        }
    },
     "room18": {
        "title": "End",
        "description": "The end? that is the question, now that you ended up in a spider's trap you obviously will die since miracles don’t exist. I could make this a longer story but making it even my of an eyesore is just torturing the poor soul who is reading this, you have my compassionate condolences for your loss of brain cells, if you even had any. Now that this story of utter Bullsh*t has ended I hope you… enjoyed?",
        "options" : {}
    },
     "room19": {
        "title": "Ransac",
        "description": "You search every drawer and cabinet, all you find are dusty cobwebs and diseased rats, do you want to stop looking?",
        "options" : {
          "stop" : "room14", 
        }
    },
     "room20": {
        "title": "Sign",
        "description": "You decide to look closer at the sign, after looking at it you notice something behind it, an overgrown statue that has a gem shape inside it.",
        "options" : {
          "return" : "room1", 
        }
    },
     "Ingem": {
        "title": "You put the red gem you found in it, which resulted in burning the whole forest down. Your only options now are to commit suicide or to let yourself be consumed by the flames.",
        "description": "",
        "options" : {
          "burn" : "go", 
          "suicide" : "go",
        }
    },
    
    
                        
}




def showRoom(roomId): 
  global dictionary
  
  print("")
  currentRoom = rooms[roomId]
  if currentRoom == rooms["go"] :
    
    print("𝔾 𝕒 𝕞 𝕖  𝕠 𝕧 𝕖 𝕣")
    print("You will be directed to the credits screen in a sec!")
    os.system("python credits.py")
  
  if currentRoom == rooms["garden-gem"] :
    
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]
    rooms['room20']['options']['place gem'] = 'Ingem'

  if currentRoom == rooms["cottage-key"] :
    
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]
    rooms['room2']['options']['unlock'] = 'room3' 

  if currentRoom == rooms["room18"] :
    
    print(currentRoom["title"])
    print(currentRoom["description"])    
    time.sleep(5)
    os.system("python credits.py")

  else :
    print(currentRoom["title"])
    print(currentRoom["description"])
    roomOptions = currentRoom["options"]

    i = len(roomOptions)
    if i > 4 : 
      print(' ')
      print("Enter your direction or action. You can choose from: ")
      for o in roomOptions:
        print(o)
    else:
      print(' ')
      print("Enter your direction or action. You can choose from:  ")
      for o in roomOptions:
        print(o)
    
    print(' ')
    print("Make a choice")
    optionChosen = input("> ")
    if optionChosen not in roomOptions.keys():
      print("You can't go that way!")
      showRoom(roomId)

    roomId = roomOptions[optionChosen]

    showRoom(roomId)

showRoom("room1")
