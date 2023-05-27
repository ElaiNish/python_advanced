import functools

def double_letter_help(ch1):
    return ch1*2
def double_letter(my_str):
    return ''.join(map(double_letter_help ,my_str))

def four_dividers_help(number):
    return number%4==0

def four_dividers(number):
    return list(filter(four_dividers_help, range(1, number + 1)))

def sum_of_digits(number):
    return sum(map(int, str(number)))

def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))

def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))

def is_funny(string):
    return all(char == 'h' or char == 'a' for char in string)







def main():
    # str1 = "we are the champions!"
    # print(double_letter(str1))
    #
    # print(four_dividers(9))
    #
    # print(sum_of_digits(104))

    # d = lambda x, y: int(x/y) if x>y else int(y/x)
    # print(d(1, 3))
    # print(d(5, 2))

    # print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

    # print(is_funny("hcahahahahaha"))

    # תרגיל מסכם כל הפונקציות

    names = open("names.txt").read().splitlines()

    # print(max(names, key=len))
    #
    # print(sum(len(name) for name in names))

    # shortest = len(min(names, key=len))
    # print('\n'.join(name for name in names if len(name) == shortest))

    # with open("name_length.txt", "w") as file:
    #     file.write('\n'.join(str(len(name)) for name in names))

    length = int(input("Enter num: "))
    print('\n'.join(name for name in names if len(name) == length))

    return 0

if __name__ == '__main__':
    main()