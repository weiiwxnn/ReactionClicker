import pyautogui
from time import sleep
import mss
import numpy as np

def is_green(pixel_color):
    # Adjust the threshold for green detection
    r, g, b = pixel_color
    # Checking if green is dominant and red/blue are significantly lower
    return g > 120 and r < 100 and b < 100

def find_green_area(x, y):
    with mss.mss() as sct:
        # Define the area to capture (1x1 pixel area)
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        screenshot = sct.grab(monitor)
        
        # Convert the pixel to RGB
        pixel = np.array(screenshot.pixel(0, 0))
        r, g, b = pixel[2], pixel[1], pixel[0]  # BGR to RGB
        
        # print(f"Pixel at (0, 0): ({r}, {g}, {b})")  # Print for debugging
        
        # Check if the pixel is green
        if is_green((r, g, b)):
            print("Green detected!")
            return True
        print("Green not detected.")
        return False

def click_if_green(x, y):
    while True:
        # Continuously capture the specified area until green is detected
        if find_green_area(x, y):
            # Click the center of the area once it turns green
            pyautogui.click(x, y)
            print("Clicked the green area!")
            break
        # Removing sleep for maximum speed

if __name__ == "__main__":
    # Coordinates of the red/green area on your screen
    x = 800  # Top-left x-coordinate
    y = 500  # Top-left y-coordinate

    print("Waiting for the color to turn green...")
    click_if_green(x, y)
    print("Finished.")
