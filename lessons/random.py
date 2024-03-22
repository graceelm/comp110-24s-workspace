def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Update the dictionary with new attendance information."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = []
        attendance_dict[day].append(student)

t: dict[str, list[str]] = {"Monday": ["Jordan", "Emma"], "Tuesday": ["Emma", "Grace"], "Wednesday": ["Jordan", "Emma"]}
day: str = "Tuesday"
student: str = "Emma"
update_attendance(t, day, student)
print(t)