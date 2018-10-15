import csv

def primary_csv():
    with open('c:/csv/sys_roles1.csv', 'ab+') as new_file:  # Create new file
        fieldnames = ['user_id', 'firstname', 'lastname', 'primary_sys', 'SyS Role Name', 'Role Name', 'prim_inst_role']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',')
        csv_writer.writeheader()
    sysmaster = 'c:/csv/System_roles_Master.csv'
    primroles = 'c:/csv/primary_roles.csv'
    with open(primroles) as primuserroles:
        pusers = csv.DictReader(primuserroles)
        for uline in pusers:
            sys_role = uline['primary_sys']
            with open(sysmaster) as smaster:
                sysroles = csv.DictReader(smaster)
                for sline in sysroles:
                    role = sline['system_role']
                    if sys_role == role:
                        new_line = uline  # description from the master
                        new_line['SyS Role Name'] = sline['name']
                        with open('c:/csv/sys_roles1.csv', 'ab+') as new_file:  # Create new file
                            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',') # define writer
                            csv_writer.writerow(new_line)   # write the new line.

def priminst():
    with open('c:/csv/prim_roles_all.csv', 'ab+') as new_file:  # Create new file
        fieldnames = ['user_id', 'firstname', 'lastname', 'primary_sys', 'SyS Role Name', 'Role Name', 'prim_inst_role',
                      'Inst Role Name']  # define headers
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',')
        csv_writer.writeheader()
    instmaster = 'c:/csv/Inst_Roles_Master.csv'
    primroles = 'c:/csv/sys_roles1.csv'
    with open(primroles) as primuserroles:
        pusers = csv.DictReader(primuserroles)
        for uline in pusers:
            ins_role = uline['prim_inst_role']
            with open(instmaster) as smaster:
                instroles = csv.DictReader(smaster)
                for sline in instroles:
                    role = sline['pk1']
                    if ins_role == role:
                        new_line = uline  # description from the master
                        new_line['Inst Role Name'] = sline['role_name']
                        with open('c:/csv/prim_roles_all.csv', 'ab+') as new_file:  # Create new file
                            fieldnames = ['user_id', 'firstname', 'lastname', 'primary_sys', 'SyS Role Name', 'Role Name', 'prim_inst_role', 'Inst Role Name'] # define headers
                            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',') # define writer
                            csv_writer.writerow(new_line)   # write the new line.

def secinst():
    userroles = 'c:/csv/secondary_institution.csv'
    instmast = 'c:/csv/Inst_Roles_Master.csv'
    with open('c:/csv/sec_inst_roles_fin.csv', 'ab+') as new_file:  # Create new file
        fieldnames = ['user_id', 'firstname', 'lastname', 'secondary_inst_role', 'prim_inst_role', 'Inst Role Name']  # define headers
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',')
        csv_writer.writeheader()
    with open(userroles) as secroles:
        iusers = csv.DictReader(secroles)
        for uline in iusers:
            insrole = uline['secondary_inst_role']
            with open(instmast) as instmaster:
                imaster = csv.DictReader(instmaster)
                for mline in imaster:
                    role = mline['pk1']
                    if insrole == role:
                        new_line = uline
                        new_line['Inst Role Name'] = mline['role_name']
                        with open('c:/csv/sec_inst_roles_fin.csv', 'ab+') as new_file:  # Create new file
                            fieldnames = ['user_id', 'firstname', 'lastname', 'secondary_inst_role', 'prim_inst_role', 'Inst Role Name']  # define headers
                            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n', delimiter=',')
                            csv_writer.writerow(new_line)






# def sec_inst():
#     instmaster = 'c:/csv/Inst_Roles_Master.csv'  # hard coded the file paths cause lazy
#     secinst = 'c:/csv/secondary_institution.csv'
#
# def sec_sys():
#     sysmaster = 'c:/csv/System_roles_Master.csv'
#     secsys = 'c:/csv/Secondary_System.csv'





    # with open(testdata, 'r') as users:                 # open test data with users list and pk1 of role
    #     usersDict = csv.DictReader(users)                # csv dict reader makes each row a dict object
    #     for line in usersDict:                            # loop through users and pull the permissions value
    #         userRole = line['permission']                # this actually saves the pk1 from users by calling the key
    #         with open(masterlist) as master:               # opening the role master with pk1 and description
    #             role_master = csv.DictReader(master)       # making our dict object
    #             for mline in role_master:                  # move through master list comparing role pk1 to user pk1
    #                 if  mline['pk1'] != userRole:         # if the don't match just keep trucking
    #                     pass
    #                 else:                                # if they do match create a new dict object adding the
    #                     new_line = line                  # description from the master
    #                     new_line['Role Name'] = mline['description']
    #                     with open('c:/users/E/Desktop/new_file.csv', 'a+') as new_file:  # Create new file
    #                         fieldnames = ['firstname', 'lastname', 'permission', 'Role Name'] # define headers
    #                         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',') # define writer
    #                         csv_writer.writerow(new_line)   # write the new line.


primary_csv()
priminst()
secinst()