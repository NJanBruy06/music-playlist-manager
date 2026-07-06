class Search:
    @staticmethod
    def is_empty(head):
        return head is None

    @staticmethod
    def search_by_title(head, keyword):
        result = []
        if Search.is_empty(head):
            return result
        keyword = keyword.strip().lower()
        current = head
        while current is not None:
            if keyword in current.data.title.lower():
                result.append(current)
            current = current.next
        return result

    @staticmethod
    def search_by_artist(head, keyword):
        result = []
        if Search.is_empty(head):
            return result
        keyword = keyword.strip().lower()
        current = head
        while current is not None:
            if keyword in current.data.artist.lower():
                result.append(current)
            current = current.next
        return result

    @staticmethod
    def search_by_genre(head, keyword):
        result = []
        if Search.is_empty(head):
            return result
        keyword = keyword.strip().lower()
        current = head
        while current is not None:
            if keyword in current.data.genre.lower():
                result.append(current)
            current = current.next
        return result

    @staticmethod
    def search_by_keyword(head, keyword):
        result = []
        if Search.is_empty(head):
            return result
        keyword = keyword.strip().lower()
        current = head
        while current is not None:
            title = current.data.title.lower()
            artist = current.data.artist.lower()
            if keyword in title or keyword in artist:
                result.append(current)
            current = current.next
        return result

    @staticmethod
    def exists(head, keyword):
        result = Search.search_by_keyword(head, keyword)
        return len(result) > 0

    @staticmethod
    def count_result(result):
        return len(result)

    @staticmethod
    def first_result(result):
        if len(result) == 0:
            return None
        return result[0]

    @staticmethod
    def last_result(result):
        if len(result) == 0:
            return None
        return result[-1]


def linear_search(dll, keyword, field="title"):
    if field == "title":
        return Search.search_by_title(dll.head, keyword)
    elif field == "artist":
        return Search.search_by_artist(dll.head, keyword)
    elif field == "genre":
        return Search.search_by_genre(dll.head, keyword)
    else:
        return Search.search_by_title(dll.head, keyword)
