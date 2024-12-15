import random
import heapq
import pandas as pd
import matplotlib.pyplot as plt

# Data pelajaran, durasi total per minggu (jam), dan guru
subjects = {
    "Matematika": {"durasi": 6, "guru": ["Ibu A", "Bapak I"]},  # 2 guru
    "IPA": {"durasi": 6, "guru": ["Bapak B", "Ibu J"]},  # 2 guru
    "IPS": {"durasi": 6, "guru": ["Ibu C", "Bapak K"]},  # 2 guru
    "Bahasa Indonesia": {"durasi": 4, "guru": ["Ibu D"]},
    "Bahasa Inggris": {"durasi": 4, "guru": ["Bapak E"]},
    "Penjas": {"durasi": 2, "guru": ["Bapak F"]},
    "Sejarah": {"durasi": 4, "guru": ["Ibu G"]},
    "SBK": {"durasi": 4, "guru": ["Bapak H"]}
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

# Fungsi untuk membagi pelajaran dengan dua guru
def assign_subject_with_multiple_teachers(subject, schedule, day_index, slot, subject_hours, teachers):
    # Membagi durasi antara guru
    if subject_hours[subject] > 0:
        # Pilih guru secara acak dari dua guru yang ada
        selected_teacher = random.choice(teachers)
        schedule[day_index][slot] = subject
        subject_hours[subject] -= 1
        return selected_teacher
    return None

# Fungsi untuk membuat jadwal untuk satu kelas dengan menggunakan prioritas
def generate_schedule_with_priority(subjects, schedule_template, conflict_graph, class_name):
    subject_heap = prioritize_subjects(subjects)
    schedule = {day: slots[:] for day, slots in schedule_template.items()}
    subject_hours = {subject: data["durasi"] for subject, data in subjects.items()}
    daily_subject_count = {day: {subject: 0 for subject in subjects} for day in schedule}

    # Loop untuk mengisi jadwal
    for day_index, day in enumerate(schedule):
        for slot in range(6):
            available_subjects = [
                subj for subj, hours in subject_hours.items()
                if hours > 0 and daily_subject_count[day][subj] < 2
                   and is_slot_available(conflict_graph, day_index, slot, subjects[subj]["guru"][0], class_name)
                   and is_subject_time_valid(day, slot, subj, subject_time_restrictions)
            ]

            if available_subjects:
                selected_subject = random.choice(available_subjects)
                if selected_subject in ["Matematika", "IPA", "IPS"]:
                    # Pelajaran dengan dua guru
                    teachers = subjects[selected_subject]["guru"]
                    assigned_teacher = assign_subject_with_multiple_teachers(selected_subject, schedule, day_index, slot, subject_hours, teachers)
                    if assigned_teacher:
                        conflict_graph[class_name][day_index][slot] = assigned_teacher
                else:
                    # Pelajaran dengan satu guru
                    schedule[day][slot] = selected_subject
                    subject_hours[selected_subject] -= 1
                    conflict_graph[class_name][day_index][slot] = subjects[selected_subject]["guru"][0]

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

# Fungsi untuk menyimpan jadwal ke Excel
def save_schedule_to_excel(schedules, filename="jadwal_kelas.xlsx"):
    # Menyusun data untuk dimasukkan ke dalam DataFrame
    data = []
    for class_name, schedule in schedules.items():
        for day, slots in schedule.items():
            data.append([class_name, day] + slots)

    # Membuat DataFrame dari data
    df = pd.DataFrame(data, columns=["Kelas", "Hari", "Jam 1", "Jam 2", "Jam 3", "Jam 4", "Jam 5", "Jam 6"])

    # Menyimpan ke file Excel
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"Jadwal berhasil disimpan ke {filename}")

# Generate jadwal untuk 3 kelas
final_schedules = generate_schedules_for_classes(subjects, schedule_template, 3)

# Menampilkan jadwal untuk setiap kelas
for class_name, schedule in final_schedules.items():
    print(f"\nJadwal untuk {class_name}:")
    for day, slots in schedule.items():
        print(f"  {day}: {slots}")

# Menyimpan jadwal ke Excel
save_schedule_to_excel(final_schedules)
