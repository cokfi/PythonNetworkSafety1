# python program to check whether a number is prime

def is_prime(num):
    if num > 1:
        for i in range(2,int(num**0.5) + 1):
            if(num % i) == 0:
                print(num, "Is not prime")
                break
        else:
            print(num, "Is prime")
    else:
        print(num, "Is not prime")

def main():
    print("Enter a number")
    number = int(input())
    is_prime(number)

if __name__ == '__main__':
    main()