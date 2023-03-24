squares = input('okay, so how many squares are there on a chessboard? ')

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
    print ("bro, that's quintillions of grains!!!!!!")

