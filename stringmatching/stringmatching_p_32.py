def make_kmp_table(pattern):
    m = len(pattern)         #m은 입력받은 패턴의 길이이다. 
    border = [-1] * (m + 1)  #길이 0부터 6까지 기록해야 하므로 총 7칸을 만들고 -1로 초기화한다.

    i = 0   #지금까지 처리한 글자 수이다. pattern[i]는 이번에 새로 확인할 글자이다.
    j = -1  #접두사와 접미사가 겹치는 길이의 후보이다. 처음에는 후보가 없어서 -1이다.

    while i < m:  #아직 패턴에 처리할 글자가 남아 있으면 반복한다.

        #pattern[i]를 새로 붙였을 때 기존의 겹침을 한 글자 늘릴 수 있는지 확인한다.
        #j가 -1이면 첫 번째 조건이 거짓이므로 pattern[j]는 읽지 않는다.
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]  #현재 후보가 실패했으므로 그보다 짧은 겹침의 길이로 이동한다.

        i += 1  #이번 글자까지 처리했으므로 처리한 글자 수를 1 늘린다.
        j += 1  #글자가 일치했다면 겹침이 1 늘어난다. 후보가 없었다면 -1에서 0이 된다.

        border[i] = j  #패턴의 앞 i글자에서 접두사와 접미사가 겹치는 최대 길이를 기록한다.

    return border  #완성된 테이블을 검색 함수에서 사용할 수 있도록 반환한다.

def kmp_search(pattern, border, text):
    m = 0                 #텍스트의 몇 번 인덱스부터 패턴을 맞춰 볼지 나타낸다.
    i = 0                 #패턴에서 다음에 비교할 인덱스이다. 이미 일치한 글자 수도 i이다.
    t_len = len(text)     #입력받은 text의 길이.
    p_len = len(pattern)  #입력받은 pattern의 길이.

    if p_len == 0:  #패턴이 빈 문자열이면 비교할 글자가 없다.
        return 0    #빈 패턴은 모든 위치에서 일치하므로 첫 일치 위치인 0을 반환한다.

    while m + i < t_len:  #다음에 비교할 텍스트 인덱스가 텍스트 범위 안이면 반복한다.

        if pattern[i] == text[m + i]:  #패턴의 i번 글자와 텍스트의 m+i번 글자를 비교한다.

            if i == p_len - 1:  #방금 일치한 글자가 패턴의 마지막 글자인지 확인한다.
                return m        #앞의 i글자도 이미 일치했으므로 패턴의 시작 위치를 반환한다.

            i += 1  #마지막 글자까지 도달하기 전이면 패턴의 다음 글자를 비교한다.

        else:  #pattern[i]와 text[m+i]가 서로 다른 경우이다.

            if border[i] > -1:  #이미 맞은 i글자에서 활용할 겹침의 길이가 0 이상인 경우이다.
                m = m + i - border[i]  #패턴의 시작점을 오른쪽으로 i - border[i]칸 옮긴다.
                i = border[i]          #겹치는 앞부분은 이미 일치하므로 그다음 글자부터 비교한다.

            else:  #이 테이블에서는 border[0]만 -1이다. 즉, 첫 글자부터 다른 경우이다.
                i = 0   #다음 시작점에서도 패턴의 첫 글자부터 비교한다.
                m += 1  #텍스트에서 패턴을 맞춰 볼 시작점을 한 칸 오른쪽으로 옮긴다.

    return -1  #텍스트 끝까지 확인했지만 패턴 전체가 일치하는 위치를 찾지 못했다.

if __name__ == "__main__":
    text = "ABABABAC"    #검색 대상이 되는 전체 문자열이다.
    pattern = "ABABAC"   #텍스트 안에서 찾으려는 문자열이다.

    border = make_kmp_table(pattern)            #먼저 패턴으로 border 테이블을 만든다.
    position = kmp_search(pattern, border, text)  #만든 테이블을 사용해서 패턴을 검색한다.

    print("border 테이블:", border)

    if position != -1:  #검색에 성공하면 시작 인덱스와 실제로 찾은 문자열을 출력한다.
        print("시작 인덱스:", position)
        print("찾은 문자열:", text[position:position + len(pattern)])
    else:
        print("패턴을 찾지 못했습니다.")