def evaluate_postfix(expression):
    stack = [] #빈 리스트 객체 생성

    for ch in expression: #문자열(expression)을 왼쭉부터 한 글자씩 읽는다.
        if ch not in "+-*/": #ch가 연산자가 아니라면(숫자라면) 예를 들어 ch가 5이면 연산자가 아니므로 true가 되어 stack.append(int(ch))가 실행된다. 즉, stack에 5를 추가한다.
            stack.append(int(ch)) #스택에 숫자를 추가한다.
        else: #ch가 연산자라면(+, -, *, /) 예를 들어 ch가 +이면 else문이 실행된다.
            op2 = stack.pop()  # 오른쪽 피연산자
            op1 = stack.pop()  # 왼쪽 피연산자

            if ch == "+": # 덧셈
                result = op1 + op2
            elif ch == "-": # 뺄셈
                result = op1 - op2
            elif ch == "*": # 곱셈
                result = op1 * op2  
            else:  # 나눗셈 
                if op2 == 0: # 만약 op2가 0이라면 0으로 나누는 것이므로 ZeroDivisionError를 발생시킨다.
                    raise ZeroDivisionError("0으로 나눌 수 없습니다.")

                result = op1 / op2  # 나눗셈

            stack.append(result) # 연산 결과를 스택에 추가한다.

    return stack.pop() # 마지막으로 스택에 남아 있는 결과를 반환한다.