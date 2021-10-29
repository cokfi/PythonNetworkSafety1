# get a sorted list of numbers and another number X.
# decides whether or not the given number X is inside the list or not andreturns True/False answer

def in_list(lis, x):
    if x in lis:
        print("True")
    else :
        print("False")
def main():
    input_string = input('Enter elements of sorted list separated by space ')
    lis = list(map(int,input_string.split()))
    x = int(input('Enter number x '))
    in_list(lis,x)

if __name__ == '__main__':
    main()