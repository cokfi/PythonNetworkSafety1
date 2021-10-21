
# python program to calculate the divisors of a number

def task2():
  print("Enter a number")
  num = int(input())
  divisors = []
  for i in range(2,num+1):
    if (num%i ==0):
        divisors.append(i)
  print(divisors)

def main():
    task2()

if __name__ == '__main__':
    main()
