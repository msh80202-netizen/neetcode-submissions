class PasswordManager:
    def __init__(self, name: str):
        self.__name = name  
    
    # TODO: Implement the verify_password method


    def verify_password(self, typed) -> bool:
        return self.__name == typed



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
