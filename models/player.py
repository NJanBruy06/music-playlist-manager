from enum import Enum, auto
from data_structures.doubly_linked_list import DoublyLinkedList
from models.playlist import Playlist
from algorithms.search import linear_search
from algorithms.sort import sort_playlist
from algorithms.shuffle import fisher_yates_shuffle, restore_order

class RepeatMode(Enum):
    NONE = auto()
    ONE  = auto()
    ALL  = auto()


class Player:
    def __init__(self, playlist_info=None):
        self.playlist_info  = playlist_info or Playlist()
        self.songs          = DoublyLinkedList()
        self.current        = None
        self.repeat_mode    = RepeatMode.NONE
        self.is_shuffled    = False
        self._original_order = []
        self._observers     = []

    def add_observer(self, callback):
        self._observers.append(callback)

    def _notify(self):
        for callback in self._observers:
            callback()

    def add_song(self, song):
        node = self.songs.append(song)
        if self.is_shuffled:
            self._original_order.append(node)
        self._notify()
        return node

    def remove_song(self, node):
        if self.current is node:
            self.current = node.next or node.prev
            if self.current is node:
                self.current = None

        if node in self._original_order:
            self._original_order.remove(node)

        song = self.songs.delete(node)
        self._notify()
        return song

    def edit_song(self, node, title=None, artist=None, duration=None, genre=None, year=None):
        if title    is not None: node.data.title    = title
        if artist   is not None: node.data.artist   = artist
        if duration is not None: node.data.duration = duration
        if genre    is not None: node.data.genre    = genre
        if year     is not None: node.data.year     = year
        self._notify()

    def play(self, node):
        self.current = node
        self._notify()

    def next_song(self):
        if self.current is None:
            self.current = self.songs.head
            self._notify()
            return self.current

        if self.repeat_mode == RepeatMode.ONE:
            self._notify()
            return self.current

        if self.current.next is not None:
            self.current = self.current.next
        elif self.repeat_mode == RepeatMode.ALL:
            self.current = self.songs.head
        else:
            self.current = None

        self._notify()
        return self.current

    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

        self._notify()
        return self.current

    def toggle_shuffle(self):
        if not self.is_shuffled:
            self._original_order = self.songs.to_list()
            fisher_yates_shuffle(self.songs)
            self.is_shuffled = True
        else:
            if self._original_order:
                restore_order(self.songs, self._original_order)
            self._original_order = []
            self.is_shuffled = False

        self._notify()
        return self.is_shuffled

    def toggle_repeat(self):
        if self.repeat_mode == RepeatMode.NONE:
            self.repeat_mode = RepeatMode.ONE
        elif self.repeat_mode == RepeatMode.ONE:
            self.repeat_mode = RepeatMode.ALL
        else:
            self.repeat_mode = RepeatMode.NONE

        self._notify()
        return self.repeat_mode

    def search(self, keyword, field="title"):
        return linear_search(self.songs, keyword, field)

    def sort(self, key="title", algorithm="merge"):
        result = sort_playlist(self.songs, key, algorithm)
        self.is_shuffled = False
        self._original_order = []
        self._notify()
        return result

    @property
    def total_songs(self):
        return len(self.songs)

    @property
    def total_duration(self):
        return sum(node.data.duration for node in self.songs)

    @property
    def total_duration_str(self):
        total_sec = self.total_duration
        h = total_sec // 3600
        m = (total_sec % 3600) // 60
        s = total_sec % 60
        if h > 0:
            return f"{h}:{m:02d}:{s:02d}"
        return f"{m}:{s:02d}"

    @property
    def current_song(self):
        return self.current.data if self.current else None

    @property
    def repeat_mode_str(self):
        labels = {
            RepeatMode.NONE: "Không lặp",
            RepeatMode.ONE:  "Lặp 1 bài",
            RepeatMode.ALL:  "Lặp toàn bộ",
        }
        return labels[self.repeat_mode]

    def __repr__(self):
        return (f"Player(playlist='{self.playlist_info.name}', "
                f"songs={self.total_songs}, "
                f"current='{self.current_song}', "
                f"repeat={self.repeat_mode.name}, "
                f"shuffled={self.is_shuffled})")
