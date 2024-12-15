import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt

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
        "Jumat": [2, 3]  # Jam 3 dan 4
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
def generate_schedule_with_priority(subjects, schedule_template, conflict_graph, class_name):
    # Urutkan mata pelajaran berdasarkan prioritas
    subject_heap = prioritize_subjects(subjects)
    schedule = {day: slots[:] for day, slots in schedule_template.items()}
    subject_hours = {subject: data["durasi"] for subject, data in subjects.items()}
    daily_subject_count = {day: {subject: 0 for subject in subjects} for day in schedule}

    # Loop untuk mengisi jadwal
    for day_index, day in enumerate(schedule):
        for slot in range(6):
            available_subjects = [
                subj for subj, hours in subject_hours.items()
                if hours > 1 and daily_subject_count[day][subj] < 2
                   and is_slot_available(conflict_graph, day_index, slot, subjects[subj]["guru"], class_name)
                   and is_subject_time_valid(day, slot, subj, subject_time_restrictions)  # Cek pembatasan waktu
                   and (slot + 1 < 6 and is_slot_available(conflict_graph, day_index, slot + 1,
                                                           subjects[subj]["guru"], class_name))
            ]

            if available_subjects:
                # Pilih pelajaran berdasarkan prioritas heap
                selected_subject = random.choice(available_subjects)
                # Alokasikan 2 jam pelajaran secara berurutan
                if slot + 1 < 6:
                    schedule[day][slot] = selected_subject
                    schedule[day][slot + 1] = selected_subject
                    subject_hours[selected_subject] -= 2
                    daily_subject_count[day][selected_subject] += 2

                    # Perbarui graf konflik
                    conflict_graph[class_name][day_index][slot] = subjects[selected_subject]["guru"]
                    conflict_graph[class_name][day_index][slot + 1] = subjects[selected_subject]["guru"]

    return schedule


# Fungsi untuk membuat jadwal untuk beberapa kelas
def generate_schedules_for_classes(subjects, schedule_template, num_classes):
    schedules = {}
    conflict_graph = {f"Kelas {class_num}": {day_index: [None] * 6 for day_index in range(5)} for class_num in
                      range(1, num_classes + 1)}

    for class_num in range(1, num_classes + 1):
        class_name = f"Kelas {class_num}"
        schedules[class_name] = generate_schedule_with_priority(subjects, schedule_template, conflict_graph, class_name)

    return schedules


# Membuat Graph untuk mendeteksi konflik
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


# Fungsi untuk menampilkan graph konflik
def display_conflict_graph(G):
    pos = nx.spring_layout(G)  # Posisi untuk layout graf
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.title("Konflik Antar Kelas")
    plt.show()


# Generate jadwal untuk 3 kelas
final_schedules = generate_schedules_for_classes(subjects, schedule_template, 3)

# Menampilkan jadwal untuk setiap kelas
for class_name, schedule in final_schedules.items():
    print(f"\nJadwal untuk {class_name}:")
    for day, slots in schedule.items():
        print(f"  {day}: {slots}")

# Membuat graph konflik
conflict_graph = build_conflict_graph(final_schedules, subjects)

# Menampilkan konflik antar kelas
print("\nKonflik antar kelas:")
for edge in conflict_graph.edges():
    print(f"Konflik antara {edge[0]} dan {edge[1]}")

# Menampilkan grafik konflik
display_conflict_graph(conflict_graph)
