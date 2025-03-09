import asyncio
import os
from random import randint
import time
import threading
from playsound import playsound
global caught_fish
global fish_list
global inventory
difficulty_level = 1
fish_luck = 0
fish_list = [
        "Flimsy Fish", "Training Fish", "Plastic Fish", "Carbon Fish", "Fast Fish",
        "Lucky Fish", "Long Fish", "Steady Fish", "Nocturnal Fish", "Fortune Fish",
        "Rapid Fish", "Magnet Fish", "Midas Fish", "Mythical Fish", "Kings Fish",
        "Destiny Fish", "Magma Fish", "Fungal Fish", "Haunted Fish", "Sockeye Salmon",
        "Pearl Fish", "Glassfish", "Magma Tang", "Golden Fish", "Cursed Fish",
        "Kingfish", "Jellyfish", "Blubberfish", "Shimmering Fish", "Goldfin Fish",
        "Pearl Cichlid", "Dragon Fish", "Titanfish", "Whirlpool Fish", "Moonlit Fish",
        "Sunfish", "Stardust Fish", "Frostbite Fish", "Fishy Fish", "Flamefish", "Spiked Fish",
        "Razorfin Fish", "Vortex Fish", "Tornado Fish", "Seafury Fish", "Mantis Fish",
        "Glimmer Fish", "Neon Fish", "Crystal Fish", "Sandfish", "Obsidian Swordfish",
        "Oceanic Fish", "Megalodon", "The Bloop", "Fishy Fishity Fishing Fished Fish"
    ]
rods_str = "Flimsy Rod,Training Rod,Plastic Rod,Carbon Rod,Fast Rod,Lucky Rod,Long Rod,Steady Rod,Nocturnal Rod,Fortune Rod,Rapid Rod,Magnet Rod,Midas Rod,Mythical Rod,Kings Rod,Destiny Rod,Magma Rod,Fungal Rod,Haunted Rod,Executive Rod,Golden Rod,Legendary Rod,Inferno Rod,Aqua Rod,Celestial Rod,Thunder Rod,Frost Rod,Solar Rod,Lunar Rod,Crystal Rod,Phantom Rod,Diamond Rod"
rods = rods_str.split(",")
sequence = []
a, b = 0, 1
for _ in range(10):
    sequence.append(a)
    a, b = b, a + b
sequence.pop(0)
rod_boost = 10
inventory = {}
for i in range(len(rods)):
    inventory[rods[i] + "🎣"] = 0
for i in range(len(fish_list)):
    inventory[fish_list[i] + "🐟"] = 0
difficulty_level = 1

def play_music(filename):
    playsound(filename)

    

async def menu():
    global caught_fish
    while True:
        menu_inputs = ["fish", "shop", "inventory", "settings"]
        menu_input = input("\n     MENU📕     \n\n-----fish-----🦈\n\n-----shop-----🪙\n\n--inventory---🧰\n\n---settings---⚙️\n")
        if menu_input not in menu_inputs:
            while menu_input not in menu_inputs:
                print("That is not an available option.\nTry again\n\n")
                menu_input = input("\n     MENU📕     \n\n-----fish-----🦈\n\n-----shop-----🪙\n\n--inventory---🧰\n\n---settings---⚙️\n")
        
        if menu_input == menu_inputs[0]:
            await Fish_menu()
        elif menu_input == menu_inputs[1]:
            shop_menu()
        elif menu_input == menu_inputs[2]:
            print(str(inventory) + f"\n    credit: {fish_credit}💰")
        elif menu_input == menu_inputs[3]:
            await settings_menu()


def shop_menu():
    global rod_boost
    global fish_credit
    shop_dict = {}
    for i in range(1, len(rods) - 1):
        shop_dict[rods[i]] = str(i * 1250) + "💰"

    print("Here are the available items\n")
    print(shop_dict)
    print("Credit: " + str(fish_credit) + "💰")
    buy_item = input("\n\nWhat would you like to buy?🎣")
    if int(str(shop_dict.get(buy_item).replace("💰", ""))) > fish_credit:
        print("You can't afford that item. ")
    else:
        print(f"{buy_item} bought")
        fish_credit -= int(shop_dict.get(buy_item).replace("💰", ""))
        print(f"Your credit is now {fish_credit}")
        inventory[buy_item + "🎣"] += 1
        rod_boost = rods.index(buy_item)+11
        


