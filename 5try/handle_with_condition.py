
try:
    user_input_a = input("정수 입력>")

    number_a = int(user_input_a)
    print("원의 반지름:", number_a)
    print("원의 둘레:", 2 * 3.14 * number_a)
    print("원의 넓이:", 3.14 * number_a * number_a)

except:
    print("무언가 잘못되었습니다")