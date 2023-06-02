# arcade -type game
from tkinter import Tk, Canvas, messagebox, font
import random
from itertools import cycle

canvas_width = 800
canvas_height = 400

root = Tk() # creates the tkinter window
c = Canvas(root, width = canvas_width, height = canvas_height, background = 'deep sky blue') # create the canvas
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5 ,canvas_height + 5, fill = 'sea green' ,width = 0)
c.create_oval(-80, -80, 120, 120, fill = 'orange' , width = 0)
c.pack() #The pack() function tells the program to draw the main window and all of its contents.

# set up egg
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
egg_width = 45
egg_height = 55
egg_score = 10               # u score 10 points for catching an egg
egg_speed = 500 # 
egg_interval = 4000          # A new egg appears every 4,000 milliseconds (4 seconds).
difficulty_factor = 0.95 # This is how much the speed and interval change after each catch (closer to 1 is easier).

# set-up catcher
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100        #This is the height of the circle that is used to draw the arc.
#These lines make the catcher start near the bottom of the canvas, in the center of the window
canvas_start_x = canvas_width / 2 - catcher_width / 2  
canvas_start_y = canvas_height - catcher_height - 20
canvas_start_x2 = canvas_start_x + catcher_width
canvas_start_y2 = canvas_start_y + catcher_height
# creating the catcher. here arc is drawn starting at angle 200 and then is extended to 140.
# first two arg is coordinate for point 1 of imaginary box inside which arc resides and other two is opposite corner coordinate
# start says where to start drawing and extent is how many degrees to draw before stopping
catcher = c.create_arc(canvas_start_x, canvas_start_y, canvas_start_x2, canvas_start_y2,start = 200, extent = 140, style = 'arc', outline = catcher_color, width = 3)

game_font = font.nametofont('TkFixedFont')  # this line selects a computer style font
game_font.config(size = 18)

score  = 0
score_text = c.create_text(10, 10, anchor = 'nw', font = game_font, fill = 'darkblue', text = f'Score: {score}')

lives_remaining  = 3  # player gets three lives
lives_text = c.create_text(canvas_width -10, 10, anchor = 'ne', font = game_font, fill = 'darkblue', text = f'Lives: {lives_remaining}')

eggs = [] # list to keep all eggs
def create_egg():
    x = random.randrange(10 ,740)          #Pick a random position along the top of the canvas for the new egg.
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill = next(color_cycle), width = 0)  # draws the egg
    eggs.append(new_egg)  # the shape is added to the list
    root.after(egg_interval, create_egg) # this calls the create_egg after the interval specified in egg_interval    
    
def move_eggs():
    for egg in eggs: # loops through all eggs
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)  # this line gets coordinate of each egg
        c.move(egg, 0 ,10)  # the egg drop down the screen 10 pixels at a time.
        if egg_y2 > canvas_height: # is the egg at the bottom of the screen ?
            egg_dropped(egg)    # if so call the function that deals with dropped eggs
    root.after(egg_speed, move_eggs)    # call this func again after the milliseconds stored in egg_speed
        
def egg_dropped(egg):
    eggs.remove(egg)  # the egg is removed from the egg list
    c.delete(egg)   # the egg disappears from the canvas
    lose_a_life()   # this line calls the lose_a_life function
    
    if lives_remaining == 0:
        messagebox.showinfo('GAME OVER!' , f'Final Score: {score}')
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1 # the player looses a life
    c.itemconfigure(lives_text, text = f'Lives: {lives_remaining}')

def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)  # get the coordinate of the catcher
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)  # this line gets coordinate of each egg
        # is the egg inside the catcher horizontally or vertically ?
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)  # remove egg from the list
            c.delete(egg) # delete the egg from the canvas
            increase_score(egg_score) # increase the score by 10 points
    root.after(100, check_catch) # call this func again after 100 milliseconds
        
def increase_score(points):        
    global score, egg_speed, egg_interval
    score += points  # add to player's score
    egg_speed = int(egg_speed * difficulty_factor) # increase the speed of egg dropping by difficulty_factor 
    egg_interval = int(egg_interval * difficulty_factor)  # change the egg_interval of creating egg by difficulty_factor
    c.itemconfigure(score_text, text = f'Score: {score}')      # modifies the the score_text var of canvas


#The move_left() and move_right() functions use the coordinates of the catcher to make sure it isn’t about to leave the screen. If there’s still space
#to move to, the catcher shifts horizontally by 20 pixels. These two functions are linked to the left and right arrow keys on the keyboard using the bind()
#function. The focus_set() function allows the program to detect the key presses.

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    # has the catcher reached the wall?
    if x1 > 0:
        c.move(catcher, -20, 0) # if not then move the catcher to the left
        
def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    # has the catcher reached the right wall?
    if x2 < canvas_width:
        c.move(catcher, 20, 0) # if not then move the catcher to right by 20 pixels

# this line calls the functions when the keys are pressed
c.bind('<Left>',move_left)
c.bind('<Right>',move_right)
# this listens to the key presses and tells the canvas 
c.focus_set()

# the three game loops begin after the slight pause of 1 sec
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)

root.mainloop() # the mainloop () function starts the Tkinter loop that manages all your loops and timers

