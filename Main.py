# %%
import numpy as np
import random

# %%
n =  input('Number Of Rooms: ')
l = input('Length Of House: ')
w = input('Width Of House: ')
p = input('People In The House: ')

# %%
def basic_room(l,w):

    #variables (oof this is gonna be a pain)
    v_window = '='
    v_brick = '|'
    h_brick = '-'
    h_window = '<>'
    v_door = '^'
    h_door = '<'
    door_position = random.randrange(1, l-1)
    h_window_position = random.randint(0, l-1)
    v_window_position = random.randrange(1, w-1)
    room=[]
    h_wall = [h_brick] * l
    h_final_wall = [h_brick] * l
    onwmiusone = random.choice([0,-1])

    #door generation
    h_wall[door_position] = h_door

    #room generation
    room.append(h_wall)
    for i in range(w-2):
        room.append([v_brick] + [' '] * (l-2) + [v_brick])
    room.append(h_final_wall)


    #window generation 
    # print(room)
    print(onwmiusone)
    room[v_window_position][onwmiusone]=v_window
    
    #final wall generation
    v_wall = [v_brick, ' ' * (len(h_wall)-2), v_brick]

    print(np.array(room))

basic_room(11,13)


