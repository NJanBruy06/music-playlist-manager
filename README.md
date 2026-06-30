# 🎵 Music Playlist Manager

**Dự án nhóm 5** &nbsp;|&nbsp; **Môn:** Phân Tích Thiết Kế Giải Thuật &nbsp;|&nbsp; **Python:** 3.10+

---

## 🌟 Tính năng

| Tính năng | Mô tả |
|---|---|
| ➕ Quản lý bài hát | Thêm mới, cập nhật, xóa bài hát khỏi danh sách phát |
| 🔍 Tìm kiếm | Tìm bài hát theo tên hoặc ca sĩ (Linear Search) |
| 🔄 Sắp xếp | Sắp xếp playlist theo tên, ca sĩ hoặc thời lượng (Merge Sort, Insertion Sort) |
| 🔀 Trộn & Lặp lại | Hỗ trợ phát ngẫu nhiên (Shuffle) và vòng lặp (Repeat 1 / Repeat All) |
| ⏭️ Hàng đợi & Lịch sử | Chuyển bài (Next), quay lại bài trước (Back) và quản lý Up Next |

---

## 🚀 Cài đặt & Chạy

```bash
# 1. Clone repo
git clone https://github.com/NJanBruy06/music-playlist-manager.git
cd music-playlist-manager

# 2. Chạy ứng dụng
python main.py
```

---

## 📂 Cấu trúc dự án

```text
music-playlist-manager/
├── main.py              ← Điểm khởi động ứng dụng
├── models/              ← Định nghĩa đối tượng (Song, Playlist)
├── data_structures/     ← Các CTDL nền tảng (Linked List, Stack, Queue)
├── algorithms/          ← Các thuật toán (Search, Sort, Shuffle)
└── ui/                  ← Giao diện người dùng (Tkinter GUI)
```

---

## ⚙️ Kiến trúc kỹ thuật

### 1. Cấu trúc dữ liệu
- **Doubly Linked List:** Lưu trữ danh sách bài hát chính, giúp chèn/xóa phần tử ở độ phức tạp $O(1)$ khi biết vị trí và dễ dàng điều hướng Next/Previous.
- **Stack (Ngăn xếp - LIFO):** Quản lý Lịch sử phát nhạc (History). Hỗ trợ tính năng quay lại bài trước (Back).
- **Queue (Hàng đợi - FIFO):** Quản lý danh sách phát tiếp theo (Up Next Queue) được người dùng chỉ định ưu tiên.

### 2. Thuật toán cốt lõi
- **Linear Search:** $O(n)$ - Duyệt tìm kiếm bài hát theo từ khóa.
- **Merge Sort:** $O(n \log n)$ - Áp dụng chia để trị để sắp xếp tối ưu danh sách theo nhiều tiêu chí.
- **Insertion Sort:** $O(n^2)$ - Thuật toán sắp xếp phụ được cài đặt để đối chiếu, so sánh hiệu năng.
- **Fisher-Yates Shuffle:** $O(n)$ - Thuật toán trộn ngẫu nhiên danh sách hoàn hảo.

---

## 💻 Yêu cầu hệ thống

- **Python** 3.10 trở lên
- **Hệ điều hành:** Windows / macOS / Linux
- **Thư viện phụ thuộc:** Không cần cài đặt thư viện ngoài (sử dụng thư viện chuẩn `tkinter` của Python).
