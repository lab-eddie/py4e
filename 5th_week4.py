# Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.

# 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.

# 😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
# 😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
# 🧐hint
# # 특정 원소의 위치를 찾는 방법
# a = [1,2,3,4]
# a.index(1)
# 0
# ✅ 출력 예시
# after_100(6,21,"월")
# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일