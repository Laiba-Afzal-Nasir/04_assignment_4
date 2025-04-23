import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check):
    hashed_password = hash_password(password_to_check)
    stored_logins = {
        'abc@example.com': hash_password('password123'),
        'xyz@example.com': hash_password('admin'),
        'pqr3@example.com': hash_password('admin124'),
    }
  
    if email in stored_logins:
        if stored_logins[email] == hashed_password:
            return "Login Successful"
        else:
            return "Wrong Password"
    else:
        return "Email Not Found"

def main():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    result = login(email, password)
    print(result)

if __name__ == "__main__":
    main()