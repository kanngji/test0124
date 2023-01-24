import csv
import numpy
csv_file = open("sample.csv","r",encoding="ms932",errors="",newline="")

#리스트 형식

# delimiter 필드간을 분할하기 위해 사용하는 문자
# doublequote # 필드 내의 quotechar이 그 문자 자체인 경우 어떻게 인용할가
# escapechar 이스케이프용의 문자열을 지정
# lineterminator writer을 사용할 때에 각 행의 끝을 표시하기 위해 사용
# skipinitialspace true의 경우 delimiter의 직후에 있는 공백은 무시 된다
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
# print(header)
calculated_line=0
error_values=[]
total_lines=0
for row in f:
    total_lines+=1
    # fow는 list
    # row[0]로 필요한 항목을 추출할 수 있다.
    answer=[]
    for val in row:
        # str->숫자로 변환이 되냐?
        if val.isdecimal():
            # int형으로 넣어주기
            answer.append(int(val))
        else:
            # int로 안되면 반복문 탈출 그리고 error_values에 넣기
            error_values.append(val)

            break
    else:
        calculated_line+=1
        mins=numpy.min(answer)
        maxs=numpy.max(answer)
        sums=numpy.sum(answer)
        means=numpy.mean(answer)
        stds=numpy.std(answer)
        medians=numpy.median(answer)
        print(float(mins),float(maxs),sums,means,stds,medians)

print("The total number of lines:", total_lines)
print("The calculated lines", calculated_line)
print("The error values", error_values)

