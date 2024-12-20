class Node:  # 단순 연결 리스트를 위한 노드 클래스 
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, node):  # 현재 노드 다음에 node를 삽입
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):  # 현재 노드의 다음 노드를 삭제
        next_node = self.link
        if next_node is not None:
            self.link = next_node.link
        return next_node


class LinkedList:  # 단순 연결 리스트 클래스
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, pos, elem):
        node = Node(elem)
        before = self.getNode(pos - 1)
        if before is None:
            node.link = self.head
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before is None:
            if self.head is not None:
                self.head = self.head.link
        else:
            before.popNext()

    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head
        for i in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def size(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count

    def display(self):  # 현재 등록된 도서 목록 출력
        print("현재 등록된 도서 목록:")
        ptr = self.head
        if ptr is None:
            print("등록된 도서가 없습니다.")
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link

    def find_by_title(self, title):  # 도서 제목으로 책장에서 도서를 찾기
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data  # 제목이 일치하는 도서 반환
            ptr = ptr.link
        return None
        
    def find_pos_by_title(self, title):  # 도서 제목으로 책장에서 도서의 위치(pos)를 찾기
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.data.title == title:
                return pos  # 제목이 일치하는 도서의 위치 반환
            ptr = ptr.link
            pos += 1
        return -1
    
    def find_by_id(self, id):  # 도서 ID로 도서를 찾기 (책 번호 중복 체크)
        ptr = self.head
        while ptr is not None:
            if ptr.data.id == id:
                return ptr.data
            ptr = ptr.link
        return None


class Book:  # 도서의 정보를 저장하는 클래스
    def __init__(self, id, title, writer, year):
        self.id = id  # 책 번호
        self.title = title  # 책 제목
        self.writer = writer  # 저자
        self.year = year  # 출판 연도

    def __str__(self):
        return f"책 번호: {self.id}, 제목: {self.title}, 저자: {self.writer}, 출판 연도: {self.year}"


class BookManagementSystem:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, id, title, writer, year):  # 새로운 도서를 리스트에 추가
        if self.books.find_by_title(title) is None and self.books.find_by_id(id) is None:  # 중복 검사
            book = Book(id, title, writer, year)
            self.books.insert(self.books.size(), book)
            print(f"도서 '{title}'가 추가되었습니다.")
        else:
            print("책 제목 또는 책 번호가 중복되었습니다.")
            return False
        return True

    def remove_book(self, title):  # 주어진 책 제목에 해당하는 도서를 리스트에서 삭제
        pos = self.books.find_pos_by_title(title)
        if pos != -1:
            self.books.delete(pos)
            print(f"도서 '{title}'가 삭제되었습니다.")
        else:
            print("해당 제목의 도서가 없습니다.")

    def search_book(self, title):  # 주어진 책 제목에 해당하는 도서를 리스트에서 조회하고, 해당 도서의 정보를 출력
        book = self.books.find_by_title(title)
        if book is not None:
            print(book)
        else:
            print("해당 제목의 도서가 없습니다.")

    def display_books(self):  # 현재 리스트에 등록된 모든 도서를 출력
        self.books.display()

    def update_book(self, title):  # 도서 정보 수정
        book = self.books.find_by_title(title)
        if book is not None:
            print("현재 도서 정보:")
            print(book)

            while True:
                new_id = input("새 책 번호를 입력하세요 (현재: {}): ".format(book.id))
                if not new_id.isdigit():  # 책 번호가 숫자가 아니면 에러 메시지 출력
                    print("책 번호는 숫자만 입력 가능합니다.")
                    continue
                new_id = int(new_id)  # 책 번호를 숫자로 변환

                # 책 번호 중복 체크
                if self.books.find_by_id(new_id) is not None and new_id != book.id:
                    print("책 번호가 중복됩니다. 다른 번호를 입력하세요.")
                    continue
                break

            while True:
                new_title = input("새 책 제목을 입력하세요 (현재: {}): ".format(book.title)) or book.title
                if self.books.find_by_title(new_title) is not None and new_title != book.title:
                    print("책 제목이 중복됩니다. 다른 제목을 입력하세요.")
                    continue
                break

            new_writer = input("새 저자를 입력하세요 (현재: {}): ".format(book.writer)) or book.writer

            while True:
                try:
                    new_year = int(input("새 출판 연도를 입력하세요 (현재: {}): ".format(book.year)))  # 출판 연도 입력
                    break
                except ValueError:
                    print("출판 연도는 숫자만 입력 가능합니다.")  # 숫자 입력 오류 메시지

            book.id = new_id
            book.title = new_title
            book.writer = new_writer
            book.year = new_year

            print(f"도서 '{title}'의 정보가 수정되었습니다.")
        else:
            print("해당 제목의 도서가 없습니다.")

    def main(self):
        while True:
            print("=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 도서 정보 수정")  # 수정 메뉴 추가
            print("6. 프로그램 종료")

            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                while True:
                    try:
                        id = int(input("책 번호를 입력하세요: "))  # 책 번호는 숫자만 가능
                    except ValueError:
                        print("책 번호는 숫자만 입력 가능합니다.")
                        continue
                    title = input("책 제목을 입력하세요: ")
                    writer = input("저자를 입력하세요: ")
                    while True:
                        try:
                            year = int(input("출판 연도를 입력하세요: "))  # 출판 연도는 숫자만 가능
                            break
                        except ValueError:
                            print("출판 연도는 숫자만 입력 가능합니다.")
                            continue
                    if self.add_book(id, title, writer, year):
                        break

            elif choice == "2":
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)

            elif choice == "3":
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif choice == "4":
                self.display_books()

            elif choice == "5":
                title = input("수정할 책 제목을 입력하세요: ")
                self.update_book(title)

            elif choice == "6":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 선택입니다. 다시 시도하세요.")

# 프로그램 실행
if __name__ == "__main__":
    system = BookManagementSystem()
    system.main()