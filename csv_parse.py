import csv

def combine_csv():
    masterlist = 'c:/users/E/Desktop/key.csv'         # hard coded the file paths cause lazy
    testdata = 'c:/users/E/Desktop/test.csv'
    with open(testdata, 'r') as users:                 # open test data with users list and pk1 of role
        usersDict = csv.DictReader(users)                # csv dict reader makes each row a dict object
        for line in usersDict:                            # loop through users and pull the permissions value
            userRole = line['permission']                # this actually saves the pk1 from users by calling the key
            with open(masterlist) as master:               # opening the role master with pk1 and description
                role_master = csv.DictReader(master)       # making our dict object
                for mline in role_master:                  # move through master list comparing role pk1 to user pk1
                    if  mline['pk1'] != userRole:         # if the don't match just keep trucking
                        pass
                    else:                                # if they do match create a new dict object adding the
                        new_line = line                  # description from the master
                        new_line['Role Name'] = mline['description']
                        with open('c:/users/E/Desktop/new_file.csv', 'a+') as new_file:  # Create new file
                            fieldnames = ['firstname', 'lastname', 'permission', 'Role Name'] # define headers
                            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',') # define writer
                            csv_writer.writerow(new_line)   # write the new line. 


combine_csv()