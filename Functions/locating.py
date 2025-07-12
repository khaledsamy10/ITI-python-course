# Function to locate specific character in string 
def locating_character(string_value,character):
    try :
        string_value=str(string_value)
        character=str(character)
        for i in range (len(string_value)):
            if character not in string_value:
                print(f'there is no {character} in {string_value}!')
                break
            elif string_value[i]==character:
                print(f'There is {character} character in index {i}')       
    except:
        print ('make sure you enter string value!')