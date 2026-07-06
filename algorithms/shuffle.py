import random

class Shuffle:

    # Kiểm tra playlist có rỗng không
    
    @staticmethod
    def is_empty(head):
        
        return head is None

    # Đếm số lượng bài hát
    @staticmethod
    def count_song(head):
        """
        Đếm số lượng bài hát trong playlist.
        """

        count = 0
        current = head

        while current is not None:
            count += 1
            current = current.next

        return count
    
    @staticmethod
    def can_shuffle(head):
        

        return Shuffle.count_song(head) >= 2

    # Chuyển Linked List sang List
    @staticmethod
    def linked_list_to_list(head):

        songs = []

        current = head

        while current is not None:
            songs.append(current.song)
            current = current.next

        return songs
   
    # Ghi List trở lại Linked List
    
    @staticmethod
    def list_to_linked_list(head, songs):
        """
        Cập nhật lại dữ liệu sau khi shuffle.
        """

        current = head
        index = 0

        while current is not None:

            current.song = songs[index]

            current = current.next
            index += 1

    # Thuật toán Fisher-Yates Shuffle
    @staticmethod
    def fisher_yates_shuffle(song_list):

        n = len(song_list)

        for i in range(n - 1, 0, -1):

            # Sinh ngẫu nhiên vị trí cần đổi
            j = random.randint(0, i)

            # Hoán đổi
            song_list[i], song_list[j] = song_list[j], song_list[i]

        return song_list
        
    # Shuffle Playlist
    @staticmethod
    def shuffle_playlist(head):

        if Shuffle.is_empty(head):

            print("Playlist đang rỗng.")

            return head

        if not Shuffle.can_shuffle(head):

            print("Playlist phải có ít nhất 2 bài hát.")

            return head

        songs = Shuffle.linked_list_to_list(head)

        Shuffle.fisher_yates_shuffle(songs)

        Shuffle.list_to_linked_list(head, songs)

        return head

    # Lấy ngẫu nhiên một bài hát
    @staticmethod
    def random_song(head):

        if Shuffle.is_empty(head):
            return None

        songs = Shuffle.linked_list_to_list(head)

        return random.choice(songs)

    # Hiển thị Playlist
    @staticmethod
    def display_playlist(head):
        
        if Shuffle.is_empty(head):

            print("\nPlaylist đang rỗng.\n")

            return

        print("\n========== PLAYLIST ==========\n")

        current = head
        index = 1

        while current is not None:

            song = current.song

            print(
                f"{index}. "
                f"{song.title} - "
                f"{song.artist}"
            )

            current = current.next
            index += 1

        print("\n==============================")
    # Kiểm tra thứ tự playlist có thay đổi không
    @staticmethod
    def is_shuffled(before, after):
        """
        So sánh hai playlist.

        Returns
        -------
        bool
        """

        if len(before) != len(after):
            return False

        for i in range(len(before)):

            if before[i] != after[i]:
                return True

        return False
