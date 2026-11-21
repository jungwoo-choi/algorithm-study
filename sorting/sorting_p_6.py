def delection_sort(A): #A는 정렬할 리스트
    n=len(A) #전체 elements의 개수

    for last in range(n-1,0,-1): #시작, 끝, 간격 그리고 끝의 값은 포함x, last는 n-1부터 1까지
        k=0 #이번 구간의 첫 번째 element를 MAAX 후보로 정한다. 새로운 구간을 확인할 떄마다 K=0으로 다시 시작한다. 
        for i in range(1,last+1): #i는 1부터 last까지
            if A[i]>A[k]: # ex) A[1]>A[0]이면 MAX후보를 A[1]로 변경한다.
                k=i #리스트 안의 눵소를 이동하는게 아니라 MAX의 index를 표시한다.
        A[k],A[last]=A[last],A[k] #이제 A[last]와 MAX를 교환한다. 이러면 0부터 n-1까지의 element중 MAX는 A[n-1]로 이동하고 다음에는 다시 0부터 n-2까지의 element중 MAX를 찾고 A[n-2]로 이동시킨다. 이런 식으로 계속하다보면 오름차순으로 정렬된다.