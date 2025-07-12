# Function to show multiplication table for every number up to (x)
def multiplication_table(x):
    try:
        x=int(x) 
        if x<=0:
            print(f'there is no multiplication table for {x}')
        else:
            for n in range (1,x+1,1):
                for j in range (1,n+1,1):
                    print(f'{n}*{j}={n*j}')
    except:
        print('make sure you enter an integer')
        


# Function to show multiplication table results for every number up to (x) in the form of list of lists
def multiplication_table_in_lists(x):
    try:
        x=int(x)
        if x<=0:
            print(f'there is no multiplication table for {x}')
        else:
            y=[]
            for n in range (1,x+1,1):
                z=[]
                for j in range (1,n+1,1):
                    z.append(n*j)
                y.append(z)
            print(y)    
    except:
        print('error, try again with intger value')