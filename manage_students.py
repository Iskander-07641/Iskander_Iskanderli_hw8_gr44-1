import sqlite3


def display_students_by_city(city_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    students = cursor.fetchall()

    if students:
        print(f"Students living in city ID {city_id}:")
        for student in students:
            print(
                f"Name: {student[0]} {student[1]}, Country: {student[2]}, City: {student[3]}, City Area: {student[4]}")
    else:
        print(f"No students found in city ID {city_id}.")

    conn.close()


def display_cities():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    print("You can display the list of students by selecting a city ID from the list below. To exit, enter 0:")
    for city in cities:
        print(f"{city[0]}: {city[1]}")

    conn.close()


def main():
    while True:
        display_cities()
        city_id = int(input("Enter city ID: "))

        if city_id == 0:
            print("Exiting program.")
            break
        else:
            display_students_by_city(city_id)


if __name__ == '__main__':
    main()
