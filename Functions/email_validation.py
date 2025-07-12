from Data_test_samples import emails

# Function to check email validation
def valid_email(email):
    if '@' in email and '.' in email:
        if email[0] not in ['@','.'] and email[-1] not in ['@','.']:
            if '.' not in email.split('@')[0] and email.split('@')[1][0]!='.':
                return True
            else :
                return False
        else : 
            return False
    else:
        return False


# Function to filter list of emails based on its validation
def filtering_emails(list_of_emails):  
    return list(filter(valid_email,list_of_emails))

# Function to validate username
def valid_username(username):
   if username !='' and len(username)>1 and not username.isdigit():
       return True
   else:
       return False