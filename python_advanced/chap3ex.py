import string

def raise_stop_iteration():
    # StopIteration
    iterable = "Hello"
    iterator = iter(iterable)
    while True:
        print(next(iterator))

def raise_zero_division_error():
    # ZeroDivisionError
    result = 1 / 0

def raise_assertion_error():
    # AssertionError
    assert 2 + 2 == 5

def raise_import_error():
    # ImportError
    #import non_existing
    return 0

def raise_key_error():
    # KeyError
    my_dict = {"key": "value"}
    print(my_dict["non_existing_key"])

def raise_syntax_error():
    # SyntaxError
    eval("print('Hello, World!'")

# def raise_indentation_error():
#     # IndentationError
#     def my_function():
#         print("This line is indented correctly")
#          print("This line has an extra space at the beginning")
#
#     my_function()

def raise_type_error():
    # TypeError
    sum = "0" + 1000

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            result = "__CONTENT_START__\n" + content + "\n__CONTENT_END__"
            return result
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
    except Exception as e:
        return "__CONTENT_START__\n__ERROR__: {}\n__CONTENT_END__".format(str(e))
    finally:
        print("nice try")

class UnderAge(Exception):
    def __str__(self):
        return "You are under 18. In a few years, you'll be able to join ido's birthday!"

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)




class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_char, position):
        self.illegal_char = illegal_char
        self.position = position

    def __str__(self):
        return f'The username contains an illegal character "{self.illegal_char}" at index {self.position}.'

class UsernameTooShort(Exception):
    def __str__(self):
        return 'The username is too short.'

class UsernameTooLong(Exception):
    def __str__(self):
        return 'The username is too long.'

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return 'The password is missing a character.'

class PasswordTooShort(PasswordMissingCharacter):
    def __str__(self):
        return 'The password is too short.'

class PasswordTooLong(PasswordMissingCharacter):
    def __str__(self):
        return 'The password is too long.'

class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Uppercase)'

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Lowercase)'

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Digit)'

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Special)'

def check_input(username, password):
    legal_chars = string.ascii_letters + string.digits + '_'

    if len(username) < 3:
        raise UsernameTooShort()
    elif len(username) > 16:
        raise UsernameTooLong()
    else:
        for idx, char in enumerate(username):
            if char not in legal_chars:
                raise UsernameContainsIllegalCharacter(char, idx)

    if len(password) < 8:
        raise PasswordTooShort()
    elif len(password) > 40:
        raise PasswordTooLong()

    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    elif not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    elif not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    elif not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

    print("OK")




# Main program
def main():
    # raise_stop_iteration()
    # raise_zero_division_error()
    # raise_assertion_error()
    # raise_import_error()
    # raise_key_error()
    # raise_syntax_error()
    # raise_indentation_error()
    # raise_type_error()

    # print(read_file("notexist.txt"))

    # send_invitation("John", 17)
    # send_invitation("Alice", 20)

    # Testing the function
    try:
        check_input("1", "2")
    except Exception as e:
        print(e)

    try:
        check_input("0123456789ABCDEFG", "2")
    except Exception as e:
        print(e)

    try:
        check_input("A_a1.", "12345678")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "2")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "abcdefghijklmnop")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGHIJLKMNOP")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGhijklmnop")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "4BCD3F6h1jk1mn0p")
    except Exception as e:
        print(e)

    return 0


if __name__ == '__main__':
    main()
















