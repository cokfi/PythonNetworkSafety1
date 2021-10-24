
# python program to find max of 3 numbers
def task7():
    print("Enter 3 numbers with space between them")
    numbers = list(map(int,input().split())) #return a list of numbers
    max = numbers[0]
    if (numbers[1]>numbers[0]):
        if (numbers[1]>numbers[2]):
            max = numbers[1]
        else:
            max = numbers[2]
    else:
        if numbers[0]>numbers[2]:
            max = numbers[0]
        else:
            max = numbers[1]
    print("The maximum number is ",max)



def main():
    task7()

if __name__ == '__main__':
    main()