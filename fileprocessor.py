with open('fileprocessor.input',) as file:
    lines = file.readlines()
print('Printing out User Data:\n')

for line in lines:
    line = line.strip()
    if line and not line.startswith('#'):
        username, password, userid, groupid = line.split(':')
        print(f"The user {username} has a password of {password} and has a userid {userid} and groupid {groupid}")
print("\nEnd of User data")
