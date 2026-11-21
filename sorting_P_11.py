def insertion_sort(A):
    n=len(A) 

    for i in range(1,n): #i는 1부터 n-1까지
        newitem=A[i] #A[1]부터 삽입할 위치를 찾기 시작한다. 삽입할 값을 따로 보관한다. 
        j=i-1 # 정렬된 앞부분의 index부터 확인한다.
        
        while j>=0 and newitem < A[j]: #리스트의 왼쪽경계를 벗어나지 않고 newitem보다 정렬된 리스트의 맨 오른쪽 부분이 더 크다면
            A[j+1]=A[j] #맨 오른쪽 부분을 오른쪽으로 한 칸 옯긴다.
            j-=1 #newitem과 바교대상을 왼쪽 한칸 옯긴다.
        A[j+1]=newitem #반복이 끝나면 확보한 자리에 newitem을 넣는다.