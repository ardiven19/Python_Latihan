import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Kelas untuk Buku dan Sistem Rekomendasi
class BookRecommendationSystem:
    def __init__(self):
        self.graph = {}
        self.network_graph = nx.Graph()  # Membuat graph untuk visualisasi
        self.rating_heap = []  # Heap untuk menyimpan buku berdasarkan rating
        self.trie = Trie()  # Trie untuk pencarian judul

    def add_book(self, book_id, title, genres, author, rating=0):
        """
        Menambahkan buku baru ke dalam sistem dan melakukan update pada graph, heap, dan trie.
        """
        self.graph[book_id] = {
            'title': title,
            'genres': genres,
            'author': author,
            'rating': rating,
            'related_books': []
        }
        self.network_graph.add_node(book_id, label=title)

        # Menambahkan buku ke dalam heap (rating tertinggi akan muncul pertama)
        heapq.heappush(self.rating_heap, (-rating, book_id))  # Kita negasikan rating untuk heap max-heap

        # Menambahkan buku ke dalam Trie untuk pencarian judul
        self.trie.insert(title, book_id)

        # Menambahkan relasi otomatis berdasarkan genre dan penulis
        for other_book_id, other_book in self.graph.items():
            if other_book_id != book_id:
                if set(other_book['genres']).intersection(set(genres)):
                    self.add_relation(book_id, other_book_id)
                if other_book['author'] == author:
                    self.add_relation(book_id, other_book_id)

    def add_relation(self, book_id_1, book_id_2):
        """
        Menambahkan relasi antar buku berdasarkan genre atau penulis yang sama.
        """
        if book_id_2 not in self.graph[book_id_1]['related_books']:
            self.graph[book_id_1]['related_books'].append(book_id_2)
        if book_id_1 not in self.graph[book_id_2]['related_books']:
            self.graph[book_id_2]['related_books'].append(book_id_1)
        self.network_graph.add_edge(book_id_1, book_id_2)

    def get_top_rated_books(self, n=3):
        """
        Mengambil n buku teratas berdasarkan rating menggunakan heap.
        """
        top_books = []
        for _ in range(n):
            if self.rating_heap:
                rating, book_id = heapq.heappop(self.rating_heap)
                top_books.append((self.graph[book_id]['title'], -rating))
        return top_books

    def search_book_by_title(self, prefix):
        """
        Mencari buku berdasarkan awalan judul menggunakan Trie.
        """
        return self.trie.search(prefix)

    def plot_graph(self):
        """
        Menampilkan visualisasi graph relasi buku.
        """
        labels = nx.get_node_attributes(self.network_graph, 'label')
        pos = nx.spring_layout(self.network_graph)
        nx.draw(self.network_graph, pos, with_labels=True, labels=labels, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
        plt.title("Graph Relasi Buku")
        plt.show()

    def plot_trie(self):
        """
        Menampilkan visualisasi pohon Trie untuk pencarian judul.
        """
        fig, ax = plt.subplots(figsize=(12, 12))
        self.trie.plot_tree(ax)
        plt.title("Visualisasi Pohon Trie")
        plt.show()

# Kelas Trie untuk pencarian judul
class TrieNode:
    def __init__(self):
        self.children = {}
        self.book_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title, book_id):
        """
        Menambahkan judul buku ke dalam Trie (case insensitive).
        """
        title = title.lower()  # Ubah judul menjadi huruf kecil
        node = self.root
        for char in title:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Tambahkan book_id pada setiap node yang terlibat dalam awalan
            node.book_ids.append(book_id)
        print(f"Inserted: {title} with book_id {book_id}")  # Debugging output

    def search(self, prefix):
        """
        Mencari buku berdasarkan awalan judul (case insensitive).
        """
        prefix = prefix.lower()  # Ubah prefix menjadi huruf kecil
        node = self.root
        for char in prefix:
            if char not in node.children:
                print(f"Prefix '{prefix}' not found at character '{char}'")  # Debugging output
                return []  # Tidak ditemukan
            node = node.children[char]
        print(f"Found books for prefix '{prefix}': {node.book_ids}")  # Debugging output
        return node.book_ids


    def plot_tree(self, ax, parent=None, level=0, pos=None, width=2., vert_gap=0.4, xcenter=0.5):
        """
        Fungsi rekursif untuk menggambar pohon Trie.
        """
        if pos is None:
            pos = {self.root: (xcenter, 1 - level * vert_gap)}

        # Plot root
        ax.text(xcenter, 1 - level * vert_gap, '<root>', horizontalalignment='center', verticalalignment='center', fontsize=12, color="blue")

        # Plot anak-anak Trie
        for i, (char, child_node) in enumerate(self.root.children.items()):
            child_pos = (xcenter - width / 2 + i * width / (len(self.root.children) or 1), 1 - (level + 1) * vert_gap)
            pos[child_node] = child_pos
            ax.text(child_pos[0], child_pos[1], char, horizontalalignment='center', verticalalignment='center', fontsize=12, color="green")
            ax.plot([xcenter, child_pos[0]], [1 - level * vert_gap, child_pos[1]], color="gray", lw=1)

            # Rekursi untuk anak Trie
            self._plot_children(child_node, ax, level + 1, pos, width / 2, vert_gap, child_pos[0])

    def _plot_children(self, node, ax, level, pos, width, vert_gap, xcenter):
        """
        Fungsi untuk menggambar anak-anak node Trie secara rekursif.
        """
        for i, (char, child_node) in enumerate(node.children.items()):
            child_pos = (xcenter - width / 2 + i * width / (len(node.children) or 1), 1 - (level + 1) * vert_gap)
            pos[child_node] = child_pos
            ax.text(child_pos[0], child_pos[1], char, horizontalalignment='center', verticalalignment='center', fontsize=12, color="green")
            ax.plot([xcenter, child_pos[0]], [1 - level * vert_gap, child_pos[1]], color="gray", lw=1)

            # Rekursi untuk anak Trie
            self._plot_children(child_node, ax, level + 1, pos, width / 2, vert_gap, child_pos[0])


