import csv
import pandas as pd
from extract_domain import extract_domains

#                                            Two different functions doing the same job

# Function reads csv file and extract,filter and make unique of domains in email column using csv module.
# it takes two variables the csv file name and the email column number in the file.

def extract_domain_from_csv(csv_file_name,email_column_number):
    try:
        open_csvfile=open(csv_file_name,'r',newline='')
        file_reader=csv.reader(open_csvfile)
        listed_data=list(file_reader)
        
        emails_list=[]
        for i in range(1,len(listed_data)):
            emails_list.append(listed_data[i][email_column_number])
            

        domains=extract_domains(emails_list)
        return set(domains)
    except:
        print('error')


domains_set=extract_domain_from_csv('employees_data2.csv',4)
print(domains_set)


# Function reads csv file and extract,filter and make unique of domains in email column using pandas module.
# it takes two variables the csv file name and the email column name in the file.

def extract_domain_from_csv(csv_file_name,email_column_name):
    try:
        open_csvfile=open(str(csv_file_name),'r')
        data_as_pandas_dataframe=pd.read_csv(open_csvfile)

        emails_list=[]
        for i in data_as_pandas_dataframe[str(email_column_name)]:
            emails_list.append(i)

        domains=extract_domains(emails_list)
        return set(domains)
    except:
        print('error')


domains_set=extract_domain_from_csv('employees_data2.csv','Email')
print(domains_set)