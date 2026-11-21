def buuble_sort(A): #A는 정렬할 리스트
    n=len(A) #전체 elements의 개수

    for last in range(n-1,0,-1): #시작, 끝, 간격 그리고 끝의 값은 포함x, last는 n-1부터 1까지
        for i in range(last): #i는 0부터 last-1까지
            if A[i]>A[i+1]: #ex) A[0]>A[1]이면 A[0]과 A[1]을 교환한다.
                A[i],A[i+1]=A[i+1],A[i] #이제 A[0]과 A[1]을 교환한다. 이런 식으로 계속하다보면 오름차순으로 정렬된다.