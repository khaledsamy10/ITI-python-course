# Function to count number of vowels in string
def count_vowels(string_value):   
    try:
        string_value=str(string_value)
        vowels ='aeoui'
        v_count=0
        for c in string_value:
            if c in vowels:
                v_count+=1
            else:
                continue
        print(f'Number of vowels in {string_value} is {v_count}')  
    except:
        print('make sure you enter string')