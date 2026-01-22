from functools import lru_cache

college_data = {
    "Engineering College": {
        "CSE": {
            "Maths": ("Theory", 4),
            "Python": ("Theory", 5),
            "AI": ("Theory", 4),
            "DBMS": ("Theory", 3),
            "OS": ("Theory", 3),
            "AI Lab": ("Practical", 2),
            "DBMS Lab": ("Practical", 2)
        }
    }
}

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

TIME_SLOTS = [
    "09:00-10:00",
    "10:00-11:00",
    "11:15-12:15",
    "12:15-01:15",
    "02:00-03:00",
    "03:00-04:00"
]

CLASSROOMS = ["C101", "C102", "C103"]
LABS = ["L201", "L202"]

def create_lectures(subjects):
    lectures = []
    for subject, (stype, count) in subjects.items():
        if stype == "Theory":
            for _ in range(count):
                lectures.append((subject, "Theory"))
        else:
            for _ in range(count):
                lectures.append((subject, "Practical"))
    return lectures

def generate_timetable_dp(subjects):
    lectures = create_lectures(subjects)
    timetable = {}
    daily_subject_usage = {}

    @lru_cache(None)
    def dp(idx, used_slots_frozen, used_branch_frozen):
        if idx == len(lectures):
            return True

        used_slots = set(used_slots_frozen)
        used_branch = set(used_branch_frozen)

        subject, stype = lectures[idx]

        for day in DAYS:
            if (subject, day) in daily_subject_usage:
                continue

            for i in range(len(TIME_SLOTS)):
                if stype == "Practical":
                    if i == len(TIME_SLOTS) - 1:
                        continue
                    time_pair = [(day, i), (day, i + 1)]
                    rooms = LABS
                else:
                    time_pair = [(day, i)]
                    rooms = CLASSROOMS

                if any((d, t) in used_branch for (d, t) in time_pair):
                    continue

                for room in rooms:
                    if any((d, t, room) in used_slots for (d, t) in time_pair):
                        continue

                    for (d, t) in time_pair:
                        used_slots.add((d, t, room))
                        used_branch.add((d, t))
                        timetable[(idx, d, t)] = (subject, room)

                    daily_subject_usage[(subject, day)] = True

                    if dp(idx + 1, frozenset(used_slots), frozenset(used_branch)):
                        return True

                    for (d, t) in time_pair:
                        used_slots.remove((d, t, room))
                        used_branch.remove((d, t))
                        del timetable[(idx, d, t)]
                    del daily_subject_usage[(subject, day)]

        return False

    dp(0, frozenset(), frozenset())

    structured = {day: {TIME_SLOTS[i]: [] for i in range(len(TIME_SLOTS))} for day in DAYS}
    for (_, day, t), (subject, room) in timetable.items():
        structured[day][TIME_SLOTS[t]].append((subject, room))

    return structured

def print_timetable(college, branch, timetable):
    print(f"\n🏫 {college} | Branch: {branch}")
    print("-" * 65)
    for day in DAYS:
        print(f"\n{day}")
        for time in TIME_SLOTS:
            if timetable[day][time]:
                for subject, room in timetable[day][time]:
                    print(f"  {time} → {subject} in {room}")
            else:
                print(f"  {time} → Free")
    print("-" * 65)

for college, branches in college_data.items():
    for branch, subjects in branches.items():
        timetable = generate_timetable_dp(subjects)
        print_timetable(college, branch, timetable)
