import random
import copy

# 학생 정보 생성 함수
def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))  # 이름
        age = random.randint(18, 22)  # 나이
        score = random.randint(0, 100)  # 성적
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬 구현
def selection_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if (data[j][key] < data[target_idx][key]) != reverse:
                target_idx = j
        data[i], data[target_idx] = data[target_idx], data[i]

# 삽입 정렬 구현
def insertion_sort(data, key, reverse=False):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and (data[j][key] > temp[key]) != reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp

# 퀵 정렬 구현
def quick_sort(data, key, reverse=False):
    if len(data) <= 1:
        return data

    pivot = data[0]
    less = [item for item in data[1:] if (item[key] < pivot[key]) != reverse]
    equal = [item for item in data if item[key] == pivot[key]]
    greater = [item for item in data[1:] if (item[key] > pivot[key]) == reverse]

    return quick_sort(less, key, reverse) + equal + quick_sort(greater, key, reverse)

# 기수 정렬 구현 (성적 기준으로만 사용)
def radix_sort(data, reverse=False):
    max_score = max(item["성적"] for item in data)
    exp = 1
    while max_score // exp > 0:
        counting_sort(data, exp, reverse)
        exp *= 10

def counting_sort(data, exp, reverse):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for item in data:
        index = (item["성적"] // exp) % 10
        count[index] += 1

    if reverse:  # 내림차순
        for i in range(8, -1, -1):
            count[i] += count[i + 1]
    else:  # 오름차순
        for i in range(1, 10):
            count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (data[i]["성적"] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]

# 메인 함수
def main():
    students = generate_students()
    print("\n생성된 학생 정보:")
    for student in students:
        print(student)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        choice = input("선택: ")
        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key_map = {"1": "이름", "2": "나이", "3": "성적"}
        if choice not in key_map:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        key = key_map[choice]

        print("정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만 가능)")
        algo_choice = input("선택: ")

        print("정렬 방식 선택:")
        print("1. 오름차순")
        print("2. 내림차순")
        order_choice = input("선택: ")
        reverse = order_choice == "2"

        temp_students = copy.deepcopy(students)  # 원본 데이터 유지
        if algo_choice == "1":
            selection_sort(temp_students, key, reverse)
        elif algo_choice == "2":
            insertion_sort(temp_students, key, reverse)
        elif algo_choice == "3":
            temp_students = quick_sort(temp_students, key, reverse)
        elif algo_choice == "4" and key == "성적":
            radix_sort(temp_students, reverse)
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        print("\n생성된 학생 정보:")
        for student in temp_students:
            print(student)

if __name__ == "__main__":
    main()