"""
[큐 - 프린터 대기열]

문제 설명:
- 큐(Queue)를 사용하여 프린터 작업을 순서대로 처리합니다.
- FIFO (First In First Out) 구조를 활용합니다.

입력:
- jobs: 인쇄 작업 리스트 (예: ["문서A", "문서B", "문서C"])

출력:
- 작업이 처리되는 순서

예제:
입력: ["문서A", "문서B", "문서C"]
출력:
처리: 문서A
처리: 문서B
처리: 문서C

힌트:
- 파이썬에서는 리스트로 큐 구현 가능
- append(): 뒤에 추가 (enqueue)
- pop(0): 앞에서 제거 (dequeue)
"""

from collections import deque

def process_print_queue(jobs):
    """
    프린터 작업을 순서대로 처리
    
    Args:
        jobs: 작업 리스트
    
    Returns:
        처리된 작업 리스트
    """
    # TODO: deque로 큐 생성
    queue = deque(jobs)
    
    processed = []

    """
    아래와 같이 for문을 쓰기 보다는 while문을 쓰는게 더 자연스러움
    큐가 비어 있지 않은 동안 작업을 하나씩 꺼낸다를 요구하기 때문
    deque 자체가 for문으로 순회가 가능하기 때문에 list(queue)를 할 필요가 없다
    list(queue)는 불필요한 복사본
    for a in list(queue):
        print("처리:", a)
        processed.append(a)
        queue.popleft()
        if queue == []:
            return processed
    # TODO: 큐가 비어있지 않은 동안 반복
    ## 큐에서 작업 꺼내기
    ## 작업 처리 (출력 및 리스트에 추가)
    pass
    """
    while queue: #queue가 비어있지 않은 동안 반복해라 라는 뜻
        job = queue.popleft() # 선입선출 구현 부분

        print("처리:", job)
        processed.append(job)

    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    jobs1 = ["문서A", "문서B", "문서C"]
    print("=== 프린터 작업 처리 ===")
    result1 = process_print_queue(jobs1)
    print(f"처리 완료: {result1}")
    print()
    
    # 테스트 케이스 2
    jobs2 = ["이메일", "보고서", "사진", "계약서"]
    print("=== 프린터 작업 처리 ===")
    result2 = process_print_queue(jobs2)
    print(f"처리 완료: {result2}")


