email_id = input("Enter email: ").strip()

username = email_id[:email_id.index('@')]

domain = email_id[email_id.index('@') + 1:]


print(f"Your username is: {username} and your domain name is: {domain}")
