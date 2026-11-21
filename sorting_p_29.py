def percolate_down(A,k,n): #A는 heap을 저장할 리스트, 현재 수정할 서브리스트의 루트 index, 힙에 포함된 원소 개수
    child=2*k+1
    right=2*k+2

    if child<n: #전체 element 수가 (left)child의 index보다 큰지 확인=> (left)child가 힙에 포함돼있는 index인지 확인
        if right<n and A[child]<A[right]: #right child도 힙에 포함되고 left랑 right중 right이 더 크다면
            child=right #(left)child index에 right(child)index를 넣는다=> 자식 중 가장 큰 element를 가진 index는 child이다.

        if A[k]<A[child]: #부모가 왼쪽 자식보다 작다면
            A[k], A[child]=A[child], A[k] #부모와 왼쪽 자식의 element를 바꾼다.
            percolate_down(A, child, n) #새로 수정된 A[child]로 인해서 하위 서브트리의 힙 조건이 깨질 수 있기 떄문에 수정된 index에서 다시 percolate_down한다.


def build_heap(A):
    n=len(A)

    for k in range((n-2) // 2, -1, -1): #가장 하위의 부모노드부터 root까지 역순으로 처리한다.
        percolate_down(A,k,n)                


def heap_sort(A): 
    build_heap(A) #리스트 전체를 최대 힙으로 만든다.

    for last in range(len(A)-1,0,-1): #last는 이번 반복에서 최대값을 놓을 인덱스이다.
        A[0], A[last]= A[last], A[0]
        percolate_down(A, 0, last)