example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("#list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))

print("#for반복문과 enumerate() 함수 조합")
for i, value in enumerate(example_list):
    print("{}번째 요소: {}".format(i, value))