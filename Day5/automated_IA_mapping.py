import cv2
import numpy as np
import pyautogui

# Load the screenshot into OpenCV
img = cv2.imread('/Users/giovanni/Desktop/Python_bootcamp/Day5/screenshot.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Grays {gray}")

# Threshold the image to highlight the items you want to map
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find the contours of the items
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



# Loop over the contours and get the bounding boxes
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # Store the coordinates of the items in variables
    button_x, button_y = x + w // 2, y + h // 2
    
    

# Use pyautogui to interact with the items on the web page
pyautogui.click(591, 461)
pyautogui.click(591, 461)
pyautogui.click(591, 461)
pyautogui.doubleClick(591,461)

#pyautogui.displayMousePosition(button_x,button_y)

# Validate the results of your automated tests
#assert some_condition, 'Test failed'
