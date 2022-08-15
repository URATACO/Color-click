import pyautogui as pyg

# take mouse position and color
print('press enter in terminal whenhovering over wanted pixel color')
temp = input()
mouse_pos = pyg.position()
mouse_pos_color_rgb = pyg.pixel()
mpc = mouse_pos_color_rgb
# checks for color and click
while True:
    if pyg.pixelMatchesColor(mouse_pos[0], mouse_pos[1],(mpc[0],mpc[1],mpc[2])):
        pyg.click(mouse_pos)
        
    #if position changes listener 'p' will allow you to change it
    #will add soon
