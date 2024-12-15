# Fungsi untuk mengecek apakah penempatan ratu valid
def is_valid(queens):
    # queens[i] = kolom tempat ratu di baris i ditempatkan
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j]:  # Cek kolom
                return False
            if abs(i - j) == abs(queens[i] - queens[j]):  # Cek diagonal kiri-ke-kanan
                return False
    return True


# Fungsi untuk mencetak solusi
def print_solution(queens):
    n = len(queens)
    board = [['0' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][queens[i]] = '1'

    for row in board:
        print(' '.join(row))
    print()  # Untuk pemisah antar solusi


# Fungsi brute-force untuk mencari semua solusi n-Queen
def solve_n_queens(n):
    def place_queens(row, queens):
        if row == n:
            if is_valid(queens):
                print_solution(queens)
            return

        # Coba semua kolom untuk baris saat ini
        for col in range(n):
            queens[row] = col
            place_queens(row + 1, queens)

    queens = [-1] * n  # Inisialisasi posisi ratu untuk setiap baris
    place_queens(0, queens)


# Menjalankan fungsi untuk 8-Queen problem
solve_n_queens(8)
