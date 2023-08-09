Students = [{"name":"ram","gender":"Male"},{"name":"ritu","gender":"Female"},{"name":"hari","gender":"Male"}]

#list comprehesion - #To get the name of students whose Gender is male and sorted in alphabetic order.
names_of_students = [student["name"] for student in Students if student["gender"] == "Male"]

for name_of_student in sorted(names_of_students):
    print(name_of_student)

print("Hello")




