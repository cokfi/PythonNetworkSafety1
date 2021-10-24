
# python program to generate strong passwords
import random
def task5():
    password_length = random.randint(8, 16)
    string = ""
    for i in range(password_length):
        character =chr(random.randint(33, 126+1))# 33 to 126 from ascii table
        string += str(character)

    print("Your password is ",string)
def main():
    task5()

if __name__ == '__main__':
    main()
