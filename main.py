import utils

print("utils.div > a와 b의 값이 필요합니다.")
print("a값(숫자) : ")
inputNumA = input()
print("b값(숫자) : ")
inputNumB = input()
print(utils.div(int(inputNumA), int(inputNumB)))

print("utils.reverse > 거꾸로 출력할 문장이 필요합니다.")
inputStr = input()
print(utils.reverse(inputStr))

print("utils.is_even > a값이 필요합니다.")
inputNumA = input()
print(utils.is_even(int(inputNumA)))