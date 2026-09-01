"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    n = len(matrix)
    rotated = []
    for _ in range(n): # n번 반복하겠다. _는 반복 횟수 자체가 필요 없을 때 관습적으로 넣음
        row = [] # 반복할 때마다 새로운 빈 리스트 생성 -> 회전된 배열의 한 줄을 의미

        for _ in range(len(matrix[0])): #matrix[0]은 매트릭스 배열의 첫째 행을 의미
                                        #len(matrix[0])은 결국 첫째 행의 길이니까 그만큼 반복
            row.append(0)               # 반복 횟수만큼 0을 row 배열에 추가
        rotated.append(row)             # row 배열을 rotated에 추가
    #리스트 컴프리헨션으로 처리 한다면:
    # rotated = [[0] * n for _ in range(n)]
    # Line 37~42의 코딩을 단 한줄로 구현 가능

    #여기서부터 회전 로직
    for i in range(n):
        for j in range(len(matrix[0])): #len(matrix[0]) = n도 같은 의미
            rotated[j][n-1-i] = matrix[i][j] # 회전 구현의 핵심


    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """

    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
    pass
        
    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동
    pass
    return rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


