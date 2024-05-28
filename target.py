from microbit import *
from random import choice

# Target shooting game. A target pixel will show across the top and the
# player will be positioned along the bottom. Use the A button to move the
# player position to the right (wrapping around to the left) and use the
# B button to fire!

score = 0        # starting score
max_time = 5000  # max time to hit target (milliseconds)
interval = 50    # time between polling buttons

def play():
    # The game starts with a target in a random
    # position along the top and the player's player
    # in the middle.
    target = choice(range(5))  # target 0..4
    player = 2                 # middle

    # Create a blank image and set the target and player positions
    img = Image()  # start with blank
    img.set_pixel(target, 0, 9)  # set target pixel
    img.set_pixel(player, 4, 9)  # set player pixel
    display.show(img)
    
    # Loop and poll buttons for player movement/fire
    for t in range(interval):
        if button_b.was_pressed():
            # Fire!
            img.set_pixel(player, 3, 9)
            display.show(img)
            sleep(50)
            img.set_pixel(player, 3, 5)
            img.set_pixel(player, 2, 9)
            display.show(img)
            sleep(50)
            img.set_pixel(player, 3, 0)
            img.set_pixel(player, 2, 5)
            img.set_pixel(player, 1, 9)
            display.show(img)
            sleep(50)
            img.set_pixel(player, 2, 0)
            img.set_pixel(player, 1, 5)
            img.set_pixel(player, 0, 9)
            display.show(img)
            sleep(250)

            # Return True/False if player hit the target
            return (player == target)
         
        if button_a.was_pressed():
            # Move position
            img.set_pixel(player, 4, 0)  # clear old position
            player = (player + 1) % 5
            img.set_pixel(player, 4, 9)  # set new player pixel
            display.show(img)

        # Sleep until the next poll time
        sleep(max_time // interval)

    # If the player hasn't hit the target by now, they lose this round
    return False
   

while True:
    if play():
        score = score + 1
        display.show(Image.HAPPY)
    else:
        score = max(score - 1, 0)
        display.show(Image.SAD)

    sleep(250)
    display.scroll("score")
    display.show(score)
    sleep(1000)
