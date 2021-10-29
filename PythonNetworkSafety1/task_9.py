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