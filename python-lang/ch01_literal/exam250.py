# str

# 문자열 저장
# - 문자열을 메모리에 저장할 때 문자열에 포함된 문자 중에서 
#   가장 큰 코드포인트(code point)를 기준으로 
#   문자 코드의 크기가 결정된다.
# - 1(latin-1), 2(utf-16), 4(utf-32) 바이트 중 하나로 결정된다.
# - 코드 포인트? 문자에 부여한 유니 코드 정수 값
import sys

# 1) 영문자만 있을 때, 모든 문자는 Latin-1(1 byte)으로 저장된다.
print(sys.getsizeof("A")) # 예) 42
print(sys.getsizeof("ABC")) # 예) 44, 한 문자 당 1 byte

# 2) 한글이 포함되어 있을 때, 
# - 한글을 기준으로 모든 문자는 UTF-16(2 byte; UCS2)으로 저장된다.
print(sys.getsizeof("가")) # 예) 60
print(sys.getsizeof("가각간")) # 예) 64, 한 문자 당 2 byte
print(sys.getsizeof("가각간ABC")) # 예) 70, 한 문자 당 2 byte

# 3) 한글 보다 더 큰 코드 값을 가진 문자가 포함되어 있을 때,
# - 그 코드 크기를 기준으로 모든 문자 코드가 저장된다.
# - 예) '𝕏' 문자는 2바이트를 초과하기 때문에 
#       무조건 UTF-32(4 byte;UCS4) 으로 저장된다.
print(sys.getsizeof("𝕏")) # 예) 64
print(sys.getsizeof("가각간ABC𝕏")) # 예) 88

# 참고!
# - 문자열 ===> UTF-16
print("AB가각".encode("UTF-16")) # ff fe 41 00 42 00 00 ac 01 ac
print("AB가각".encode("UTF-16BE")) # 00 41 00 42 ac 00 ac 01
print("AB가각".encode("UTF-16LE")) # 41 00 42 00 00 ac 01 ac
print("AB가각".encode("UTF-8")) # 41 42 ea b0 80 ea b0 81