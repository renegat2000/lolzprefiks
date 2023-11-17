from notes_manager import NoteManager


def main_menu(note_manager):
    while True:
        print("-----------------------------------------------")
        print("----- Приложение для управления заметками -----")
        print("1. Добавить заметку")
        print("2. Просмотреть список всех заметок")
        print("3. Поиск заметок")
        print("4. Удалить заметку")
        print("5. Выйти из приложения")

        choice = input("Введите номер действия: ")

        match choice:
            case "1":
                # добавление заметки
                title = input("Введите заголовок заметки: ")
                content = input("Введите содержание заметки: ")
                note_manager.add_note(title, content)
            case "2":
                # просмотр списка всех заметок
                note_manager.display_all_notes()
            case "3":
                # поиск заметок по ключевому слову
                keyword = input("Введите ключевое слово для поиска: ")
                note_manager.search_notes(keyword)
            case "4":
                # удаление заметки
                note_id = int(input("Введите ID заметки,"
                                    " которую хотите удалить: "))
                note_manager.delete_note(note_id)
            case "5":
                # выход из приложения
                break
            case _:
                print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    db_file = 'notes.db'
    note_manager = NoteManager(db_file)
    main_menu(note_manager)
    note_manager.close_connection()
