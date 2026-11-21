def bubble_sort2(A):
    n=len(A)

    for last in range(n-1,0,-1):
        is_sorted=True #일단 정렬돼있따고 가정한다=> is_sorted=True, 매 pass마다 true로 초기화한다.
        for i in range(last):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                is_sorted=False #만악 교환을 했다면 앞에서 했던 가정이 틀렸다는 뜻이므로 is_sorted를 False로 바꾼다.

        if is_sorted: #is_sorted가 true라면 함수를 종료한다. 교환을 했더라면 is_sorted가 false라서 함수가 죵료x, 만약 해당 pass에서 교환이 없었더라면 is_sorted가 ture하서 바로 함수가 종료될 것이다
            return        

