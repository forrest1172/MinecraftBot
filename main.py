import pyautogui as pt
from time import sleep


blocksMoved = 0

#move cursor to center of the image of "back to game" button if found with coonfidence of 50%
def nav_to_image(image,clicks,off_x=0,off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.5)

    if position is None:
        print(f'{image} not found')
        return 0
    else:
        print("image of back to game found!")
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x,off_y,duration=0.1)
        pt.click(clicks=clicks, interval=0.3)

#move character
def move_character(key_press, Duration, action="walking"):
    pt.keyDown(key_press)

    if action == "walking":
        print("walking")
    elif action == "attack":
        pt.mouseDown(duration=3500)
        print("Mining")
    sleep(Duration)
    pt.mouseUp()
    pt.keyUp(key_press)

def locate_lava():
    position1 = pt.locateCenterOnScreen('images/lava.png', confidence=0.6, grayscale=False)
    position2 = pt.locateCenterOnScreen('images/lava_1.png', confidence=0.5, grayscale=False)
    if position1 is None:
        return False
    elif position2 is None:
        return False
    else:
        move_character('s', 3, "walking")
        print("found lava!")
        return True

def CheckPick(walkBack):
    pos = pt.locateOnScreen("images/empty_slot.png", confidence=0.7, grayscale=False)
    if pos is None:
        return False
    else:
        print("Pickaxe broke or ran out of torches!")
        move_character('s', walkBack / 4.317)
        return True

def start(numOfBlocks):
    print("Number of blocks traveled: " + str(numOfBlocks))
    nav_to_image("images/start_game.png", 1)
    pt.keyDown("1")
    duration = 5
    while duration != 0:
        if not CheckPick(numOfBlocks):
            print("Pick OK")
        else:
            break
        if not locate_lava():
            move_character("w", 3, "attack")
        else:
            break
        duration -= 1
        print("Time remaining: " + str(duration))
    print("Placing torch!")
    PlaceTorch()
1
def PlaceTorch():
    global blocksMoved
    mousePos = pt.position()
    print(mousePos)
    pt.moveTo(200, mousePos.y, duration=0.2)
    sleep(0.3)
    pt.keyDown("9")
    pt.rightClick()
    pt.moveTo(-200, mousePos.y, duration=0.3575)
    pt.keyDown("1")
    blocksMoved += 5
    start(blocksMoved)

#start program

sleep(1)
print("starting in 3...")
sleep(1)
print("starting in 2..")
sleep(1)
print("starting in 1!")
start(0)