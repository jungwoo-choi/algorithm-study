class TreeNode:
    # BST를 구성하는 노드 하나를 만든다. 노드 하나가 단어 하나를 나타낸다.
    def __init__(self, key, frequency, pos):
        self.key = key              # 단어를 저장한다. 예를 들어 "abandon"이다.
        self.frequency = frequency  # 사진의 Frequency 열에 있는 빈도를 저장한다.
        self.pos = [pos]            # 처음 받은 품사를 리스트에 넣는다. 예를 들어 ["NN"]이다.
        self.left = None            # 사전순으로 앞에 오는 단어를 연결할 왼쪽 자식이다.
        self.right = None           # 사전순으로 뒤에 오는 단어를 연결할 오른쪽 자식이다.


class BST:
    def __init__(self):
        self.root = None  # 처음에는 저장된 단어가 없으므로 루트도 없다.

    # 1. 단어, 빈도, 품사를 삽입한다.
    def insert(self, key, frequency, pos):
        if self.root is None:  # 빈 트리라면 첫 번째 단어가 루트가 된다.
            self.root = TreeNode(key, frequency, pos)
            return

        current = self.root  # 루트부터 단어를 비교한다.
        parent = None        # current가 빈자리까지 내려갔을 때 그 부모를 기억할 변수이다.

        while current is not None:
            parent = current  # 자식으로 이동하기 전에 현재 노드를 기억한다.

            if key < current.key:       # 새 단어가 현재 단어보다 사전순으로 앞에 있으면
                current = current.left  # 왼쪽 자식으로 이동한다.
            elif key > current.key:     # 새 단어가 현재 단어보다 사전순으로 뒤에 있으면
                current = current.right # 오른쪽 자식으로 이동한다.
            else:
                # 여기까지 왔으면 key == current.key이므로 이미 저장된 단어이다.
                if pos not in current.pos:   # 이 단어에 아직 없는 품사인지 확인한다.
                    current.pos.append(pos)  # 예를 들어 ["NN"]에 "VB"를 추가한다.
                return  # 같은 단어의 빈도는 한 번만 저장하고 삽입을 끝낸다.

        # current가 None이 되면 새 단어를 넣을 빈자리를 찾은 것이다.
        # 이때 parent는 그 빈자리 바로 위의 노드를 가리킨다.
        new_node = TreeNode(key, frequency, pos)

        if key < parent.key:
            parent.left = new_node   # 부모보다 앞선 단어이면 왼쪽에 연결한다.
        else:
            parent.right = new_node  # 부모보다 뒤인 단어이면 오른쪽에 연결한다.

    # 2. 단어를 검색하고, 찾으면 그 단어의 노드를 반환한다.
    def search(self, key):
        current = self.root  # 검색도 루트에서 시작한다.

        while current is not None:
            if key < current.key:
                current = current.left   # 찾는 단어가 더 앞에 있으므로 왼쪽을 탐색한다.
            elif key > current.key:
                current = current.right  # 찾는 단어가 더 뒤에 있으므로 오른쪽을 탐색한다.
            else:
                return current  # 단어를 찾았다. 이 노드에서 빈도와 품사를 꺼낼 수 있다.

        return None  # 빈자리까지 내려왔으므로 트리에 해당 단어가 없다.

    # 3. 단어를 삭제한다. 그 단어에 저장된 빈도와 모든 품사도 함께 삭제된다.
    def delete(self, key):
        current = self.root  # 삭제할 노드를 찾기 위해 루트에서 시작한다.
        parent = None        # 삭제 후 연결을 바꿔야 하므로 부모도 기억한다.

        # 현재 노드가 존재하고, 아직 찾는 단어와 다르면 계속 내려간다.
        while current is not None and current.key != key:
            parent = current  # 이동하기 전에 현재 노드를 부모로 기억한다.

            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:  # 삭제할 단어가 트리에 없으면 바로 종료한다.
            return

        # 자식이 2개이면 오른쪽 서브트리에서 가장 작은 단어인 후속자를 찾는다.
        if current.left is not None and current.right is not None:
            succ_parent = current      # 처음에는 삭제할 노드가 후속자 후보의 부모이다.
            successor = current.right  # 먼저 오른쪽 자식으로 한 번 이동한다.

            while successor.left is not None:
                succ_parent = successor     # 왼쪽으로 이동하기 전에 부모를 기억한다.
                successor = successor.left  # 왼쪽 끝에 도착하면 그 노드가 후속자이다.

            # 현재 자리에 후속자의 단어 정보를 모두 복사한다.
            current.key = successor.key
            current.frequency = successor.frequency
            current.pos = successor.pos.copy()  # 품사 리스트의 내용도 복사한다.

            # 후속자 정보가 현재 자리에 들어갔으므로 원래 후속자 노드를 제거하면 된다.
            current = successor   # 아래에서 실제로 제거할 노드를 가리킨다.
            parent = succ_parent  # 그 노드의 부모를 가리킨다.

        # 여기서 current는 자식이 최대 1개이다.
        # 왼쪽 자식이 있으면 그 자식을, 없으면 오른쪽 자식을 선택한다.
        # 양쪽 모두 없으면 child는 자연스럽게 None이 된다.
        child = current.left if current.left is not None else current.right

        if parent is None:               # 제거할 노드가 루트인 경우이다.
            self.root = child            # 남은 자식이 새 루트가 된다.
        elif parent.left is current:     # 제거할 노드가 부모의 왼쪽 자식인 경우이다.
            parent.left = child          # 부모의 왼쪽을 남은 자식과 연결한다.
        else:
            parent.right = child         # 오른쪽 자식이었다면 부모의 오른쪽을 연결한다.

    # 4. 중위 순회로 사진처럼 단어, 빈도, 품사를 사전순으로 출력한다.
    def inorder(self):
        stack = []           # 나중에 다시 방문할 노드를 저장하는 스택이다.
        current = self.root  # 루트에서 순회를 시작한다.

        # <15는 왼쪽 정렬로 15칸, >10은 오른쪽 정렬로 10칸을 사용한다.
        print(f"{'ENTRY':<15} {'Frequency':>10}  POS")

        while current is not None or stack:
            # 현재 노드를 스택에 저장하면서 왼쪽 끝까지 내려간다.
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()  # 왼쪽 탐색이 끝났으므로 현재 출력할 노드를 꺼낸다.

            # 예를 들어 pos가 ["NN", "VB"]이면 같은 단어를 두 줄로 출력한다.
            for pos in current.pos:
                print(f"{current.key:<15} {current.frequency:>10}  {pos}")

            current = current.right  # 현재 단어를 출력했으므로 오른쪽 서브트리로 이동한다.


