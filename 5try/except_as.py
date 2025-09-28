list_number = [52, 273, 32, 7, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다!")
    print("exception:", exception)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)