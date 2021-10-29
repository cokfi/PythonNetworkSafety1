# Given an unsorted array of positive and negative numbers and another number X.
# check if there is a pair of numbers in the array whose sum is equal to the number X.

def pair_sum_detect(lis,x):
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            if lis[i] + lis[j] == x:
                return True
    return False


def main():
    input_string = input('Enter elements of list separated by space ')
    x = int(input('Enter number x '))
    lis = list(map(int,input_string.split()))
    if pair_sum_detect(lis,x):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()