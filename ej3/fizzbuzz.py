for i in range(1, 21):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz', end=', ')
        continue
    elif i%3 == 0:
        print('Fizz', end=', ')
    elif i%5 == 0:
        print('Buzz',  end=', ')
    else:
        print(i, end=', ')