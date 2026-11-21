def infix_to_postfix(self, expression):
    self.stack = []    # 연산자를 보관하는 스택 초기화
    self.output = []   # 후위 수식을 저장하는 리스트 초기화

    expression = self.tokenization(expression) #전달받은 문자열을 토큰화한다. 예를 들어 "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"와 같은 문자열을 ['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2', '^', '3']와 같이 리스트로 만든다.
 
    for token in expression: #토큰화한 것을 하나씩 읽는다.
        # 1. 피연산자이면 결과에 바로 추가
        if self.is_operand(token):
            self.output.append(token)

        # 2. 여는 괄호이면 스택에 추가
        elif token == '(':
            self.stack.append(token)

        # 3. 닫는 괄호이면 '('가 나올 때까지 연산자를 출력
        elif token == ')':
            while self.stack and self.stack[-1] != '(':
                self.output.append(self.stack.pop())

            self.stack.pop()  # '(' 제거: 결과에는 넣지 않음

        # 4. 연산자인 경우
        else:
            # 수정한 부분: 우선순위와 결합 방향을 함께 확인
            while (
                self.stack # 스택이 비어 있지 않고
                and self.stack[-1] != '(' # 스택의 top이 '('가 아니고
                and (
                    self.precedence(self.stack[-1]) # 스택의 top 연산자의 우선순위가 현재 토큰의 우선순위보다 크거나 같으면
                    > self.precedence(token)
                    or ( 
                        self.precedence(self.stack[-1]) # 스택의 top 연산자의 우선순위가 현재 토큰의 우선순위와 같고
                        == self.precedence(token)
                        and token != '^' # 현재 토큰이 '^'가 아니면(즉, 왼쪽 결합이면)
                    )
                )
            ):
                self.output.append(self.stack.pop()) #스택의 top 연산자를 결과에 추가하고 스택에서 제거한다.

            self.stack.append(token) #현재 토큰을 스택에 추가한다.

    # 5. 입력을 모두 읽은 뒤 남은 연산자 출력
    while self.stack: 
        self.output.append(self.stack.pop()) #스택에 남아 있는 연산자를 결과에 추가하고 스택에서 제거한다.

    return ' '.join(self.output) #결과 리스트를 문자열로 변환하여 반환한다. 예를 들어 ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+']와 같은 리스트를 "3 4 2 * 1 5 - 2 3 ^ ^ / +"와 같은 문자열로 만든다.