import pickle
import os

with open("student_data.std", "rb") as file:
    student_data = pickle.load(file)

for grade in student_data:
    os.mkdir(grade)
    for lang in student_data[grade]:
        os.mkdir(f"{grade}/{lang}")
        with open(f"{grade}/{lang}/students", "w") as file:
            file.write(str(student_data[grade][lang]))