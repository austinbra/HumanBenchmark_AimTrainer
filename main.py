
import pyautogui
import time

def checkColor(x, y):
    #finds the rgb values at the coordinate
    pixel_color = pyautogui.pixel(x, y)
    if pixel_color == (149,195,232):
        pyautogui.click(x,y)
        return True
    return False

def grid(rows, cols, col_step_size, row_step_size):
    screen_width, screen_height = pyautogui.size()
    for row in range(4, rows - 4):
        for col in range(1, cols - 1):
            x = col * col_step_size
            y = row * row_step_size
            checkColor(int(x),int(y))
            pyautogui.moveTo(x, y)

pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0
# Define grid parameters
grid_rows = 20
grid_cols = 25
col_step_size = float(pyautogui.size()[0]) / grid_cols  # Adjust this based on your preference
row_step_size = float(pyautogui.size()[1]) / grid_cols
# Call the function to move the mouse in a grid pattern
start = time.time()
end = start + 30
while time.time() < end:
    grid(grid_rows, grid_cols, col_step_size, row_step_size)


