current_users=["James","Clarkson","Richard"]
new_users=["james"]

for new_users in new_users:
    if new_users in current_users:
        print("username taken")

    else:
        print("user added")

