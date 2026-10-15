# ADVANCED NUMBER ANALYZER

def is_prime(number):
    if number <= 1: return False
    elif number == 2: return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def get_divisors(number):
    if is_prime(number):
        return [1, number]

    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors

def sum_of_digits(number):
    total = 0

    while number:
        last = number % 10
        total += last
        number = number // 10

    return total

def reverse_number(number):
    result = 0
    div = 1
    while number >= div*10:
        div *= 10

    add = 1
    while number:
        digit = number // div
        result += digit * add
        add *= 10
        number = number % div
        div /= 10

    return int(result)

def analyze_number(number):
    analysis = []
    if is_prime(number):
        analysis.append("PRIME NUMBER")
    divisors = get_divisors(number)
    total_sum = sum_of_digits(number)
    rev = reverse_number(number)
    analysis.extend([f"Divisors: {divisors}", f"Sum of its digit: {total_sum}", f"The number in reverse: {rev}"])

    return analysis

print(analyze_number(123))