import csv


def combine_csv():
    with open('c:/csv2/new_file2.csv', 'ab+') as new_file:  # Create new file for results (output file)
        fieldnames = ['course_role', 'entitlement_uid', 'pk1']  # define headers in output file
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')  # define writer options
        csv_writer.writeheader()  # write the headers to your output file. done outside of loop on purpose.
    testdata = 'c:/csv2/test_env.csv'  # file 1
    clientdata = 'c:/csv2/client_env.csv' # file 2
    with open(testdata, 'r') as testenv:  # open test data with users list and pk1 of role
        testDict = csv.DictReader(testenv)  # csv dict reader makes each row a dict object
        test_env = []
        for line in testDict:  # loop through file 1 and pull a column of data
            test_env.append(line['entitlement_uid'])  # create a list of values from file 1
        with open(clientdata) as clientenv:  # open file 2
            clientDict = csv.DictReader(clientenv)  # making our dict object for file 2
            for mline in clientDict:  # move through file 2
                if mline['entitlement_uid'] in test_env:  # if the value is in the file 1 list pass
                    pass
                else:  # if the value from file 2 isn't in the list from file 1 write that out as a difference
                    with open('c:/csv2/new_file2.csv', 'ab+') as new_file:  # reopen output file for differences
                        fieldnames = ['course_role', 'entitlement_uid', 'pk1']
                        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n',
                                                    delimiter=',')
                        csv_writer.writerow(mline)

combine_csv()
