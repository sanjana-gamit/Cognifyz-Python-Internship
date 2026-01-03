def validate_email(email):
    if "@" in email and "." in email:
        return "Valid Email"
    else:
        return "Invalid Email"

print(validate_email("test@gmail.com"))
