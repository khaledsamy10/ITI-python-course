from email_validation import valid_username
from Data_test_samples import user_list


# Function to authenticate the user have the right password
def user_pass_auth():
    try:
        user_name=input('enter your username: ').strip()
        if valid_username(user_name):
            for i in range(len(user_list)):
                if user_list[i]['name']==user_name:
                    password=input('enter your password: ').strip()
                    if user_list[i]['pass']==password:
                        print('welcome')
                        break
                    else:
                        print('wrong password')
                        break
                else:
                    continue
            else:
                print('Not a user. please sign up')
        else:
            print('not valid username')
    except:
        print('error happened, try again')