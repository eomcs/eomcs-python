# set
# - 요소의 중복을 허용하지 않는다.

print({}, type({})) # 빈 딕셔너리. 집합이 아니다.
print(set(), type(set())) # 빈 집합
print({1}, type({1})) # 집합
print({1, 2, 3}) # 정수 집합
print({"Hello", "Python"}) # 문자열 집합
print({1, "Hello", 3.14}) #  다양한 타입의 집합
# print({1, {2, 3}, [4, 5]}) # 해시 가능한 객체만 포함될 수 있다.

# 중복된 값을 제거한다.
print({1, 2, 2, 2, 2, 3, 3, 4, 4, 4})