if __name__ == "__main__":
    bst = BST()  # 빈 Lexicon을 만든다.

    # 각 튜플은 사진에 있는 한 행이며, 순서는 (단어, 빈도, 품사)이다.
    # 자식이 2개인 경우의 삭제도 확인할 수 있도록 "ability"를 먼저 넣는다.
    entries = [
        ("ability", 5725, "NN"),
        ("abandon", 151, "NN"),
        ("able", 5766, "JJ"),
        ("a", 2380456, "AT"),
        ("abandon", 151, "VB"),
        ("abbreviate", 214, "VB"),
        ("abbreviation", 464, "NN"),
        ("aberration", 1043, "NN"),
        ("abnormal", 451, "JJ"),
        ("abnormality", 216, "NN"),
        ("abort", 274, "NN"),
        ("abort", 274, "VB"),
        ("about", 153361, "IN"),
        ("about", 153361, "RB"),
        ("above", 54731, "IN"),
        ("abrasion", 1038, "NN"),
        ("abrupt", 203, "JJ"),
        ("absence", 2418, "NN"),
        ("absent", 803, "JJ"),
        ("absent", 803, "VB"),
        ("absolute", 2679, "JJ"),
        ("absolutely", 103, "RB"),
        ("absorb", 6451, "VB"),
        ("absorbent", 13697, "JJ"),
        ("absorbent", 13697, "NN"),
        ("absorbing", 2802, "JJ"),
    ]

    for key, frequency, pos in entries:  # 한 행에서 단어, 빈도, 품사를 각각 꺼낸다.
        bst.insert(key, frequency, pos)  # 꺼낸 세 값을 트리에 삽입한다.

    print("[전체 Lexicon]")
    bst.inorder()  # 삽입 순서와 관계없이 a, abandon, abbreviate, ... 순서로 출력된다.

    print("\n[abandon 검색]")
    node = bst.search("abandon")  # abandon이 저장된 노드를 받아 온다.

    if node is not None:
        print("단어:", node.key)                # abandon
        print("빈도:", node.frequency)          # 151
        print("품사:", ", ".join(node.pos))     # NN, VB
    else:
        print("해당 단어가 없습니다.")

    print("\n[ability 삭제]")
    bst.delete("ability")  # 왼쪽과 오른쪽 자식을 모두 가진 루트를 삭제한다.
    bst.inorder()          # ability가 빠지고 나머지 단어가 사전순으로 출력된다.