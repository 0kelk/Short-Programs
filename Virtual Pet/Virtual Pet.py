import os.path
import threading
import time
import random
def money_func():
    global money
    global promolevel
    while True:
        if promolevel == 1:
            money = money+10
        elif promolevel == 2:
            money = money+20
        elif promolevel == 3:
            money = money+40
        time.sleep(30)
def promotion_func():
    global promolevel
    if promolevel < 3:
        time.sleep(120)
        y = random.randint(1,10)
        if y == 3:
            print("Woah! You've recieved a promotion, your pay has been raised.")
            promolevel = promolevel+1
def levelamount_func():
    global hunger
    global thirst
    global happiness
    while True:
        if hunger == 0 or thirst == 0:
            print("Oh no! Your pet is not healthy, you must feed them now or the consequences could be fatal.")
            time.sleep(30)
            if hunger == 0 or thirst == 0:
                print("Your pet is unhealthy and hasn't been fed so, unfortunately, they've passed away.")
                os.remove("Virtual Pet.save")
                exit()
        time.sleep(45)
        hunger = hunger-5
        thirst = thirst-5
        happiness = happiness-5
def item_bought():
    global foodamount
    global drinkamount
    global itemamount
    global money
    print("You now have "+str(foodamount)+" packets of food, "+str(drinkamount)+" bowls of water, "+str(itemamount)+" toys and $"+str(money)+".")
z = threading.Thread(target = money_func, name = 'money_thread', daemon = True)
b = threading.Thread(target = promotion_func, name = 'promo_thread', daemon = True)
c = threading.Thread(target = levelamount_func, name = 'levels_thread', daemon = True)
if os.path.exists("Virtual Pet.save") == True:
    f = open("Virtual Pet.save", "r")
    try:
        if f.mode == "r":
            fa = f.readlines()
            animal = fa[0][:-1]
            hunger = int(fa[1])
            thirst = int(fa[2])
            happiness = int(fa[3])
            money = int(fa[4])
            promolevel = int(fa[5])
            foodamount = int(fa[6])
            drinkamount = int(fa[7])
            itemamount = int(fa[8])
    except:
        print("Your save file could not be read, please delete or fix the file and then try again.")
        f.close()
        exit()
    f.close()
    print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
else:
    hunger = 100
    thirst = 100
    happiness = 100
    money = 100
    promolevel = 1
    foodamount = 3
    drinkamount = 3
    itemamount = 1
    animchoice = input("Welcome! Before we begin, would you like your pet to be a Cat or a Dog?\n")
    wloopa = True
    while wloopa:
        animal = animchoice.lower()
        if animal != "cat" and animal != "dog":
            print("Please choose a cat or a dog.")
            animchoice = input("")
        else:
            wloopa = False
    print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
z.start()
b.start()
c.start()
wloopb = True
while wloopb:
    command = input("")
    command = command.lower()
    if command == "check levels":
        print("These are your pet's current levels:")
        print("Hunger: "+str(hunger)+".")
        print("Thirst: "+str(thirst)+".")
        print("Happiness: "+str(happiness)+".")
        print("Money: "+str(money)+".")
        print("Level of promotion: "+str(promolevel)+".")
    elif command == "feed":
        wloopc = True
        while wloopc:
                feedchoice = input("Would you like to feed your pet food or drink?\n")
                if feedchoice.lower() == "food":
                    if foodamount > 0:
                        print("You've fed them some more food and they seem happy.")
                        hunger = 100
                        foodamount = foodamount-1
                        print("You now have "+str(foodamount)+" packets of pet food.")
                        wloopc = False
                    else:
                        print("Sorry, you don't have any more packets of pet food.")
                elif feedchoice.lower() == "drink":
                    if drinkamount > 0:
                        print("You've given them some more drink and they seem happy.")
                        thirst = 100
                        drinkamount = drinkamount-1
                        print("You now have "+str(drinkamount)+" bowls of water.")
                        wloopc = False
                    else:
                        print("Sorry, you don't have any more bowls of water.")
                else:
                    print("Sorry, that is not food or drink.")
    elif command == "shop":
        wloopd = True
        print("Hi! Welcome to the shop.")
        while wloopd:
            print("What would you like to purchase? You can purchase food($50), water($20) and toys($30).")
            a = input("")
            a = a.lower()
            if a == "food":
                if money > 49:
                    print("Ok, you've bought one packet of "+animal+" food.")
                    foodamount = foodamount+1
                    wloopd = False
                    item_bought()
                    money = money-50
                else:
                    print("Sorry, you don't have enough money to purchase "+animal+" food (You can leave by leaving it blank) .")
            elif a == "water":
                if money > 19:
                    print("Ok, you've bought a bowl of water.")
                    drinkamount = drinkamount+1
                    wloopd = False
                    item_bought()
                    money = money-20
                else:
                    print("Sorry, you don't have enough money to purchase water.")
            elif a == "toys":
                if money > 29:
                    print("Ok, you've bought a new toy for your "+animal+".")
                    itemamount = itemamount+1
                    wloopd = False
                    item_bought()
                    money = money-30
                else:
                    print("Sorry, you don't have enough money to purchase a toy.")
            elif a == "":
                wloopd = False
    elif command == "help":
        print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
    elif command == "leave":
        print("Come back soon!")
        wloopb = False
    elif command == "delete save":
        savefileexistsd = True
        deleteconfirm = input("Are you sure you want to delete your save file? y/n\n")
        if deleteconfirm == "y":
            try:
                os.remove("Virtual Pet.save")
            except:
                print("It doesn't seem like you have a save file.")
                print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
                savefileexistsd = False
            if savefileexistsd == True:
                print("Deleting...")
                exit()
            else:
                break
        if deleteconfirm == "n":
            print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
    else:
        print("That isn't a command, sorry.")
        print("You can use these commands:\nCheck levels\nFeed\nShop\nHelp\nLeave\nDelete save")
f = open("Virtual Pet.save", "w")
f.write(str(animal)+"\n"+str(hunger)+"\n"+str(thirst)+"\n"+str(happiness)+"\n"+str(money)+"\n"+str(promolevel)+"\n"+str(foodamount)+"\n"+str(drinkamount)+"\n"+str(itemamount))
f.close()
exit()
