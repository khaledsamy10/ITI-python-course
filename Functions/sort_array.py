# Function take unlimited intgers and print it sorted ascendingly and descendingly.
def sort_array(*x):
    try:
        x=list(x)
        array_list=[]
        for i in range (len(x)):
            x[i]=int(x[i])
            array_list.append(x[i])
        asc_sort=sorted(array_list)
        desc_sort=sorted(array_list,reverse=True)
        
        print(f'The array in ascending order is: {asc_sort}')
        print(f'The array in descending order is: {desc_sort}')
    except:
        print('only integer values allowed')