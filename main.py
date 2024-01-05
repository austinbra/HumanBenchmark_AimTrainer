import pyautogui
import time

target = (149, 195, 232)
ops = (43, 135, 209)
yel = (255,209,84)
screenshot = None

def checkColor(x, y):
    global screenshot
    if screenshot is None:
        screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))
    if pixel_color != ops and pixel_color != yel:
        screenshot = None  # Reset the screenshot after click
        return True
    return False

def grid(rows, cols, col_step_size, row_step_size):
    for row in range(5, rows + 4):
        for col in range(6, cols - 9):
            x = col * col_step_size
            y = row * row_step_size
            if checkColor(int(x), int(y)):
                pyautogui.click(x, y)
                return True
    return False

pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0

# Define grid parameters
screen_width, screen_height = pyautogui.size()
grid_rows = 10
grid_cols = 35
col_step_size = 100  # Adjust this based on your preference
row_step_size = 100

# Calls the function to click on the blue pixel of the target
start = time.time()
end = start + 5
print('Code is Running')
pyautogui.click(screen_width/2, (screen_height*3)/7)
while time.time() < end:
    grid(grid_rows, grid_cols, col_step_size, row_step_size)
print('Stopped')