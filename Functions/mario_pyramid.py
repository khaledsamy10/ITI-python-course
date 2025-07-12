# function to build mario pyramid of (x) number of layers
def simple_mario_pyramid(x):
    try:
        x=int(x)
        if x==0:
            print("can't build pyramid with 0 layers!")
        elif x<0:
            print("can't build pyramid with negative value layers")
        else:
            z=x-1
            spaces =' '*z
            astrixes='*'
            for i in range (1,x+1,1):
                print (spaces+astrixes)
                z=z-1
                spaces=' '*(z)
                astrixes=astrixes+'*'
    except:
        print('error occured, try again with positive intger number!')
        


# Function to build mario pyramid lists
def list_mario_pyramid(x):
    try:
        x=int(x)
        if x==0:
            print("can't build pyramid with 0 layers!")
        elif x<0:
            print("can't build pyramid with negative value layers")
        else:
            pyramid_list=[' ']*x
            for i in range(x):
                pyramid_list.remove(' ')
                pyramid_list.append('*')
                print(pyramid_list)
    except:
        print('error occured, try again with positive intger number!')