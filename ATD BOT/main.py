from scraper import get_attendance
from attendance_analysis import analyze

print("Program started...")

data = get_attendance()

print("Data collected:", data)

analyze(data)

print("Excel file created")