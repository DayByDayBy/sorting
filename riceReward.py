squares = input("okay, so there are 64 square on a chess board, and 100 on a snakes and ladders board, so how many squares are there on the board you have?  ")

reward = f'{(1<<(int(squares))):,}'
print(reward)

if reward.count(',') == 1:
    print ("bro, that's thousands of grains!")
if reward.count(",") == 2:
    print ("bro, that's millions of grains!!")
if reward.count(",") == 3:
    print ("bro, that's billions of grains!!!")
if reward.count(",") == 4:
    print ("bro, that's trillions of grains!!!!")
if reward.count(",") == 5:
    print ("bro, that's quadrillions of grains!!!!!!")
if reward.count(",") == 6:
    print ("bro, that's quintillions of grains!!!!!!!")
if reward.count(",") == 7:
    print ("bro, that's sextillions of grains!!!!!!!!")
if reward.count(",") == 8:
    print ("bro, that's septtillions of grains!!!!!!!!!")  
if reward.count(",") == 9:
    print ("bro, that's octtillions of grains!!!!!!!!!!")   
if reward.count(",") == 10:
    print ("bro, that's nonillions of grains!!!!!!!!!!!")    

