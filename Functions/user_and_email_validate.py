from email_validation import valid_email,valid_username

def user_email_validate():    
    for i in range(5):
        try:
            username=input('enter your username: ').strip()
            if valid_username(username):
                print('username confirmed')
                break
            else:
                print('unvalid username, try again')
        except:
            print('unvalid username, try again')
    else:
        raise ValueError
            
    for i in range (5):
        try:
            email=input('enter your email: ').strip()
            if valid_email(email):   
                print('email confirmed')
                break
            else:
                print('unvalid email, try again')
        except:
            print('unvalid email, try again')
    else:
        raise ValueError
            
    print(f'the username is: {username}')
    print(f'the email is: {email}')