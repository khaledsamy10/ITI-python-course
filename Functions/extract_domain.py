from email_validation import emails,filtering_emails

# Function to extraxt domains from email list (and filter them first so we only extract domains from valid emails)
def extract_domains(email_list):
    filtered_emails=filtering_emails(email_list)
    domains= list(map(lambda email:email.split('@')[1],filtered_emails))
    return domains