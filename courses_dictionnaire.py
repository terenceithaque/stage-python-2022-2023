courses = {"Litière" : 1,
           "Chocapic" : 3,
           "Lait" : 8}


print(courses)

courses.update({"Jouets" : 130})

courses.__delitem__("Litière")
courses.update({"Chocapic" : 7000})

print(courses)