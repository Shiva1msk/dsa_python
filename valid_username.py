def valid_username(username):
    username=username.strip()
    if username=="":
        return "username cannot be empty"
    elif len(username)<3:
        return "username too short"
    else:
        return "username accepted"