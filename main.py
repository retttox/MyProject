
from database import create_database

from services.teacher_service import TeacherService
from services.discipline_service import DisciplineService
from services.auth_service import AuthService
from services.teacher_discipline_service import TeacherDisciplineService


teacher_service = TeacherService()
discipline_service = DisciplineService()
auth_service = AuthService()
teacher_discipline_service = TeacherDisciplineService()


def show_teachers():
    teachers = teacher_service.get_all()

    print("\nСписок преподавателей:")

    for teacher in teachers:
        print(
            f"ID: {teacher.id} | ФИО: {teacher.full_name} | "
            f"Email: {teacher.email} | Кафедра: {teacher.department}"
        )


def show_disciplines():
    disciplines = discipline_service.get_all()

    print("\nСписок дисциплин:")

    for discipline in disciplines:
        print(
            f"ID: {discipline.id} | Название: {discipline.name} | "
            f"Часы: {discipline.hours} | Описание: {discipline.description}"
        )


def admin_menu():
    while True:
        print("\n=== МЕНЮ АДМИНИСТРАТОРА ===")
        print("1. Показать преподавателей")
        print("2. Добавить преподавателя")
        print("3. Удалить преподавателя")
        print("4. Показать дисциплины")
        print("5. Добавить дисциплину")
        print("6. Удалить дисциплину")
        print("7. Изменить преподавателя")
        print("8. Изменить дисциплину")
        print("9. Назначить дисциплину преподавателю")
        print("10. Найти преподавателя по ФИО")
        print("11. Привязать аккаунт к преподавателю")
        print("12. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                show_teachers()

            elif choice == "2":
                full_name = input("ФИО: ")
                email = input("Email: ")
                department = input("Кафедра: ")

                teacher_service.add_teacher(full_name, email, department)
                print("Преподаватель добавлен!")

            elif choice == "3":
                teacher_id = int(input("Введите ID преподавателя: "))
                teacher_service.delete_teacher(teacher_id)
                print("Преподаватель удалён!")

            elif choice == "4":
                show_disciplines()

            elif choice == "5":
                name = input("Название дисциплины: ")
                hours = int(input("Количество часов: "))
                description = input("Описание: ")

                discipline_service.add_discipline(name, hours, description)
                print("Дисциплина добавлена!")

            elif choice == "6":
                discipline_id = int(input("Введите ID дисциплины: "))
                discipline_service.delete_discipline(discipline_id)
                print("Дисциплина удалена!")

            elif choice == "7":
                teacher_id = int(input("Введите ID преподавателя: "))
                full_name = input("Новое ФИО: ")
                email = input("Новый Email: ")
                department = input("Новая кафедра: ")

                teacher_service.update_teacher(
                    teacher_id, full_name, email, department
                )

                print("Данные преподавателя обновлены!")

            elif choice == "8":
                discipline_id = int(input("Введите ID дисциплины: "))
                name = input("Новое название дисциплины: ")
                hours = int(input("Новое количество часов: "))
                description = input("Новое описание: ")

                discipline_service.update_discipline(
                    discipline_id, name, hours, description
                )

                print("Данные дисциплины обновлены!")

            elif choice == "9":
                show_teachers()
                teacher_id = int(input("Введите ID преподавателя: "))

                show_disciplines()
                discipline_id = int(input("Введите ID дисциплины: "))

                teacher_discipline_service.assign_discipline(
                    teacher_id, discipline_id
                )

                print("Дисциплина назначена преподавателю!")

            elif choice == "10":
                search_name = input("Введите ФИО для поиска: ").strip().lower()

                teachers = teacher_service.get_all()

                found = [
                    teacher for teacher in teachers
                    if search_name in teacher.full_name.lower()
                ]

                if found:
                    print("\nРезультаты поиска:")

                    for teacher in found:
                        print(
                            f"ID: {teacher.id} | ФИО: {teacher.full_name} | "
                            f"Email: {teacher.email} | "
                            f"Кафедра: {teacher.department}"
                        )
                else:
                    print("Преподаватель не найден.")

            elif choice == "11":
                username = input("Введите логин пользователя: ")

                teachers = auth_service.get_teachers()

                print("\nСписок преподавателей:")

                for teacher in teachers:
                    print(f"{teacher[0]}. {teacher[1]}")

                teacher_id = int(input("Введите ID преподавателя: "))

                auth_service.link_teacher(username, teacher_id)

                print("Аккаунт успешно привязан!")

            elif choice == "12":
                break

            else:
                print("Неверный пункт меню!")

        except (ValueError, sqlite3.IntegrityError) as error:
            print("Ошибка:", error)


def user_menu(user):
    while True:
        print("\n=== МЕНЮ ПРЕПОДАВАТЕЛЯ ===")
        print("1. Посмотреть свои данные")
        print("2. Посмотреть свои дисциплины")
        print("3. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                teacher = teacher_service.get_by_id(user["teacher_id"])

                print("\nМои данные:")
                print("ФИО:", teacher.full_name)
                print("Email:", teacher.email)
                print("Кафедра:", teacher.department)

            elif choice == "2":
                disciplines = teacher_discipline_service.get_by_teacher_id(
                    user["teacher_id"]
                )

                print("\nМои дисциплины:")

                if not disciplines:
                    print("У вас пока нет назначенных дисциплин.")

                for discipline in disciplines:
                    print(
                        f"ID: {discipline.id} | "
                        f"Название: {discipline.name} | "
                        f"Часы: {discipline.hours} | "
                        f"Описание: {discipline.description}"
                    )

            elif choice == "3":
                break

            else:
                print("Неверный пункт меню!")

        except ValueError as error:
            print("Ошибка:", error)


def main():
    create_database()

    while True:
        print("\n=== УЧЁТ ПРЕПОДАВАТЕЛЕЙ И ДИСЦИПЛИН ===")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                username = input("Логин: ")
                password = input("Пароль: ")

                user = auth_service.login(username, password)

                print("Добро пожаловать,", user["username"])

                if user["role"] == "admin":
                    admin_menu()

                else:
                    if user["teacher_id"] is None:
                        print("Ваш аккаунт не привязан к преподавателю.")
                        continue

                    user_menu(user)

            elif choice == "2":
                username = input("Придумайте логин: ")
                password = input("Придумайте пароль: ")

                teachers = auth_service.get_teachers()

                print("\nСписок преподавателей:")

                for teacher in teachers:
                    print(f"{teacher[0]}. {teacher[1]}")

                teacher_id = int(input("Выберите свой ID преподавателя: "))

                auth_service.register(username, password, teacher_id)

                print("Регистрация прошла успешно!")

            elif choice == "3":
                print("Программа завершена.")
                break

            else:
                print("Неверный пункт меню!")

        except (ValueError, sqlite3.IntegrityError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    import sqlite3
    main()
