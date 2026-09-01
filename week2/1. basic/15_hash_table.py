"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 해시 테이블로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)

힌트:
- 딕셔너리 사용
- 평균: sum(scores.values()) / len(scores)
- 최고점: max(scores, key=scores.get)
"""

def manage_grades(students):
    """
    학생 성적 관리 시스템
    
    Args:
        students: {이름: 점수} 딕셔너리
    
    Returns:
        평균, 최고점 학생 이름, 최고점
    """
    # TODO: 평균 점수 계산
    pass
    avg = sum(students.values()) / len(students) #students에서 값만 갖고 오기
    
    # TODO: 최고 점수 학생 찾기
    pass
    """
    top_score = max(students.values())
    for name, score in students.items(): #items()는 키와 값을 같이 가져옴
        if score == top_score:
            top_student = name
    """
    top_student = max(students, key=students.get)
    # students의 key들을 대상으로 max를 찾는데,
    # 각각의 key를 students.get()에 넣어서 나온 값을 기준으로 비교해라.
    top_score = students[top_student]
    
    return avg, top_student, top_score

def find_student_score(students, name):
    """
    특정 학생의 점수 조회
    
    Args:
        students: 학생 딕셔너리
        name: 찾을 학생 이름
    
    Returns:
        점수 (없으면 None)
    """
    # TODO: students에서 name 찾기
    pass
    """
    딕셔너리는 key를 이용해서 바로 value를 찾을 수 있기 때문에 for문을 쓸 필요가 없음
    for key, value in students.items():
        if key == name:
            return students.get(name)
        elif key != name:
            return "None"
    """
    return students.get(name)


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {top_name} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")


