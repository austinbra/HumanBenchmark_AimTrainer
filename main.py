import pyautogui
import time
import threading

top_x_val = 700      #Adjust this if you have a different resolution
top_y_val = 500      #Adjust this if you have a different resolution
bottom_x_val = 2500  #Adjust this if you have a different resolution
bottom_y_val = 1400  #Adjust this if you have a different resolution

#incorrect colors and target
target = (149, 195, 232)
ops = (43, 135, 209)
yel = (255,209,84)
screenshot = None
pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0
screen_width, screen_height = pyautogui.size()

# sets a timer
start = time.time()
end = start + 5
count = 0
print('Code is Running')




def checkColor(x, y, screenshot):
    #check the color of the current pixel
    pixel_color = screenshot.getpixel((x, y))
    if pixel_color != ops and pixel_color != yel:
        return True
    return False

def grid(top_x_val, top_y_val, bottom_x_val, bottom_y_val, screenshot, prev):
    #runs a check on all availible spots where the circle could be
    for y in range(top_y_val, bottom_y_val, 50):
        for x in range(top_x_val, bottom_x_val, 50):
            if checkColor(int(x), int(y), screenshot):
                return(x, y)
    return prev



#initial click and loops for 5 seconds until test is over
screenshot = pyautogui.screenshot()
prev = (screen_width/2, (screen_height*3)/7)
x, y = prev

pyautogui.click(screen_width/2, (screen_height*3)/7)
while time.time() < end:
    screenshot = pyautogui.screenshot()
    x, y = grid(top_x_val, top_y_val, bottom_x_val, bottom_y_val, screenshot, prev)
    pyautogui.click(x, y)
print('Stopped')