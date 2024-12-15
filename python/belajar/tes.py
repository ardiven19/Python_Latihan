import matplotlib.pyplot as plt
import networkx as nx

courses = {
    "Matematika 1": {"dosen": "Dr. A", "ruangan": "101", "waktu": ["Senin 08:00-10:00", "Rabu 10:00-12:00"]},
    "Fisika 2": {"dosen": "Dr. B", "ruangan": "202", "waktu": ["Selasa 10:00-12:00", "Kamis 08:00-10:00"]},
    "Kimia 1": {"dosen": "Dr. C", "ruangan": "103", "waktu": ["Senin 10:00-12:00", "Rabu 08:00-10:00"]},
    "Biologi 1": {"dosen": "Dr. D", "ruangan": "104", "waktu": ["Selasa 08:00-10:00", "Kamis 9:00-12:00"]},

    # Data tambahan dengan tabrakan jadwal
    "Statistika": {"dosen": "Dr. E", "ruangan": "105", "waktu": ["Rabu 10:00-13:00"]},  # Tabrakan dengan "Matematika 1"
    "Komputer Dasar": {"dosen": "Dr. F", "ruangan": "106", "waktu": ["Selasa 10:00-12:00"]},  # Tabrakan dengan "Fisika 2"
    "Ekonomi": {"dosen": "Dr. G", "ruangan": "107", "waktu": ["Senin 09:00-11:00"]},  # Tabrakan dengan "Matematika 1"
    "Sejarah": {"dosen": "Dr. H", "ruangan": "108", "waktu": ["Kamis 09:00-11:00"]}  # Tabrakan dengan "Fisika 2"
}

def parse_time_range(time_range):
    day, hours = time_range.split(" ")
    start, end = hours.split("-")
    start_hour, start_minute = map(int, start.split(":"))
    end_hour, end_minute = map(int, end.split(":"))
    return day, (start_hour * 60 + start_minute, end_hour * 60 + end_minute)

def has_overlap(time1, time2):
    day1, (start1, end1) = parse_time_range(time1)
    day2, (start2, end2) = parse_time_range(time2)
    if day1 != day2:
        return False
    return not (end1 <= start2 or end2 <= start1)

def detect_conflicts(courses):
    conflict_graph = {}
    course_names = list(courses.keys())
    for course in course_names:
        conflict_graph[course] = set()

    for i in range(len(course_names)):
        for j in range(i + 1, len(course_names)):
            course1 = course_names[i]
            course2 = course_names[j]
            for time1 in courses[course1]["waktu"]:
                for time2 in courses[course2]["waktu"]:
                    if has_overlap(time1, time2):
                        conflict_graph[course1].add(course2)
                        conflict_graph[course2].add(course1)
    return conflict_graph


# Simulasi penambahan mata kuliah
def simulate_add_course(new_course, courses, conflict_graph):
    # Cek apakah mata kuliah baru ada di data
    if new_course not in courses:
        return f"Mata kuliah {new_course} tidak ditemukan!"

    # Cek konflik dengan graph
    conflicts = []
    for course in conflict_graph.get(new_course, []):
        conflicts.append(course)

    # Jika ada konflik
    if conflicts:
        print(f"Mata kuliah {new_course} memiliki konflik dengan: {', '.join(conflicts)}")
        print("Pilihan:")
        print("1. Hapus salah satu mata kuliah yang bertabrakan")
        print("2. Jadwalkan ulang salah satu mata kuliah")
        print("3. Batalkan penambahan mata kuliah")
        choice = input("Pilih opsi (1/2/3): ")
        if choice == "1":
            remove_course = input(f"Masukkan mata kuliah yang ingin dihapus dari {', '.join(conflicts)}: ")
            if remove_course in courses:
                del courses[remove_course]
                print(f"Mata kuliah {remove_course} dihapus.")
            else:
                print(f"Mata kuliah {remove_course} tidak ditemukan.")
        elif choice == "2":
            print("Fitur penjadwalan ulang belum diimplementasikan.")
        elif choice == "3":
            return "Simulasi dibatalkan."
    else:
        print(f"Tidak ada konflik! Mata kuliah {new_course} berhasil ditambahkan.")

    # Konfirmasi penambahan
    confirm = input(f"Konfirmasi penambahan mata kuliah {new_course}? (y/n): ")
    if confirm.lower() == "y":
        courses[new_course] = {
            "dosen": "Dr. X", "ruangan": "999", "waktu": ["Jumat 10:00-12:00"]
        }
        print(f"Mata kuliah {new_course} berhasil ditambahkan.")
    else:
        print("Penambahan mata kuliah dibatalkan.")
    return courses


conflict_graph = detect_conflicts(courses)
for course, conflicts in conflict_graph.items():
    if conflicts:
        print(f"{course} bertabrakan dengan: {', '.join(conflicts)}")


# Membuat graph menggunakan NetworkX
G = nx.Graph()
for course, conflicts in conflict_graph.items():
    for conflict in conflicts:
        G.add_edge(course, conflict)

# Mengatur layout untuk visualisasi
pos = nx.spring_layout(G, seed=42)

# Plot graph
plt.figure(figsize=(10, 6))
nx.draw(
    G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold"
)
plt.title("Conflict Graph of Courses", fontsize=14)
plt.show()
