from random import sample
from sys import get_int_max_str_digits

from flask import Flask, render_template, request
from markupsafe import escape

# Integer string conversion length limitation
INT_MAX_STR = get_int_max_str_digits()
RAND_MAX_RANGE = 100
RAND_COUNT = 20

app = Flask(__name__)


def foobar(num: int) -> str:
    result = ''
    if num % 3 == 0:
        result += 'foo'
    if num % 5 == 0:
        result += 'bar'
    if result == '':
        result = num
    return result


def parse_input_nums(input_nums: str) -> list[int]:
    nums = input_nums.split()
    ints = []
    for num in nums:
        if num.isdigit():
            ints.append(int(num[:INT_MAX_STR]))
    return ints


def random_nums() -> list[int]:
    return sample(range(1, RAND_MAX_RANGE), RAND_COUNT)


@app.route('/', methods=['POST', 'GET'])
def index():
    answer = []
    input_nums = ''
    if request.method == 'POST':
        if 'button-generate' in request.form.keys():
            input_nums = ' '.join(str(num) for num in random_nums())
        else:
            nums = parse_input_nums(escape(request.form['input-nums']))
            input_nums = ' '.join(str(num) for num in nums)
            for num in nums:
                answer.append(f'{num} -> {foobar(num)}')
    return render_template('index.html', answer=answer, input_nums=input_nums)
