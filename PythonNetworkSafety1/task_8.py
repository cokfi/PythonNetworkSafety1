# generate txt files : One txt file has a list of all prime numbers under 1000,
# and the other txt file has a list of happy numbers up to 1000 .
# Given those two txt files that have lists of numbers in them, find the numbers that are overlapping. 

def is_prime(num):
    if num > 1:
        for i in range(2,int(num**0.5) + 1):
            if(num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def numSquareSum(n):
    squareSum = 0;
    while (n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;


def isHappynumber(n):
    # set slow and fast to n
    slow = n;
    fast = n;
    while (True): #check if there is a loop

        # move slow number by one iteration
        slow = numSquareSum(slow);

        # move fast number by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if (slow != fast): # check if they meet
            continue;
        else:
            break;

    # if both number meet at 1, return True
    return slow == 1;


def main():
    common_list = []
    p = open("prime.txt", "w")
    h = open("happy.txt", "w")
    for i in range(1001):
        if is_prime(i):
            p.write(str(i) + " ")
        if isHappynumber(i):
            h.write(str(i) + " ")
    p.close()
    h.close()
    prime = open("prime.txt", "r")
    happy = open("happy.txt", "r")
    prime_list = list(map(int,prime.read().split()))
    happy_list = list(map(int,happy.read().split()))
    prime.close()
    happy.close()
    for element in prime_list:
        if element in happy_list:
            common_list.append(element)
    print(common_list)

if __name__ == '__main__':
    main()