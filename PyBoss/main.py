import csv
import datetime



def stateabbrev (statename):
    statename_dict = {}
    statename_dict = {
        'Alabama':'AL',
        'Alaska':'AK',
        'Arizona':'AZ',
        'Arkansas':'AR',
        'Colorado':'CO',
        'California':'CA',
        'Connecticut':'CT',
        'Delaware':'DE',
        'Florida':'FL',
        'Georgia':'GA',
        'Hawaii':'HI',
        'Idaho':'ID',
        'Illinois':'IL',
        'Indiana':'IN',
        'Iowa':'IA',
        'Kansas':'KA',
        'Kentucky':'KY',
        'Louisiana':'LA',
        'Maine':'ME',
        'Maryland':'MD',
        'Massachusetts':'MA',
        'Michigan':'MI',
        'Minnesota':'MN',
        'Mississippi':'MS',
        'Missouri':'MO',
        'Montana':'MT',
        'Nebraska':'NE',
        'Nevada':'NV',
        'New Hampshire':'NH',
        'New Jersey':'NJ',
        'New Mexico':'NM',
        'New York':'NY',
        'North Carolina':'NC',
        'North Dakota':'ND',
        'Ohio':'OH',
        'Oklahoma':'OK',
        'Oregon':'OR',
        'Pennsylvania':'PA',
        'Rhode Island':'RI',
        'South Carolina':'SC',
        'South Dakota':'SD',
        'Tennessee':'TN',
        'Texas':'TX',
        'Utah':'UT',
        'Vermont':'VT',
        'Virginia':'VA',
        'Washington':'WA',
        'West Virginia':'WV',
        'Wisconsin':'WI',
        'Wyoming':'WY'
    }
    return str(statename_dict[statename])


new_employee_dict = []
name = []

with open("employee_data2.csv",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id = row['Emp ID']
        name = row['Name'].split()
        first_name = name[0]
        last_name = name[1]
        #print(name)
        dob_re_formatted = datetime.datetime.strptime(row["DOB"], '%Y-%m-%d').strftime('%d/%m/%Y')
        ssn = row["SSN"]
        ssn_last_4 = "***-**-"+ssn[-4:]
        #print(f'hide ssn is: {ssn_last_4}')
        state = stateabbrev(row["State"])
        #print(f'state is: {state}')
        new_employee_dict.append(
            {
                "Emp ID": row["Emp ID"],
                "First Name": first_name,
                "Last Name": last_name,
                "DOB": dob_re_formatted,
                "SSN": ssn_last_4,
                "State Abbrev": state
            }
        )
#print(new_employee_dict)

#write updated data to csv vile
with open("new_employee_data2.csv", "w") as csvfile:
    field_names = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State Abbrev"]
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(new_employee_dict)