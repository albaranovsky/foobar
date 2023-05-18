def foobar(num: int) -> str:
    result = ''
    if num % 3 == 0:
        result += 'Foo'
    if num % 5 == 0:
        result += 'Bar'
    if result == '':
        result = num
    return result


# print(foobar(150))
for i in range(1, 101):
    print(i, ' - ', foobar(i))
