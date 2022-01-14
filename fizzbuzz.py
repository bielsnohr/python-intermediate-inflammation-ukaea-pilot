print("=== Structural implementation ===")
# this could also be put into a function with the range of values passed as a
# parameter
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print("=== Functional implementation ===")
factors = [[3, 'Fizz'], [5, 'Buzz']]


def fizzbuzz(val):
    result = ''
    for factor, text in factors:
        if val % factor == 0:
            result += text
    else:
        if not result:
            result = str(val)
    return result

# Alternative one liner from course
# fizzbuzz = lambda val: ''.join(text for factor, text in factors if val % factor == 0) or str(val)

outputs = map(fizzbuzz, range(1, 101))
print('\n'.join(outputs))

