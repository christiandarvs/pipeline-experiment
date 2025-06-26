import platform
from datetime import datetime


def get_month_text(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return months.get(month)


current_os = platform.system()
day = datetime.now().day
month = datetime.now().month
month_text = get_month_text(month)
year = datetime.now().year

print(f"Current Operating System: {current_os}")
print(f"{month_text} {day}, {year}")
