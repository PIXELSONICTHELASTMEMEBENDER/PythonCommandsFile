global name
import random


class myfirstClass:
    # Intro to Variables
    amazingVariable = str(1)

    goodVariable = str("pay respects")

    firstVariable = int(1)

    if amazingVariable == "2" and firstVariable == 2:
        print("There both the same value")

    elif amazingVariable == "1" and firstVariable == 1:
        print('There both different')

    # Multiple Variables
    colors = str("colors")

    rainbow, colors, light = 10, "beautiful", colors

    print(rainbow)

    print(colors)

    print(light)

    # List
    colors_Of_Rainbow = [
        "red", "green", "blue", "violet", "yellow", "blue", "orange", "indigo"
    ]

    a, b, c, d, e, f, g, h = colors_Of_Rainbow

    print(a)

    print(b)

    print(c)

    print(d)

    print(e)

    print(f)

    print(g)

    print(h)

    # Output statements
    xcode = str("Xcode")

    space = str(" and")

    python = str(" Python")

    space1 = str(" are")

    space2 = str(" equally")

    finishedSentence = str(" amazing")

    theWholeSentence = xcode + space + python + space1 + space2 + finishedSentence

    print(theWholeSentence)

    # Global Keyword
    def theGlobalKeyword():
        global o
        o = " but why"

    theGlobalKeyword()
    print("Nice Code" + o)

    # Value Types
    numberVariable = int(1011)

    numberVariable1 = int(1233)

    numberVariable2 = int(1343)

    print(numberVariable)

    print(numberVariable1)

    print(numberVariable2)

    print(type(numberVariable))

    print(type(numberVariable1))

    print(type(numberVariable2))

    floatvalueVariable = 2.323

    floatvalueVariable1 = -092.e33

    floatvalueVariable2 = -90.e87

    print(floatvalueVariable)

    print(floatvalueVariable1)

    print(floatvalueVariable2)

    print(type(floatvalueVariable))

    print(type(floatvalueVariable1))

    print(type(floatvalueVariable2))

    complexvar = 35j

    complexvar1 = 4 - 3j

    complexvar2 = 34 + 9j

    print(complexvar)

    print(complexvar1)

    print(complexvar2)

    # Changing the Variable Type
    change = float(numberVariable)

    change1 = int(floatvalueVariable)

    change2 = str(complexvar)

    print(change)

    print(change1)

    print(change2)

    # Strings
    theSentence = str(
        """ Hi my name is KoolAid or aka TheLastMemeBender. I'm a professional game developer and a professional gamer myself, I've played in the NGUOF(National Gamers Union of Florida) back in 2001, I've also recieved a medal for most professional player of all time (PPAT). After this I got an opportunity in the IGSFPG (International Gamers Society for Professionals and Gods), I proudly took it and won. So I've went to the NGUOF, IGSFPG,ISRGU (International Speed Runners Gaming Union), USCFST (Universal Science Con for Science and Technology), GC1984CR (Gamers Con 1984 campaign run, and finally GWRGC 2001 (Guinness World Record Gamers Con 2001)"""
    )

    print(theSentence)

    x = "Apple"
    c = "Orange"
    o = "Grapes"
    k = "Prunes"

    print(x[1])
    print(c[2])
    print(o[3])
    print(k[4])

    print(len(c))

    for b in "SuperMan":
        print(b)

    if "prunes" in theSentence:
        print("ummmm......DATA CRASHED")
    elif "grapes" in theSentence:
        print("not executable......SORRY")
    elif "orange" in theSentence:
        print("ummmmm.....STILL NOT EXECUTABLE")
    elif "apple" in theSentence:
        print("seriously TRY A DIFFERENT VALUE...")
    elif "USCFST" in theSentence:
        print("ok looks like you got it.......ACCESS CONFIRMED")

    # Using the "not in" keyword is basically the opposite of using the "in" keyword

    # Declaring Random number generator
    theRandoms = random.randint(0, 10)

    # Slicing Strings
    Hello_World = "Hello_World"
    print(Hello_World[-4:-2])

    print(theRandoms)

    # The Upper method

    world = "world"
    print(world.upper())

    # The lower Case method

    world1 = "URANUS"
    print(world1.lower())

    # The String method

    world2 = "  P H O B O S  "
    print(world2.strip())

    # The Replace method

    world3 = "Neptune"
    print(world3.replace("t", "T"))

    # The Split method

    world4 = "Eros, Nebula"
    print(world4.split(","))

    # Concatenating Strings

    a = "Mr."
    b = "Cheese"

    combined = a + b
    print(combined)

    # Formating Strings

    itemno = 37837

    itemname = "Socket wrench"

    dollar = 199.9

    mechanicOrder = " Could I have item #no {0} and also could I have the {1} for {2}? "

    print(mechanicOrder.format(itemno, itemname, dollar))

    # Escape Characters
    vikings = "Vikings"
    prt = "We are \"vikings\" from the future"
    print(prt.upper())

    # Booleans

    a = bool(100)

    b = bool(9000)

    c = bool(28322)

    if a > b:
        print("RICK ROLLED <1>")
    elif a > c:
        print("RICK GOT WRECKED <2>")
    elif c < a:
        print("RICK GOT WRECKED |3|")
    elif b > a < c:
        print("RICK ROLLED <4>")

    r = bool("peppa pog")

    i = bool(None)

    c = bool(1234512345679)

    k = bool(["orange", "purple", "magenta"])

    r = bool("")

    o = bool({})

    l = bool(())

    l = bool([])

    print(r, i, c, k, r, o, l, l)

    class classguy():
        def __len__(self):
            return 2

    myobj = classguy()
    print(bool(myobj))

    def myfunction1():
        return False

    print(myfunction1())

    if myfunction1():
        print(" YES! ")
    else:
        print(" NO! ")

    kfool = "RICK ROLLED"

    kfoo112 = print(isinstance(kfool, int))

    # Operators

    print(10 - 3 - 5 + 100 + 1000 * 3 * 3 / 2 * 1000000)

    # List

    sea_animals = ("crabs", "squids", "whales", "sharks", "hammerhead-shark",
                   "Angler Fish")

    animals = ["monkey", "giraffe", "elephant", "giraffe", "dogs", "parrot"]

    numbers = [1, 2, 3, 5, 6, 9]

    trueorFalse = [True, False, True, False]

    mixed = ["confusion", 99, "lol", 88, "studies"]

    print(len(animals))

    print(type(mixed))

    print(type(numbers))

    # Accessing Items in Lists

    print(trueorFalse[1])

    print(mixed[-1])

    print(animals[5])

    print(animals[0:6])

    print(animals[:4])

    print(animals[2:])

    # Replacing Values (Different Types)

    if "monkey" in animals:
        print("We have all the animals loaded in!")

    animals[3:4] = ["Donkey", "Rabbit"]

    print(animals)

    # Inserting Values (Different Ways)

    animals.insert(7, "pig")
    print(animals)

    animals.insert(8, "sheep")
    print(animals)

    # Appending Values

    animals.append("mules")

    print(animals)

    # Extending Values

    animals.extend(sea_animals)

    print(animals)

    # Removing Values (Different Ways)

    # Remove
    animals.remove("Donkey")

    print(animals)

    # Pop
    animals.pop(0)

    print(animals)

    # Pop v1
    animals.pop()

    print(animals)

    # Del (Delete)
    del animals[0]

    print(animals)
    # Or any other character in the list will be delete when you put that specific number

    temporaryList = ["Im", "About", "To Be", "Deleted and Yeeted"]
    del temporaryList

    # Clear (deletes content inside list but the list itself still remains)
    temporaryList1 = ["Im", "About", "To Be", "Deleted and Yeeted"]

    temporaryList1.clear()

    print(temporaryList1)

    if temporaryList1 == []:
        print("lUl\n")

    # Looping Through Lists (Different Ways)

    youtubers = [
        "Dream", "GeorgeNotFound", "Skeppy", "DanTDM", "ArlogProXD",
        "NithinDab", "PIXEL SONIC", "PewDiePie\n"
    ]

    # For In loop
    for minecrafters in youtubers:
        print(minecrafters)

    for keppy in range(len(youtubers)):
        print(youtubers[keppy])

    # While Loop
    i = 0
    while i < len(youtubers):
        print(youtubers[i])
        i = i + 1

    # Looping Using List Comprehension
    [print(minecrap) for minecrap in youtubers]

    # List Comprehension
    # Another Way: ebic = [v for v in youtubers if "e" in v]
    # And then.....print it; print(ebic)
    [print(v) for v in youtubers if "e" in v]

    # List Comprehension Syntax
    # newlist = [expression for item in iterable if condition == True]
    [print(k) for k in youtubers if k != "Skeppy"]

    cool = [cool for cool in youtubers if "e" in cool]
    print(cool)

    coolness = [b.upper() for b in youtubers]
    print(coolness)

    bells = ['yellow' for c in youtubers]
    print(bells)

    # bananas = "oranges"
    # fruits [vegetables if vegetables != "ban"]

    newlist = [q if q != "Skeppy" else "DanTDM" for q in youtubers]
    print(newlist)

    youtubers.sort()
    print(youtubers)

    def temporaryFunc(v):
        return (v - 2)

    thenumberGang = [100, 99, 88, 77, 1, 0]

    thenumberGang.sort(key=temporaryFunc)

    print(thenumberGang)

    bruhmoment = youtubers.copy()

    print(bruhmoment)

    combination = thenumberGang + youtubers

    print(combination)

    for m in thenumberGang:
        youtubers.append(m)

    print(youtubers)

    thistuple = ("PipthePantMan,")

    print(len(thistuple))

    print(type(thistuple))

    tuple1 = ("apple", "banana", "grape", "cherry")

    tuple2 = (1, 2, 4, 5, 6, 8)

    tuple3 = (True, False, True, False)

    tuple4 = ("abc", 43, True, "gender")

    tuple5 = tuple(("bruh", "moment"))

    print(tuple5)

    print(tuple1[0])

    print(tuple1[2])

    print(tuple1[-1])

    print(tuple2[0:3])

    if 1 in tuple2:
        print("Ok")

    convert = list(tuple1)

    convert.append("orange")

    convert.append("kiwi")

    convert.append("mangos")

    tuple1 = tuple(convert)

    print(tuple1)

    #Unpacking Tuples

    stuff = ("guitar", "piano", "violen", "keyboard")

    (green, blue, *noice) = stuff

    print(green, blue, noice)

    #Loop Tuples(different types)

    for count in stuff:
        print(count)

    for i in range(len(stuff)):
        print(stuff[i])

    v = 0
    while v < len(stuff):
        print(stuff[v])
        v = v + 1

    tuplex = tuple1 + tuple3
    t = tuple1 * 2
    print(tuplex)

    print(t)

    # Python Sets

    thisset = {"fortnite", "minecraft", "roblox", "among us", "hypixel"}
    print(thisset)

    print(len(thisset))

    set1 = {1, 2, 3, 4, 5, 6}

    set2 = {True, False}

    set3 = {"a", "b", "c", "d"}

    print(type(set3))

    thisset1 = set(("bruh", 1))
    print(thisset1)

    # Accessing Items through Loops

    for b in set3:
        print(b)

    # Checks if that value is in that set; ex. print ("orange" in fruits). It will print true or false
    print("a" in set3) 

    # Adding Set Items
    set3.add("e")
    print(set3)

    tropical_Islands = {"ManuLand", "JawaIsland", "Hawaii", "Honolulu", "O'ahu", "ManuLand", "JawaIsland"}
    thisset.update(tropical_Islands)
    print(thisset)

    # Removing Items from the Set

    tropical_Islands.remove("ManuLand")
    tropical_Islands.discard("JawaIsland")
    print(tropical_Islands)

    mmmm = tropical_Islands.pop()
    print(mmmm)

    thisset11 = {"dead", "dead", "dead", "dead"}

    del thisset11

    # Looping through sets
    for bruh in tropical_Islands:
      print(bruh)

    # Joining Sets
    # The union() method returns a new set with all items from both sets
    # The update() method inserts the items in set2 into set1:
    # The intersection_update() method will keep only the items that are present in both sets.
    x = {"apple", "google", "microsoft"}
    y = {"google", "microsoft", "apple"}

    x.intersection(y) # Result will be apple and microsoft
    # The intersection() method will return a NEW set, that only contains the items that are present in both sets.
    # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
    x1 = {"apple", "google", "microsoft"}
    y1 = {"google", "samsung", "apple"}

    x1.symmetric_difference_update(y1)
    print(x1) # results in everything except for apple
    # The symmetric_difference() method will return a NEW set, that contains only the elements that are NOT present in both sets.

    # Brief overview of Set Methods
    
    # add()	Adds an element to the set
    
    # clear()	Removes all the elements from the set
    
    # copy()	Returns a copy of the set
    
    # difference()	Returns a set containing the difference between two or more sets
    
    # difference_update()	Removes the items in this set that are also included in another, specified set
    
    # discard()	Remove the specified item
    
    # intersection()	Returns a set, that is the intersection of two other sets
    
    # intersection_update()	Removes the items in this set that are not present in other, specified set(s)
    
    # isdisjoint()	Returns whether two sets have a intersection or not
    
    # issubset()	Returns whether another set contains this set or not
    
    # issuperset()	Returns whether this set contains another set or not
    
    # pop()	Removes an element from the set
    
    # remove()	Removes the specified element
    
    # symmetric_difference()	Returns a set with the symmetric differences of two sets
    
    # symmetric_difference_update()	inserts the symmetric differences from this set and another
    
    # union()	Return a set containing the union of sets
    
    # update()	Update the set with the union of this set and others


    # Python Dictionaries
    carsMemes = {
      "meme1": "I am speed",
      "meme2": "I am fast",
      "meme3": "I don't know what to say anymore",
      "meme4": False,
      "meme5": False,
    }

    print(carsMemes["meme1"])
    x = carsMemes["meme2"]
    x9 = carsMemes.get("meme3")
    print(x)
    print(x9)

    # Getting all the KEYS
    memes = carsMemes.keys()

    print(memes) # before the change

    carsMemes["meme6"] = "rapGod"

    print(memes) # after the change

    # Getting all the VALUES
    memesXD = carsMemes.values()

    print(memesXD) # before the change

    carsMemes["meme4"] = "Jamal has joined the chat"

    print(memesXD) # after the change

    # The items() method will return each item in a dictionary, as tuples in a list.
    jamaml = carsMemes.items()
    print(jamaml)

    # To determine if a specified key is present in a dictionary use the in keyword
    
    spareDict = {
      "object1": "cars",
      "object2": "dress",
      "object3": "bandages",
      "object4": "toys",
      "object5": "shoes",
      "object6": "watches",
      "object7": "time machines"

    }

    # Changing in the Dictionary 
    spareDict["object1"] = 2020 
    # The update() method; used for both changing and add items into the Dictionary
    spareDict.update({"object3": 1663}) 

    # Remove items from dictionary

    # The pop() method removes the item with the specified key name
    # The popitem() method removes the last inserted item
    # The del keyword removes the item with the specified key name
    # The clear() method empties the dictionary

    # Looping through Dictionaries
    
    for x in spareDict: # Prints all key names one by one
      print(x)

    for x1 in spareDict: # Prints all values one by one
      print(spareDict[x1])

    for x2 in spareDict.keys():
      print(x2)
    
    for x3, x4 in spareDict.items():
      print(x3, x4)

    















