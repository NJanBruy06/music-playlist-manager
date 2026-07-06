class Search:
    
    # Kiểm tra playlist có rỗng hay không
    @staticmethod
    def is_empty(head):

        return head is None

    # Tìm kiếm theo tên bài hát
    @staticmethod
    def search_by_title(head, keyword):

        result = []

        if Search.is_empty(head):
            return result

        keyword = keyword.strip().lower()

        current = head

        while current is not None:

            if keyword in current.song.title.lower():
                result.append(current.song)

            current = current.next

        return result

    # ==========================================================
    # Tìm kiếm theo tên ca sĩ
    # ==========================================================
    @staticmethod
    def search_by_artist(head, keyword):

        result = []

        if Search.is_empty(head):
            return result

        keyword = keyword.strip().lower()

        current = head

        while current is not None:

            if keyword in current.song.artist.lower():
                result.append(current.song)

            current = current.next

        return result

    
    # Tìm kiếm theo từ khóa
    @staticmethod
    def search_by_keyword(head, keyword):

        result = []

        if Search.is_empty(head):
            return result

        keyword = keyword.strip().lower()

        current = head

        while current is not None:

            title = current.song.title.lower()
            artist = current.song.artist.lower()

            if keyword in title or keyword in artist:
                result.append(current.song)

            current = current.next

        return result

    # Kiểm tra bài hát có tồn tại hay không
    @staticmethod
    def exists(head, keyword):
        """
        Trả về True nếu tìm thấy bài hát.
        """

        result = Search.search_by_keyword(head, keyword)

        return len(result) > 0

    # Đếm số lượng kết quả
    @staticmethod
    def count_result(result):

        return len(result)

    # Hiển thị kết quả
    @staticmethod
    def display_result(result):
        

        if len(result) == 0:
            print("\nKhông tìm thấy bài hát.\n")
            return

        print("\n KẾT QUẢ TÌM KIẾM")

        for index, song in enumerate(result, start=1):

            print(
                f"{index}. "
                f"{song.title} - "
                f"{song.artist}"
            )

        print("======================================")

    # Lấy bài hát đầu tiên
    @staticmethod
    def first_result(result):

        if len(result) == 0:
            return None

        return result[0]

    # Lấy bài hát cuối cùng
    @staticmethod
    def last_result(result):

        if len(result) == 0:
            return None

        return result[-1]