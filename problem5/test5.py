import urllib.request
from collections import Counter

if __name__ == "__main__":
    answer=[]
    total_count=0
    # 100번 반복하기
    for _ in range(100):
        dict1={}
        req = urllib.request.Request("http://codingtest.brique.kr:8080/random")
        data = urllib.request.urlopen(req).read()
        # 문자열 'b 접두사 없애기
        data = data.decode('utf-8')

        answer.append(data)
    # 많은 빈도수로 정렬하기
    cnt = Counter(answer).most_common()
    for i in cnt:
        print(i[1],i[0])
        # 토탈카운트 더 해주기
        total_count+=i[1]

    print("Total count:",total_count)