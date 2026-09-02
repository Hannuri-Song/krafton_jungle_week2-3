"""
[정수론 - 최대공약수(GCD)와 최소공배수(LCM)]

문제 설명:
- 두 정수의 최대공약수(GCD)와 최소공배수(LCM)를 구합니다.
- 유클리드 호제법을 사용하여 GCD를 효율적으로 계산합니다.
- GCD를 이용하여 LCM을 계산합니다.

입력:
- a, b: 두 개의 양의 정수

출력:
- GCD: 최대공약수
- LCM: 최소공배수

예제:
입력: a = 48, b = 18
출력: 
  GCD = 6
  LCM = 144

힌트:
- 유클리드 호제법: gcd(a, b) = gcd(b, a % b)
- LCM 공식: lcm(a, b) = (a × b) / gcd(a, b)
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """

    """
    if b == 0:
        return a

    if a/b > 1:
        if a%b == 0:
            return b
        elif a%b != 0:
            return gcd(b,a%b)

    elif a/b < 1:
        a, b = b, a
        return gcd(a,b)
    """
        
    """
    1. a/b > 1은 필요 없다
    애초에 뭐가 큰 지 고려할 필요가 없음 알아서 큰 수랑 작은 수랑 위치가 바뀜

    2. 중요한건 % (나머지)

    따라서 Line 39~50은 아래와 같이 간단하게 바꿀 수 있음
    """
    if b == 0: # base case
        return a
    
    return gcd(b, a%b) # recursive
    
    # TODO: 유클리드 호제법 구현
    # base case: b가 0이면 a 반환
    # recursive를 이용 
    pass

def gcd_iterative(a, b):

    for _ in range(max(a,b)):
        if b == 0:
            return a
        a,b = b, a%b
    return a

    """
    for 문은 보통 몇 번 반복할 지 알고 있을 때 사용하는데,
    GCD는 몇 번 반복할지 알 필요가 없음
    다만 b가 0이 될 때까지 반복하기만 하면 되기 때문에
    while문을 써서 아래와 같이 하면 더 자연스러움:
    
    while b != 0:
        a,b = b, a%b
    return a
    """

    """
    반복문을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """
    # TODO: 반복문으로 구현
    # b가 0이 될 때까지 반복
    pass

def lcm(a, b):
    """
    최소공배수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최소공배수
    """
    # TODO: LCM 계산
    # //는 몫이 반영되니까 아래와 같이 쓰는 편이 깔끔함:
    return a*b // gcd(a,b)
    # return int(a * b / gcd(a,b))
    pass

def extended_gcd(a, b):
    """
    확장 유클리드 호제법
    ax + by = gcd(a, b)를 만족하는 x, y를 찾음
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        (gcd, x, y) 튜플
    """
    # TODO: 확장 유클리드 호제법 구현
    # base case: b가 0이면 (a, 1, 0) 반환    
    # recursive case
    # 역추적하며 x, y 계산
    if b == 0:
        return (a, 1, 0) # base case. b가 0이면, x=1, y=0을 의미

    g, x1, y1 = extended_gcd(b, a % b) # gcd(a,b) = gcd(b, a%b)를 이용

    x = y1 # 역추적하며 y 계산
    y = x1 - (a // b) * y1 # a%b = a - (a//b) % b 활용

    return g, x, y
    
    pass

def is_prime(n):
    """
    소수 판별
    
    Args:
        n: 판별할 양의 정수
    
    Returns:
        소수이면 True, 아니면 False
    """
    # TODO: 소수 판별 구현
    # n이 2보다 작으면 False
    # 2부터 sqrt(n)까지 나누어 떨어지는지 확인    
    # 3부터 sqrt(n)까지 홀수만 확인
    pass
    n < 2 == False
    def sqrt(n):
        for a in range(1, n+1):

            if a*a >= n:
                return a
            """
            if a* a > n:
                return int(a)
            if a*a == n:
                return a
            """

    t = sqrt(n)
            
    if n>=2:
        if n == 2:
            return True
        elif n%2 == 0:
            return False

    for a in range(2, t+1, 2):
        n%a != 0
        return True

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")


