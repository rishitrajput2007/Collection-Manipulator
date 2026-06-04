print("Welcome to the Student Data Organizer!")

s = []

while True:

    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    n = int(input("Enter your choice: "))

    match n:


        case 1:

            print("\nEnter Student Details:")

            sid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")

            subjects = input(
                "Subjects (comma-separated): "
            ).split(",")

            details = (sid, dob)

            student = {
                "name": name,
                "age": age,
                "grade": grade,
                "date": dob,
                "subject": subjects,
                "details": details
            }

            s.append(student)

            print("Student added successfully!")


        case 2:

            print("\n--- Display All Students ---")

            if len(s) == 0:
                print("No student records found.")

            else:
                for i in s:

                    print(
                        f"Student ID: {i['details'][0]} | "
                        f"DOB: {i['details'][1]} | "
                        f"Name: {i['name']} | "
                        f"Age: {i['age']} | "
                        f"Grade: {i['grade']} | "
                        f"Subjects: {', '.join(i['subject'])}"
                    )


        case 3:

            sid = int(input("Enter Student ID to update: "))

            found = False

            for i in s:

                if i["details"][0] == sid:

                    found = True

                    i["age"] = int(input("Enter new age: "))

                    i["subject"] = input(
                        "Enter new subjects (comma-separated): "
                    ).split(",")

                    print("Student information updated successfully!")

                    break

            if not found:
                print("Student not found!")


        case 4:

            sid = int(input("Enter Student ID to delete: "))

            found = False

            for i in s:

                if i["details"][0] == sid:

                    s.remove(i)

                    found = True

                    print("Student deleted successfully!")

                    break

            if not found:
                print("Student not found!")


        case 5:

            subjects_set = set()

            for i in s:
                subjects_set.update(i["subject"])

            print("\nSubjects Offered:")

            for sub in subjects_set:
                print(sub)


        case 6:

            print("Thank you for using the Student Data Organizer!")
            break


        case _:

            print("Invalid Choice!")