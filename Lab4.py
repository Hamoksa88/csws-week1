Usernames=['Admin','James','Hammond','Jeremey']
Admin_Message = f"Hello Admin, Would You Like to see a Status Report?{Usernames[0].title()}"
Usernames_noadmin=Usernames.pop(0)
username_message = f"Hello {Usernames[1]}"
if Usernames == 'Admin':
    print(Admin_Message)

for Usernames in Usernames:
 print(f"Hello {Usernames}")

Empty_username = []

if Empty_username:
    for Empty_username in Empty_username:
     print(f"hello {Usernames}.")

else:
     print("No message to output list is empty")
