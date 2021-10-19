import sys

# 16진법으로 출력 (영문 소문자로 출력)
a = sys.stdin.readline().rstrip()
n = int(a)

print("%x"%n)

# 16진법으로 출력 (영문 대문자로 출력)
a = sys.stdin.readline().rstrip()
n = int(a)

print("%X"%n)

# 8진법으로 출력
a = sys.stdin.readline().rstrip()
n = int(a)

print("%o"%n)

# 16진법으로 변환하여 8진법으로 출력
a = sys.stdin.readline().rstrip()
n = int(a, 16)

print("%o"%n)

# 문자를 입력받아 Unicode로 출력
a = ord(sys.stdin.readline().rstrip())

print(a)

# Unicode를 입력받아 문자로 출력
a = int(sys.stdin.readline().rstrip())
print(chr(a))
