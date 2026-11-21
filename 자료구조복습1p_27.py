class Node:
    def __init__(self, data): #전달받은 값을 node의 data에 저장하고, prev와 next를 None으로 초기화
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList: #노드 하나가 아니라 여러개를 관리하는 이중연결리스트, 첫 번째 노드와 마지막 노드를 가리킨다, 리스크가 비어 있으면 둘 다 None이다. 
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data): #처음에 삽입
        new_node = Node(data) #새로운 new_node를 생성한다.

        if self.head is None: #만약 리스트가 비어있다면
           self.head = new_node #head가 새 노드를 가리키고
           self.tail = new_node #tail도 새 노드를 가리킨다.
        else:                   #리스트가 비어있지 않다면
           new_node.next = self.head #새 노드의 next가 현재 head를 가리키고
           self.head.prev = new_node #현재 head의 prev가 새 노드를 가리키고
           self.head = new_node #head가 새 노드를 가리킨다.


def insert_last(self, data): #마지막에 삽입
    new_node = Node(data)

    if self.tail is None: #만약 리스트가 비어있다면
        self.head = new_node #head가 새 노드를 가리키고
        self.tail = new_node #tail도 새 노드를 가리킨다.
    else:
        self.tail.next = new_node #tail의 next가 새 노드를 가리키고
        new_node.prev = self.tail #새 노드의 prev가 현재 tail을 가리키고
        self.tail = new_node #tail이 새 노드를 가리킨다.


def insert_after(self, target, data): #target 값이 있는 노드 뒤에 새 노드를 삽입한다.
    current = self.head # target 값을 찾기 위해 head부터 시작한다.

    while current is not None: #리스트 끝까지 반복한다.
        if current.data == target: #만약 현재 노드의 data가 target과 같다면
            new_node = Node(data) #새로운 노드를 생성한다.

            new_node.prev = current #새 노드의 prev가 현재 노드를 가리키고
            new_node.next = current.next #새 노드의 next가 현재 노드의 next를 가리킨다.

            if current.next is not None: #만약 현재 노드의 next가 None이 아니라면(즉, 현재 노드가 마지막 노드가 아니라면)
                current.next.prev = new_node #현재 노드의 next의 prev가 새 노드를 가리키도록 한다.
            else: #만약 현재 노드의 next가 None이라면(즉, 현재 노드가 마지막 노드라면)
                self.tail = new_node #tail이 새 노드를 가리키도록 한다.

            current.next = new_node #현재 노드의 next가 새 노드를 가리키도록 한다.
            return

        current = current.next #만약 현재 노드의 data가 target과 같지 않다면, current를 다음 노드로 이동시킨다.


def delete_first(self): #첫 번째 노드를 삭제한다.
    if self.head is None: # 만약 리스트가 비어있다면 삭제할 것이 없으므로 return한다.
        return

    if self.head == self.tail: #만약 리스트에 노드가 하나만 있다면
        self.head = None #head와 tail을 None으로 만들어서 리스트를 비어있게 만든다.
        self.tail = None 
    else: #만약 리스트에 노드가 여러 개 있다면
        self.head = self.head.next #head가 첫 노드의 다음노드를 가리키게 만들고
        self.head.prev = None #단일 연결리스트가 아니라 이중연결리스트라서 역방향으로 연결된 것도 끊어주기 위해 head의 prev를 None으로 만든다.


def delete_last(self): #마지막 노드를 삭제한다.
    if self.tail is None: #빈 리스트라면 종료한다.
        return

    if self.head == self.tail: #만약 리스트에 노드가 하나만 있다면
        self.head = None #head와 tail을 None으로 만들어서 리스트를 비어있게 만든다.
        self.tail = None
    else:                #만약 리스트에 노드가 여러 개 있다면
        self.tail = self.tail.prev #tail이 마지막 노드의 이전 노드를 가리키게 만들고
        self.tail.next = None #단일 연결리스트가 아니라 이중연결리스트라서 역방향으로 연결된 것도 끊어주기 위해 tail의 next를 None으로 만든다.


def delete(self, data): #data 값을 가진 노드를 삭제한다.
    current = self.head #첫 노드부터 삭제할 노드를 탐색하기 시작한다.

    while current is not None: #리스트 끝까지 반복한다.
        if current.data == data: #만약 현재 노드의 data가 삭제할 data와 같다면
            if current == self.head: #찾은 data가 첫 노드라면
                self.delete_first() #delete_first()를 살행한다.
            elif current == self.tail: #찾은 data가 마지막 노드라면
                self.delete_last() #delete_last()를 실행한다.
            else:                  #찾은 data가 첫 노드도 마지막 노드도 아니라면
                current.prev.next = current.next #현재 노드의 이전 노드의 next가 현재 노드의 next를 가리키도록 한다.
                current.next.prev = current.prev #현재 노드의 next의 prev가 현재 노드의 prev를 가리키도록 한다.
            return

        current = current.next #아직 원하는 data를 찾지 못했다면 current를 다음 노드로 이동시킨다.


def search(self, data): #원하는 data 값을 가진 노드를 찾는다.
    current = self.head #첫 노드부터 탐색을 시작한다.

    while current is not None: #리스트 끝까지 반복한다.
        if current.data == data: #만약 현재 노드의 data가 찾고자 하는 data와 같다면
            return current       #찾은 노드를 반환한다.
        current = current.next   #아직 원하는 data를 찾지 못했다면 current를 다음 노드로 이동시킨다.

    return None                  #만약 리스트 끝까지 탐색했는데도 원하는 data를 찾지 못했다면 None을 반환한다.


def print_forward(self): #정방향 출력
    current = self.head  #첫 노드부터 시작

    while current is not None: #리스트 끝까지 반복한다.
        print(current.data, end=" ") #노드 출력 그리고 공백 출력
        current = current.next #current를 다음 노드로 이동시킨다.

    print() #줄 바꿈을 해준다


def print_backward(self): #역방향 출력
    current = self.tail   #마지막 노드부터 시작한다

    while current is not None: #리스트 끝까지 반복한다.
        print(current.data, end=" ") #노드 출력 그리고 공백 출력
        current = current.prev #current를 이전 노드로 이동시킨다.

    print() #줄 바꿈을 해준다 
    
