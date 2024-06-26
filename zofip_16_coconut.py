#chatgpt 이용함
def cocoprice(coconut):
    stack = []  # 스택을 사용하여 괄호를 처리합니다.
    price = 0

    for i in coconut:
        if i == '(':
            stack.append(price)  # 이전까지의 가격을 스택에 저장합니다.
            price = 0  # 내부 디코넛의 가격을 계산하기 위해 초기화합니다.
        elif i == ')':
            if not stack:  # 올바른 괄호 쌍이 아닌 경우
                return 0

            price += stack.pop() + max(price, 2)  # 내부 디코넛의 가격을 계산합니다.

    if stack:  # 올바른 괄호 쌍이 아닌 경우
        return 0

    return price

coconut = input()
print(cocoprice(coconut))

