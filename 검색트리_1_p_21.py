
class TreeNode: #BST를 구성하는 노드 하나를 만드는 class이다.
    def __init__(self, key):
        self.key = key #노드에 저장할 값을 설정한다.
        self.left = None #처음에는 자식이 없으니까 left와 right를 None로 초기화한다.
        self.right = None


class BST: #여러 노드를 관리한다.
    def __init__(self):
        self.root = None #root는 가장 위에 있는 노드를 가리킨다. 처음에는 아무것도 없으니까 root를 None로 초기화한다.

    # 새로운 key 삽입 (반복문)
    def insert(self, key):
        new_node = TreeNode(key) #삽입할 값을 가진 새로운 노드를 생성한다.

        if self.root is None: #root가 none이라는 것은 트리 자체에 아무것도 없다는 것이므로 root에 newnode를 삽입한다.
            self.root = new_node 
            return

        current = self.root #처음에는 root부터 탐색하기 위해 current가 root를 가리키게 한다.
        parent = None #그리고 처음에는 parent가 None이다.

        while current is not None: #끝까지 탐색한다. current가 None이 되면 더 이상 노드가 없는 위치에 도달한 것 이므로 while문을 종료한다.
            parent = current #일단 현재 부모 노드를 부모 노드로 기억한다.
            if key < current.key: #만약 찾고 있는 값이 current보다 작다면 current를 왼쪽 자식으로 이동한다.
                current = current.left
            elif key > current.key: #더 크다면 current를 오른쪽 자식으로 이동한다.
                current = current.right
            else:
                # 삽입할 값이 현재노드의 값과 같다면 BST에서는 중복값을 허용하지 않으므로 새로운 노드를 연결하지 않고 함수를 종료한다.
                return

        if key < parent.key: #while문이 종료되었다면 current는 None이고 parent는 마지막으로 방문한 노드이다. 삽입할 값과 부모 노드의 값을 비교해서 왼쪽과 오른쪽에 연결할지 결정한다.
            parent.left = new_node
        else:
            parent.right = new_node

    # key에 해당하는 노드 삭제 (반복문)
    def delete(self, key):
        current = self.root #처음(root)부터 탐색하기 시작한다.
        parent = None #parent를 None로 초기화한다.

        # 1. 삭제할 노드와 그 부모 탐색
        while current is not None and current.key != key: #current가 None이 아닐때까지라는 것은 끝까지 탐색할겠다는 뜻이고 current.ket!=key는 현재 노드가 삭제할려고 하는 노드가 아니다라는 뜻이다. 두 조건을 모두 만족하면 while문을 실행한다.
            parent = current #parent를 current로 초기화한다. 
            if key < current.key: #만약 찾고 있는 값이 current보다 작다면 current를 왼쪽 자식으로 이동한다.
                current = current.left
            else: #그게 아니면 current를 오른쪽 자식으로 이동한다.
                current = current.right

        # 삭제할 노드가 없는 경우
        if current is None:
            return

        # 2. 자식이 2개인 경우: 오른쪽 서브트리의 최솟값(successor)으로 대체
        if current.left is not None and current.right is not None:
            succ_parent = current #succ_parent는 후속자 노드의 부모를 기억하기 위한 변수이다.
            successor = current.right #successor는 후속자를 찾기 위해 이동하는 변수이다. 후혹자는 오른쪽 서브트리에서 가장 작은 값을 가진 노드이므로 먼저 오른쪽 자식을 이동한다.

            while successor.left is not None: #오른쪽 서브트리에서 최솟값을 찾기 위한 while문이다.
                succ_parent = successor
                successor = successor.left

            # successor의 값을 현재 노드에 복사
            current.key = successor.key #삭제하려는 노드의 값을 후속자 값으로 변경한다.

            # 이제 successor 노드(자식이 최대 1개: 오른쪽 자식만 가능)를 삭제 대상으로 전환
            current = successor
            parent = succ_parent

        # 3. 자식이 0개 또는 1개인 노드 삭제
        child = current.left if current.left is not None else current.right

        if parent is None:
            # 루트 노드를 삭제하는 경우
            self.root = child
        elif parent.left is current:
            parent.left = child
        else:
            parent.right = child

    # 중위 순회 결과 출력 (스택 기반 반복문)
    def inorder(self):
        result = []
        stack = []
        current = self.root

        while current is not None or stack:
            # 왼쪽 끝까지 내려가며 경로를 스택에 저장
            while current is not None:
                stack.append(current)
                current = current.left

            # 가장 왼쪽 노드 방문 및 값 기록
            current = stack.pop()
            result.append(str(current.key))

            # 오른쪽 서브트리로 이동
            current = current.right

        print(" ".join(result))


if __name__ == "__main__":
    bst = BST()

    # 초기 BST 생성
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)

    print("초기 BST:")
    bst.inorder()

    # 자식이 0개인 노드 삭제
    bst.delete(20)
    print("20 삭제 후 (자식 0개):")
    bst.inorder()

    # 자식이 1개인 노드 삭제
    bst.delete(30)
    print("30 삭제 후 (자식 1개):")
    bst.inorder()

    # 자식이 2개인 노드 삭제
    bst.delete(50)
    print("50 삭제 후 (자식 2개):")
    bst.inorder()
