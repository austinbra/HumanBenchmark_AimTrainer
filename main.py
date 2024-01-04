import pyautogui
import time

target = (149, 195, 232)
screenshot = None

def checkColor(x, y):
    global screenshot
    if screenshot is None:
        screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))

    if pixel_color == target:
        pyautogui.click(x, y)
        screenshot = None  # Reset the screenshot after click
        return True
    return False

def grid(rows, cols, col_step_size, row_step_size):
    screen_width, screen_height = pyautogui.size()
    for row in range(6, rows + 3):
        for col in range(5, cols - 8):
            x = col * col_step_size
            y = row * row_step_size
            checkColor(int(x), int(y))
            pyautogui.moveTo(x, y)

pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0

# Define grid parameters
grid_rows = 10
grid_cols = 30
col_step_size = 100  # Adjust this based on your preference
row_step_size = 100

# Call the function to move the mouse in a grid pattern
start = time.time()
end = start + 15
while time.time() < end:
    grid(grid_rows, grid_cols, col_step_size, row_step_size)