# Membuat sistem rekomendasi buku
system = BookRecommendationSystem()

# Menambahkan buku-buku ke dalam sistem dengan lebih dari satu genre dan rating
system.add_book(1, "The Hobbit", ["Fantasy", "Adventure"], "J.R.R. Tolkien", 4.8)
system.add_book(2, "The Fellowship of the Ring", ["Fantasy", "Adventure"], "J.R.R. Tolkien", 4.9)
system.add_book(3, "Harry Potter and the Sorcerer's Stone", ["Fantasy", "Magic"], "J.K. Rowling", 4.7)
system.add_book(4, "To Kill a Mockingbird", ["Fiction", "Drama"], "Harper Lee", 4.5)
system.add_book(5, "The Two Towers", ["Fantasy", "Adventure"], "J.R.R. Tolkien", 4.6)
system.add_book(6, "The Prisoner of Azkaban", ["Fantasy", "Magic"], "J.K. Rowling", 4.8)

# Mendapatkan 3 buku teratas berdasarkan rating
def main_menu():
    """
    Menampilkan menu utama dan menjalankan loop untuk mengakses sistem rekomendasi buku.
    """

    while True:
        print("\n=== Sistem Rekomendasi Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Top Buku Berdasarkan Rating")
        print("3. Cari Buku Berdasarkan Awalan Judul")
        print("4. Tampilkan Graph Relasi Buku")
        print("5. Tampilkan Visualisasi Trie")
        print("6. Rekomendasi Buku Berdasarkan Judul")
        print("7. Keluar")

        choice = input("Pilih menu (1-7): ")
        if choice == "1":
            # Tambah Buku
            try:
                book_id = int(input("Masukkan ID Buku (angka): "))
                title = input("Masukkan Judul Buku: ")
                genres = input("Masukkan Genre Buku (pisahkan dengan koma): ").split(",")
                author = input("Masukkan Penulis Buku: ")
                rating = float(input("Masukkan Rating Buku (0-5): "))
                system.add_book(book_id, title.strip(), [g.strip() for g in genres], author.strip(), rating)
                print(f"Buku '{title}' berhasil ditambahkan!")
            except ValueError:
                print("Input tidak valid. Pastikan ID berupa angka dan rating berupa angka desimal.")

        elif choice == "2":
            # Lihat Buku Teratas Berdasarkan Rating
            try:
                n = int(input("Berapa buku teratas yang ingin ditampilkan? "))
                top_books = system.get_top_rated_books(n)
                print(f"\nTop {n} Buku Berdasarkan Rating:")
                for title, rating in top_books:
                    print(f"- {title} (Rating: {rating})")
            except ValueError:
                print("Input tidak valid. Pastikan jumlah buku berupa angka.")

        elif choice == "3":
            # Cari Buku Berdasarkan Awalan Judul
            prefix = input("Masukkan awalan judul buku: ")
            book_ids = system.search_book_by_title(prefix)
            if book_ids:
                print("\nBuku yang ditemukan:")
                for book_id in book_ids:
                    print(f"- {system.graph[book_id]['title']} (Rating: {system.graph[book_id]['rating']})")
            else:
                print("Tidak ada buku yang cocok dengan awalan tersebut.")

        elif choice == "4":
            # Tampilkan Graph Relasi Buku
            print("Menampilkan Graph Relasi Buku...")
            system.plot_graph()

        elif choice == "5":
            # Tampilkan Visualisasi Trie
            print("Menampilkan Visualisasi Trie...")
            system.plot_trie()

        elif choice == "6":
            # Rekomendasi Buku Berdasarkan Judul
            prefix = input("Masukkan judul buku atau awalan untuk mendapatkan rekomendasi: ").strip()
            book_ids = system.search_book_by_title(prefix)

            if not book_ids:
                print("Tidak ada buku yang cocok dengan awalan tersebut.")
            elif len(book_ids) == 1:
                # Hanya satu buku ditemukan
                book_id = book_ids[0]
                print(f"Buku utama: {system.graph[book_id]['title']}")
                print("Buku yang direkomendasikan berdasarkan relasi:")
                related_books = system.graph[book_id]['related_books']
                if related_books:
                    for rel_id in related_books:
                        book = system.graph[rel_id]
                        print(f"- {book['title']} (Rating: {book['rating']}, Penulis: {book['author']})")
                else:
                    print("Tidak ada buku yang memiliki relasi dengan buku ini.")
            else:
                # Lebih dari satu buku ditemukan, konfirmasi dengan user
                print("\nBeberapa buku ditemukan dengan awalan tersebut:")
                for i, book_id in enumerate(book_ids, start=1):
                    book = system.graph[book_id]
                    print(f"{i}. {book['title']} (Rating: {book['rating']}, Penulis: {book['author']})")

                try:
                    choice = int(input("Pilih nomor buku yang dimaksud: "))
                    if 1 <= choice <= len(book_ids):
                        selected_book_id = book_ids[choice - 1]
                        print(f"Buku utama: {system.graph[selected_book_id]['title']}")
                        print("Buku yang direkomendasikan berdasarkan relasi:")
                        related_books = system.graph[selected_book_id]['related_books']
                        if related_books:
                            for rel_id in related_books:
                                book = system.graph[rel_id]
                                print(f"- {book['title']} (Rating: {book['rating']}, Penulis: {book['author']})")
                        else:
                            print("Tidak ada buku yang memiliki relasi dengan buku ini.")
                    else:
                        print("Pilihan tidak valid.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")

        elif choice == "7":
            # Keluar
            print("Keluar dari sistem. Terima kasih telah menggunakan sistem rekomendasi buku!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


# Menjalankan menu utama
main_menu()     

