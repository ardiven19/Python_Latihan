class BookRecommendationSystem:
    def __init__(self):
        # Inisialisasi graph kosong untuk menyimpan buku dan relasinya
        self.graph = {}

    def add_book(self, book_id, title, genres, author):
        """
        Menambahkan buku baru ke dalam graph dan otomatis membuat relasi dengan buku lain
        yang memiliki genre atau penulis yang sama.
        """
        # Menambahkan buku ke dalam graph
        self.graph[book_id] = {
            'title': title,
            'genres': genres,  # Genre sekarang berupa list
            'author': author,
            'related_books': []  # Buku yang berhubungan
        }

        # Menambahkan relasi otomatis berdasarkan genre dan penulis
        for other_book_id, other_book in self.graph.items():
            if other_book_id != book_id:
                # Cek genre yang sama (jika ada genre yang sama antara dua buku)
                if set(other_book['genres']).intersection(set(genres)):
                    self.add_relation(book_id, other_book_id)
                # Cek penulis yang sama
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

    def get_recommendations(self, book_id):
        """
        Mengambil daftar rekomendasi buku berdasarkan relasi buku yang sudah ada.
        """
        recommendations = []
        for related_book_id in self.graph[book_id]['related_books']:
            recommendations.append(self.graph[related_book_id]['title'])
        return recommendations


# Membuat sistem rekomendasi buku
system = BookRecommendationSystem()

# Menambahkan buku-buku ke dalam sistem dengan lebih dari satu genre
system.add_book(1, "The Hobbit", ["Fantasy", "Adventure"], "J.R.R. Tolkien")
system.add_book(2, "The Fellowship of the Ring", ["Fantasy", "Adventure"], "J.R.R. Tolkien")
system.add_book(3, "Harry Potter and the Sorcerer's Stone", ["Fantasy", "Magic"], "J.K. Rowling")
system.add_book(4, "To Kill a Mockingbird", ["Fiction", "Drama"], "Harper Lee")
system.add_book(5, "The Two Towers", ["Fantasy", "Adventure"], "J.R.R. Tolkien")
system.add_book(6, "The Prisoner of Azkaban", ["Fantasy", "Magic"], "J.K. Rowling")

# Mendapatkan rekomendasi untuk buku dengan ID 1 (The Hobbit)
recommendations = system.get_recommendations(1)

# Menampilkan hasil rekomendasi
print("Rekomendasi untuk 'The Hobbit':")
for book in recommendations:
    print(f"- {book}")
