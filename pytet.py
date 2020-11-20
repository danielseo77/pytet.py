from matrix import *
from random import *

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     
a1 = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]
a2 = [ [ 1, 1, 1, 1 ] ]
a3 = a1
a4 = a2

b1 = [ [ 0, 1, 1, 0 ], [ 0, 1, 1, 0 ] ]

c1 = [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]
c4 = [ [ 1, 1, 1, 0 ], [ 1, 0, 0, 0 ] ]
c3 = [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ] ]
c2 = [ [ 0, 0, 1, 0 ], [ 1, 1, 1, 0 ] ]

d1 = [ [ 0, 1, 1, 0 ], [ 0, 1, 0 ,0 ], [ 0, 1, 0, 0 ] ]
d4 = [ [ 1, 0, 0, 0 ], [ 1, 1, 1, 0 ] ]
d3 = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ] ]
d2 = [ [ 1, 1, 1, 0 ], [ 0, 0, 1, 0 ] ]

e1 = [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ] ]
e4 = [ [ 0, 1, 1, 0 ], [ 1, 1, 0, 0 ] ]
e3 = e1
e2 = e4

f1 = [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ] ]
f4 = [ [ 1, 1, 0, 0 ], [ 0, 1, 1, 0 ] ]
f3 = f1
f2 = f4

g1 = [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 1 ] ]
g4 = [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ] ]
g3 = [ [ 0, 1, 1, 1 ], [ 0, 0, 1, 0 ] ]
g2 = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ] ]


ran_num= randint(1,7)
if ran_num== 1:      
    arrayBlk= a1
elif ran_num == 2:     
    arrayBlk= b1
elif ran_num == 3:  
    arrayBlk= c1
elif ran_num == 4:  
    arrayBlk= d1
elif ran_num == 5:           
    arrayBlk= e1
elif ran_num == 6:            
    arrayBlk= f1
elif ran_num == 7:
    arrayBlk= g1
        
        

def drop():
    global top
    while True:

        print()
        top += 1
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            break;

def rotateBlk() :
    global arrayBlk
    global currBlk
    global tempBlk
    if arrayBlk == a1:
        arrayBlk = a2
    elif arrayBlk == a2:
        arrayBlk = a3
    elif arrayBlk == a3:
        arrayBlk = a4
    elif arrayBlk == a4:
        arrayBlk = a1
    elif arrayBlk == b1:
        arrayBlk = b1
    elif arrayBlk == c1:
        arrayBlk = c2
    elif arrayBlk == c2:
        arrayBlk = c3
    elif arrayBlk == c3:
        arrayBlk = c4
    elif arrayBlk == c4:
        arrayBlk = c1
    elif arrayBlk == d1:
        arrayBlk = d2
    elif arrayBlk == d2:
        arrayBlk = d3
    elif arrayBlk == d3:
        arrayBlk = d4
    elif arrayBlk == d4:
        arrayBlk = d1
    elif arrayBlk == e1:
        arrayBlk = e2
    elif arrayBlk == e2:
        arrayBlk = e3
    elif arrayBlk == e3:
        arrayBlk = e4
    elif arrayBlk == e4:
        arrayBlk = e1
    elif arrayBlk == f1:
        arrayBlk = f2
    elif arrayBlk == f2:
        arrayBlk = f3
    elif arrayBlk == f3:
        arrayBlk = f4
    elif arrayBlk == f4:
        arrayBlk = f1
    elif arrayBlk == g1:
        arrayBlk = g2
    elif arrayBlk == g2:
        arrayBlk = g3
    elif arrayBlk == g3:
        arrayBlk = g4
    elif arrayBlk == g4:
        arrayBlk = g1

    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    print(arrayBlk)
    print(currBlk)

def counter_rotateBlk():
    global arrayBlk
    if arrayBlk == a1:
        arrayBlk = a4
    elif arrayBlk == a4:
        arrayBlk = a3
    elif arrayBlk == a3:
        arrayBlk = a2
    elif arrayBlk == a2:
        arrayBlk = a1
    elif arrayBlk == b1:
        arrayBlk = b4
    elif arrayBlk == b4:
        arrayBlk = b3
    elif arrayBlk == b3:
        arrayBlk = b2
    elif arrayBlk == b2:
        arrayBlk = b1
    elif arrayBlk == c1:
        arrayBlk = c4
    elif arrayBlk == c4:
        arrayBlk = c3
    elif arrayBlk == c3:
        arrayBlk = c2
    elif arrayBlk == c2:
        arrayBlk = c1
    elif arrayBlk == d1:
        arrayBlk = d4
    elif arrayBlk == d4:
        arrayBlk = d3
    elif arrayBlk == d3:
        arrayBlk = d2
    elif arrayBlk == d2:
        arrayBlk = d1
    elif arrayBlk == e1:
        arrayBlk = e4
    elif arrayBlk == e4:
        arrayBlk = e3
    elif arrayBlk == e3:
        arrayBlk = e2
    elif arrayBlk == e2:
        arrayBlk = e1
    elif arrayBlk == f1:
        arrayBlk = f4
    elif arrayBlk == f4:
        arrayBlk = f3
    elif arrayBlk == f3:
        arrayBlk = f2
    elif arrayBlk == f2:
        arrayBlk = f1
    elif arrayBlk == g1:
        arrayBlk = g4
    elif arrayBlk == g4:
        arrayBlk = g3
    elif arrayBlk == g3:
        arrayBlk = g2
    elif arrayBlk == g2:
        arrayBlk = g1
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    
### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
print(arrayBlk)
print(currBlk)
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        rotateBlk()
    elif key == ' ': # drop the block
        drop()
        
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    

    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            counter_rotateBlk()
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        ran_num= randint(1,7)
        if ran_num== 1:      
            arrayBlk= a1
        elif ran_num == 2:     
            arrayBlk= b1
        elif ran_num == 3:  
            arrayBlk= c1
        elif ran_num == 4:  
            arrayBlk= d1
        elif ran_num == 5:           
            arrayBlk= e1
        elif ran_num == 6:            
            arrayBlk= f1
        elif ran_num == 7:
            arrayBlk= g1
        
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
