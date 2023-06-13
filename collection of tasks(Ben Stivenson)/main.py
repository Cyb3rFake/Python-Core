

"""Part 4.Functions.Tasks """

def drawbox(x,y):

    print(' '+x*'_')
    print(*['H'+' ' * x + 'H' for i in range(y)], sep='\n')
    print(' ' + x * '_')

drawbox(7,5)