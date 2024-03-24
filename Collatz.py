import time

print('Collatz Conjecture')


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        time.sleep(0.1)
        return number
    else:
        number = 3 * number + 1
        print(number)
        time.sleep(0.1)
        return number


while True:
    try:
        userNum = int(input('enter number: '))
    except ValueError:
        print('you must enter an integer')
        continue
    break

while True:
    userNum = collatz(userNum)
    if userNum == 1:
        break
    else:
        continue
input()
