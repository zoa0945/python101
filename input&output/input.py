import sys

# 공백으로 나눠진 입력
a, b = sys.stdin.readline().rstrip().split()

print(a, b)

# 입력받은 값 자료형 변경
a = sys.stdin.readline().rstrip()

print(int(a))
print(float(a))

# 입력받은 값 정수형으로 리스트에 저장
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(arr)
