import pyautogui
from time import sleep
from PIL import ImageGrab

def is_green(pixel_color):
    # Adjust the threshold for green detection
    r, g, b = pixel_color
    # Checking if green is dominant and red/blue are significantly lower
    return g > 120 and r < 100 and b < 100

def find_green_area(x1, y1, x2, y2):
    # Capture a screenshot of the specified area
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    width, height = screen.size
    print(f"Checking area: ({x1},{y1}) to ({x2},{y2})")

    for x in range(width):
        for y in range(height):
            # Get the color of the pixel
            pixel = screen.getpixel((x, y))
            print(f"Pixel at ({x}, {y}): {pixel}")  # Print the pixel color for debugging
            if is_green(pixel):
                print("Green detected!")
                return True  # Found green
    print("Green not detected.")
    return False

def click_if_green(x, y, width, height):
    while True:
        # Continuously capture the specified area until green is detected
        if find_green_area(x, y, x + width, y + height):
            # Click the center of the area once it turns green
            pyautogui.click(x + width // 2, y + height // 2)
            print("Clicked the green area!")
            break
        else:
            print("No green detected, retrying...")
        # sleep(0.01)  # Short sleep to make it more responsive (adjust if needed)

if __name__ == "__main__":
    # Coordinates of the red/green area on your screen
    # Adjust these values to the location of the red/green box
    x = 800  # Top-left x-coordinate
    y = 500  # Top-left y-coordinate
    width = 1  # Width of the area (small 10x10 area as you mentioned)
    height = 1  # Height of the area

    print("Waiting for the color to turn green...")
    click_if_green(x, y, width, height)
    print("Finished.")