async def Fish_menu():
    
    global caught_fish_inventory_addon
    global fish_list
    global fish_credit
    global caught_fish
    
    
    def fish_chance():
        
        global rod_boost
        global fish_credit
        global caught_fish
        global caught_fish_inventory_addon
        fish_forloop_count = 1
        
        for i in range(0, len(fish_list)):
            fish_forloop_count += 1
            randint_fish = randint(1, 100)
            fish_choosed = 0

            if randint_fish < ((100/fish_forloop_count)/(rod_boost/10)):
                rand_fish_emoji = ["🐟","🐠","🐡","🦈"]
                caught_fish = fish_list[i] + rand_fish_emoji[randint(0, 3)]
                caught_fish_inventory_addon = fish_list[i]
                fish_credit += i * 100
                fish_choosed = 1
                break
            else:
                pass
        if fish_choosed == 1:
            pass
        elif fish_choosed == 0:
            while fish_choosed == 0:
                fish_forloop_count = 1
        
                for i in range(0, len(fish_list)):
                    fish_forloop_count += 1
                    randint_fish = randint(1, 100)
                    fish_choosed = 0
        
                    if randint_fish > ((100/fish_forloop_count)*(rod_boost)):
                        rand_fish_emoji = ["🐟","🐠","🐡","🦈"]
                        caught_fish = fish_list[i] + rand_fish_emoji[randint(0, 3)]
                        caught_fish_inventory_addon = fish_list[i]
                        fish_credit += i * 100
                        fish_choosed = 1
                        break
                    else:
                        pass
                
       
    def fish_script():
        print("Write the correct number within 1 second to catch a fish")
    async def fish():
        
        global caught_fish_inventory_addon
        global caught_fish
        random_number_f = randint(0, 9)
        print(f"{random_number_f}")
        global pass_
        global time_
        fish_chance()
        pass_ = 0
        time_ = 1.5

        try:
            print()
            user_input = await asyncio.wait_for(asyncio.to_thread(input), time_)
            if int(user_input) != random_number_f:
                print("You caught nothing❌")
                pass_ = 0
            else:
                print(f"You caught {caught_fish}")
                print("Credit: " + str(fish_credit) + "💰")
                inventory[caught_fish_inventory_addon + "🐟"] += 1
                pass_ = 1
                time.sleep(1)
        except (asyncio.TimeoutError, ValueError):
            print("You caught nothing❌")
            pass_ = 0
            

    fish_script()
    time.sleep(1)
    while 6999 == 6999:
        await fish()
        if pass_ == 0:
            print("\nGoing to menu...\nType a random key to resume to the menu.\n")
            break


async def settings_menu():
    global difficutly_level
    setting_inputs = ["directions", "music", "reset", "quit"]
    
    while True:
        setting_input = input("     settings⚙️    \n\n-----directions-----📜\n\n-------music--------🔊\n\n-----reset--------♻️\n\n-----quit----------❌\n")

        if setting_input not in setting_inputs:
            print("That option is unavailable.\nPlease try again.\n")
            continue

        if setting_input == "directions":
            print("in this game you have to catch fish\nafter you catch a fish you can buy rods\n rods upgrade your rare fish catch chance so try to buy one as soon as possible\n to look/view your progress, choose inventory on the main menu\nthe difficulty settings make it so there is a chance that the fishes will eat you\nthe reset option is still in development\nto exit settings, choose the quit option\nthank you:)!")
            time.sleep(1)
            

        elif setting_input == "music":
            threading.Thread(play_music("Procrastinating Jazz.mp3"))
            
            

        elif setting_input == "reset":
            print("This option is still in development.\nReturning to menu...\n")
            break

        elif setting_input == "quit":
            print("quitting settings...")
            time.sleep(1)
            break


async def start():
    global caught_fish
    global fish_credit
    fish_credit = 550
    while True:
        try:
            await menu()
        except Exception as e:
            continue
       


asyncio.run(start())
