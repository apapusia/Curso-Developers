def FizzBuzz(max_number):
    numbers=range(1,max_number+1)
    for number in numbers:
        if number%3==0 and number%5==0:
            print('FizzBuzz')
            continue
        elif number%3==0:
            print('Fizz')
            continue
        elif number%5==0:
            print('Buzz')
            continue
        else:
            print(number)


FizzBuzz(1500)
