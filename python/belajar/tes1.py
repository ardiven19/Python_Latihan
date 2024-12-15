import random

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


# Fungsi untuk memeriksa apakah slot waktu tersedia (tidak konflik)
def is_slot_available(conflict_graph, day_index, slot, guru, class_name):
    # Memeriksa apakah guru yang sama mengajar di kelas lain pada waktu yang sama
    for other_class_name, other_schedule in conflict_graph.items():
        if other_class_name != class_name and other_schedule[day_index][slot] == guru:
            return False
    return conflict_graph[class_name][day_index][slot] is None


# Fungsi untuk membuat jadwal untuk satu kelas
def generate_schedule(subjects, schedule_template, conflict_graph, class_name):
    # Salin template jadwal
    schedule = {day: slots[:] for day, slots in schedule_template.items()}

    # Track alokasi jam per mata pelajaran
    subject_hours = {subject: data["durasi"] for subject, data in subjects.items()}

    # Track jumlah jam per pelajaran per hari
    daily_subject_count = {day: {subject: 0 for subject in subjects} for day in schedule}

    # Loop untuk mengisi jadwal
    for day_index, day in enumerate(schedule):
        i = 0
        while i < len(schedule[day]):
            # Pilih pelajaran secara acak yang masih memiliki durasi, belum melebihi 2 jam per hari, dan tidak konflik
            available_subjects = [
                subj for subj, hours in subject_hours.items()
                if hours > 1 and daily_subject_count[day][subj] < 2
                   and is_slot_available(conflict_graph, day_index, i, subjects[subj]["guru"], class_name)
                   and (i + 1 < len(schedule[day]) and is_slot_available(conflict_graph, day_index, i + 1,
                                                                         subjects[subj]["guru"], class_name))
            ]

            if not available_subjects:
                break

            selected_subject = random.choice(available_subjects)

            # Alokasikan 2 jam pelajaran secara berurutan
            if i + 1 < len(schedule[day]):
                schedule[day][i] = selected_subject
                schedule[day][i + 1] = selected_subject
                subject_hours[selected_subject] -= 2
                daily_subject_count[day][selected_subject] += 2

                # Perbarui graf konflik
                conflict_graph[class_name][day_index][i] = subjects[selected_subject]["guru"]
                conflict_graph[class_name][day_index][i + 1] = subjects[selected_subject]["guru"]

                i += 2
            else:
                break

    return schedule


# Fungsi untuk membuat jadwal untuk beberapa kelas
def generate_schedules_for_classes(subjects, schedule_template, num_classes):
    schedules = {}
    conflict_graph = {f"Kelas {class_num}": {day_index: [None] * 6 for day_index in range(5)} for class_num in
                      range(1, num_classes + 1)}

    for class_num in range(1, num_classes + 1):
        class_name = f"Kelas {class_num}"
        schedules[class_name] = generate_schedule(subjects, schedule_template, conflict_graph, class_name)

    return schedules


# Generate jadwal untuk 3 kelas
final_schedules = generate_schedules_for_classes(subjects, schedule_template, 3)

# Tampilkan jadwal untuk setiap kelas
for class_name, schedule in final_schedules.items():
    print(f"\nJadwal untuk {class_name}:")
    for day, slots in schedule.items():
        print(f"  {day}: {slots}")


def check_schedule_conflicts(final_schedules, subjects):
    conflicts = []
    # Ambil jadwal semua kelas
    days = list(schedule_template.keys())
    num_slots = len(schedule_template["Senin"])  # Asumsi semua hari punya slot sama
    for day_index, day in enumerate(days):
        for slot in range(num_slots):
            # Lacak guru yang mengajar di waktu tertentu
            teaching_gurus = {}
            for class_name, schedule in final_schedules.items():
                subject = schedule[day][slot]
                if subject:
                    guru = subjects[subject]["guru"]
                    if guru in teaching_gurus:
                        conflicts.append((day, slot, guru, teaching_gurus[guru], class_name))
                    else:
                        teaching_gurus[guru] = class_name
    return conflicts


# Cek konflik antar kelas
conflicts = check_schedule_conflicts(final_schedules, subjects)
if conflicts:
    print("\nKonflik terdeteksi:")
    for conflict in conflicts:
        day, slot, guru, class1, class2 = conflict
        print(f"  - {guru} mengajar di {class1} dan {class2} pada {day} slot {slot + 1}")
else:
    print("\nTidak ada konflik antar kelas.")
