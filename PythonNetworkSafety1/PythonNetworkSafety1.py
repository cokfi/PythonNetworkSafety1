#
def task1():
  print("Enter your name")
  name = input()
  print("Enter your age")
  age = input()
  age = int(age)+100
  print(name," you will be ",age," years old in a hundred years!" )
def main():
    task1()

if __name__ == '__main__':
    main()
