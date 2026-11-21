def quick_sort(A,p,r):
    if p<r: #시작<끝 이라면 element가 2개 이상 p==r(이미 정렬), p>r(빈 공간x)
        q=partition(A,p,r) #q는 pivot의 index

        quick_sort(A,p,q-1) #pivot의 왼쪽 구간 정렬
        quick_sort(A,q+1,r) #pivot의 오른쪽 구간 정렬

def partition(A,p,r): 
    x=A[r] #구간의 마지막을 pivot이라고 한다.
    i=p-1 #pivot보다 작은 원소 구간의 마지막 index

    for j in range(p,r): #j는 p부터 r-1까지, A[r]는 pivot이라 r은 제외
        if A[j]<x: #pivot보다 작다면
            i+=1 #pivot의 왼쪽 구간을 1만큼 확장해서 그 확장공간에 A[j를 넣는다
            A[i],A[j] = A[j],A[i]

    A[i+1], A[r]= A[r], A[i+1] #pivot보다 작은 구간의 마지막 index 바로 다음 index에 pivot이 위치하도록 한다.

    return i+1 #pivot의 index를 반환한다.       