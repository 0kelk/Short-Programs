import random
import time
print("Welcome to a text adventure! Due to unfortunate circumstances, you just woke up on a deserted island.")
print("It's tiny, but with no doubt has many secrets to be found!")
print("You should try your best to make your way home with the resources you can get.")
inven = []
startitem = random.randint(1,5)
if startitem == 1:
    startitem = "Axe"
if startitem == 2:
    startitem = "Freshly Baked Meat Pie"
if startitem == 3:
    startitem = "Paperclip"
if startitem == 4:
    startitem = "Rope"
if startitem == 5:
    startitem = "Crowbar"
inven.append(startitem)
placeselectstat = "true"
time.sleep(2)
print("What's this? It seems that alongside your backpack, you've actually been carrying a/an "+startitem+", how did that get there...")
time.sleep(2)
print("After looking around you can see 4 landmarks, a Cave, an Extremely Large Tree, a Beach and a Gushing Waterfall.")
print("You decide to explore one, but you aren't sure which one.")
placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
pss = True
while pss == True:
    if placeselect == "Cave":
        print("You reckon that you should explore the cave")
        break
    if placeselect == "Tree":
        print("You reckon that you should explore the Tree")
        break
    if placeselect == "Beach":
        print("You reckon that you should explore the Beach")
        break
    if placeselect == "Waterfall":
        print("You reckon that you should explore the Waterfall")
        break
    if placeselect == "Barrels":
        print("Wow! You could of sworn this wasn't here before... but now that you are here, it's probably smart to look inside the barrels.")
        time.sleep(2)
        inven.append("Mug")
        inven.append("Basket")
        inven.append("Dog Food")
        print("Strange, a Mug, a Basket and a thick packet of Hungry Dog's Dog Food™")
        print("You now have the following items in your backpack:")
        for x in range(len(inven)):
            print(inven[x])
        print("Let's see where else we can go.")
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n") 
    else:
        print("You can't see one of those, you decide to pick where to go.")
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
eps = True
ops = True
cavecont = ""
treecont = ""
beachcont = ""
while eps == True:
    while ops == True:
        if placeselect == "Cave":
            print("You walk into the cave, it's dark and musty and makes you shiver")
            print("3 silent figures all fly around you...")
            print("You take a closer look and discover that they are bats... yuck.")
            cavecont = input("Will you continue and find out what other.. suprises the cave holds? y/n")
            break
        if placeselect == "Tree":
            print("You are amazed by this marvel of nature, it's absolutely humongous!")
            print("Such a tree would provide one with stunning and useful views from the top.")
            print("Since you were always good at rock climbing, maybe you shoud try climb it.")
            print("However, that might not help at all.")
            treecont = input("So will you climb it? y/n")
            break
        if placeselect == "Beach":
            print("Ahh, the ocean.")
            print("You love the blue and the marine life that lives inside.")
            print("Surrounded by palm trees and coconuts, this is a place of wonders.")
            print("You decide to grab one of the coconuts, for later.")
            time.sleep(2)
            inven.append("Coconut")
            print("You now have the following items in your backpack:")
            for x in range(len(inven)):
                print(inven[x])
            print("You realise, this wood looks very healthy. You could make a place to camp at.")
            beachcont = input("Do you want to build a place to camp? y/n")
            break
        if placeselect == "Waterfall":
            print("You walk over to the waterfall, you can feel little droplets of water on your hot face.")
            print("Cupping your hands, you drink a bit of the water and feel very refreshed and hydrated.")
            print("You wonder if there is any way that you could store this water...")
            if inven.count("Coconut")>1:
                print("Wait! There is, you remember you have a coconut. So you carve out the insides and scoop in some water.")
                inven.append("Mug of Water")
                print("You now have the following items in your backpack:")
                for x in range(len(inven)):
                    print(inven[x])
            if inven.count("Mug")>1:
                print("Wait! There is, you remember you have a mug. So you fill up the mug with water.")
                inven.append("Mug of Water")
                print("You now have the following items in your backpack:")
                for x in range(len(inven)):
                    print(inven[x])
            else:
                print("You'll have to think about it... but for now you decide to head back out to the clearing you woke up in.")
            placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
        else:
            print("You can't see that, where should you go?")
            placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if cavecont == "n":
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if treecont == "n":
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if beachcont == "n":
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if cavecont == "y":
        print("You walk in and immediately feel the cold in the area.")
        print("You walk as far as you can see and find the end of the cave.")
        print("It seems to be a dead end")
        print("You go back.")
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if treecont == "y":
        print("You begin the long and hard climb to the top.")
        print("Halfway there your left foot begins to sleep, you start falling.")
        print("Whether it be by good reflexes, or good fortune, we may never know.")
        print("But you caught a small, weak branch and are safe.")
        print("You carefully climb up this time, and reach the top.")
        print("You can mostly see the beautiful ocean.")
        print("A lovely larger island is off in the distance.")
        print("Wait, are those buildings?")
        print("No, no. Must be a figment of your imagination.")
        print("You climb back down")
        placeselect = input("Where do you want to go? Cave/Tree/Beach/Waterfall\n")
    if beachcont == "y":
        print("You spend the rest of your day snapping and breaking, placing and building.")
        print("When night grows near, you admire your wonderful work on this project.")
        print("The hut of sorts has thin walls and leaves on top to protect it's inhabitant from the worst of weather.")
        print("So you clear out a little area inside, because it seems best you get some rest.")

        
        
        
        
