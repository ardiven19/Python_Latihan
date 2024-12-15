import random
import heapq
import networkx as nx

# Data pelajaran, durasi total per minggu (jam), dan guru
subjects = {
    "Matematika": {"durasi": 6, "guru": "Ibu A"},
    "IPA": {"durasi": 6, "guru": "Bapak B"},
    "IPS": {"durasi": 6, "guru": "Ibu C"},
    "Bahasa Indonesia": {"durasi": 4, "guru": "Ibu D"},
    "Bahasa Inggris": {"durasi": 4, "guru": "Bapak E"},
    "Penjas": {"durasi": 2, "guru": "Bapak F"},
    "Sejarah": {"durasi": 4, "guru": "Ibu G"},
    "SBK": {"durasi": 4, "guru": "Bapak H"}
}

# Slot waktu per hari (08:00-14:00, 6 jam pelajaran per hari)
schedule_template = {
    "Senin": [None] * 6,
    "Selasa": [None] * 6,
    "Rabu": [None] * 6,
    "Kamis": [None] * 6,
    "Jumat": [None] * 6
}

# Pembatasan waktu pelajaran
subject_time_restrictions = {
    "Penjas": {  # Hanya boleh di jam 3 dan 4 pada hari Rabu dan Jumat
        "Rabu": [2, 3],  # Jam 3 dan 4
        "Jumat": [2, 3]   # Jam 3 dan 4
    }
}

# Fungsi untuk memeriksa apakah slot waktu tersedia (tidak konflik)
def is_slot_available(conflict_graph, day_index, slot, guru, class_name):
    # Memeriksa apakah guru yang sama mengajar di kelas lain pada waktu yang sama
    for other_class_name, other_schedule in conflict_graph.items():
        if other_class_name != class_name and other_schedule[day_index][slot] == guru:
            return False
    return conflict_graph[class_name][day_index][slot] is None

# Fungsi untuk memprioritaskan pelajaran berdasarkan durasi
def prioritize_subjects(subjects):
    subject_heap = []
    for subject, details in subjects.items():
        heapq.heappush(subject_heap, (-details["durasi"], subject))  # Durasi negatif agar yang terbesar diambil dulu
    return subject_heap

# Fungsi untuk memeriksa apakah pelajaran sesuai dengan pembatasan waktu
def is_subject_time_valid(day, slot, subject, subject_time_restrictions):
    if subject in subject_time_restrictions:
        if day in subject_time_restrictions[subject]:
            valid_slots = subject_time_restrictions[subject][day]
            return slot in valid_slots
    return True

# Fungsi untuk membuat jadwal untuk satu kelas dengan menggunakan prioritas
def generate_schedule_with_priority(subjects, schedule_template, conflict_graph, class_name, subject_order):
    # Urutkan mata pelajaran berdasarkan prioritas yang diberikan (subject_order)
    schedule = {day: slots[:] for day, slots in schedule_template.items()}
    subject_hours = {subject: data["durasi"] for subject, data in subjects.items()}
    daily_subject_count = {day: {subject: 0 for subject in subjects} for day in schedule}

    # Loop untuk mengisi jadwal dengan mengikuti urutan yang telah ditentukan
    for day_index, day in enumerate(schedule):
        for slot in range(6):
            for subject in subject_order:
                # Tentukan pelajaran yang tersedia berdasarkan waktu dan guru
                if subject_hours[subject] > 0 and daily_subject_count[day][subject] < 2 and is_slot_available(conflict_graph, day_index, slot, subjects[subject]["guru"], class_name) and is_subject_time_valid(day, slot, subject, subject_time_restrictions):
                    # Alokasikan 2 jam pelajaran secara berurutan
                    if slot + 1 < 6:
                        schedule[day][slot] = subject
                        schedule[day][slot + 1] = subject
                        subject_hours[subject] -= 2
                        daily_subject_count[day][subject] += 2
                        # Perbarui graf konflik
                        conflict_graph[class_name][day_index][slot] = subjects[subject]["guru"]
                        conflict_graph[class_name][day_index][slot + 1] = subjects[subject]["guru"]
                        break

    return schedule

# Fungsi untuk membuat jadwal untuk beberapa kelas
def generate_schedules_for_classes(subjects, schedule_template, num_classes, subject_order):
    schedules = {}
    conflict_graph = {f"Kelas {class_num}": {day_index: [None] * 6 for day_index in range(5)} for class_num in range(1, num_classes + 1)}

    for class_num in range(1, num_classes + 1):
        class_name = f"Kelas {class_num}"
        schedules[class_name] = generate_schedule_with_priority(subjects, schedule_template, conflict_graph, class_name, subject_order)

    return schedules

# Urutan pelajaran (Matematika -> IPA, IPS -> SBK atau Sejarah)
subject_order = ["Matematika", "IPA", "IPS", "Sejarah", "SBK", "Bahasa Indonesia", "Bahasa Inggris", "Penjas"]

# Generate jadwal untuk 3 kelas
final_schedules = generate_schedules_for_classes(subjects, schedule_template, 3, subject_order)

# Menampilkan jadwal untuk setiap kelas
for class_name, schedule in final_schedules.items():
    print(f"\nJadwal untuk {class_name}:")
    for day, slots in schedule.items():
        print(f"  {day}: {slots}")

def build_conflict_graph(final_schedules, subjects):
    G = nx.Graph()  # Membuat graph kosong
    # Menambahkan node untuk setiap kelas
    for class_name in final_schedules.keys():
        G.add_node(class_name)

    # Menambahkan edge jika ada konflik antar kelas
    for class1, schedule1 in final_schedules.items():
        for class2, schedule2 in final_schedules.items():
            if class1 != class2:
                for day in schedule1:
                    for slot in range(6):
                        if schedule1[day][slot] == schedule2[day][slot]:
                            G.add_edge(class1, class2)  # Menambahkan edge jika ada konflik antara dua kelas
    return G
# Membuat graph konflik
conflict_graph = build_conflict_graph(final_schedules, subjects)

# Menampilkan konflik antar kelas
print("\nKonflik antar kelas:")
for edge in conflict_graph.edges():
    print(f"Konflik antara {edge[0]} dan {edge[1]}")