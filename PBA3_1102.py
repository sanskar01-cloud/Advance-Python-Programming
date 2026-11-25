# Create a Python script to ready a JSON file containing student information and display the names of all students
import json

with open("students.json", "r") as file:
    data = json.load(file)

print("List of Student Names:")

for student in data["students"]:
    print(student["name"])
