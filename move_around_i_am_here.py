# pip install pyautogui
# pip install keyboard


import pyautogui
import time
import argparse
import sys

def move_mouse(duration):
    # Set the failsafe to stop script when move mouse in the top-left corner
    pyautogui.FAILSAFE = True

    # Get the start time
    start_time = time.time()

    while time.time() - start_time < duration:
    
        # Move the mouse to the position (x=100, y=200) on your screen
        pyautogui.moveTo(-1650, 200)
        pyautogui.click()

        # Wait for 1 second
        time.sleep(1)

        # Move the mouse by an offset from its current position
        # This will move the mouse 50 pixels to the right and 30 pixels down
        pyautogui.move(0, 150)
        pyautogui.click()

        # Wait for 1 second
        time.sleep(1)

         # Calculate remaining time and print it
        remaining_time = duration - (time.time() - start_time)
        print(f'\rRemaining time: {remaining_time:.2f} seconds', end='')
        sys.stdout.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Move the mouse for a specific duration.')
    parser.add_argument('duration', type=int, help='The duration in seconds for which the mouse should be moved.')

    args = parser.parse_args()

    move_mouse(args.duration)
