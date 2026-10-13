
def validate_password(password):
    if len(password) < 8:
        return "password is too short"
    else:
        return "password accepted"

print(validate_password("abc"))
print(validate_password("python123"))
