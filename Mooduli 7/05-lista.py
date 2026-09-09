def delete_unevens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lite_numbers = delete_unevens(numbers)
print(f'Original list: {numbers}')
print(f'Lite list: {lite_numbers}')
