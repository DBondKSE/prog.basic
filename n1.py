import pickle

with open("data.csv", "r") as file:
    next(file)
    grades = ["grade 8", "grade 9", "grade 10", "grade 11"]
    langs = ["Python", "C++", "C#", "Java"]
    student_dict = {}
    for g in grades:
        lang_dict = {}
        for l in langs:
            lang_dict[l] = []

        student_dict[g] = lang_dict


    for line in file:
        student = line.split(", ")
        grade = student[3]
        lang = student[5].replace("\n", "")
        student_dict[f"grade {grade}"][lang].append(student)

    for i in student_dict:
        print(i)
        for j in student_dict[i]:
            print(f"    {j}")
            print(*student_dict[i][j], sep="\n")

with open("student_data.std", "wb") as file:
    pickle.dump(student_dict, file)