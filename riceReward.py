#a really basic script based on the legendary reward 
# also a way to demo exponential growth 
# and the bitwise operator, <<

squares = input("okay, so there are 64 square on a chess board, and 100 on a snakes and ladders board, \nso how many squares are there on the board you have?  ")

reward = f'{(1<<(int(squares))):,}'
print(reward)

if reward.count(',') == 1:
    print ("no way bro, that's thousands of grains!")
if reward.count(",") == 2:
    print ("no way bro, that's millions of grains!!")
if reward.count(",") == 3:
    print ("no way bro, that's billions of grains!!!")
if reward.count(",") == 4:
    print ("no way bro, that's trillions of grains!!!!")
if reward.count(",") == 5:
    print ("no way bro, that's quadrillions of grains!!!!!!")
if reward.count(",") == 6:
    print ("no way bro, that's quintillions of grains!!!!!!!")
if reward.count(",") == 7:
    print ("no way bro, that's sextillions of grains!!!!!!!!")
if reward.count(",") == 8:
    print ("no way bro, that's septtillions of grains!!!!!!!!!")  
if reward.count(",") == 9:
    print ("no way bro, that's octtillions of grains!!!!!!!!!!")   
if reward.count(",") == 10:
    print ("no way bro, that's nonillions of grains!!!!!!!!!!!")   


 

