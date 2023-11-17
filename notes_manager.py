import sqlite3


class NoteManager:
    def __init__(self, db_file):
        # создаем подключение к базе данных
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # создаем таблицу, если она не существует
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              title TEXT,
                              content TEXT)''')

    def add_note(self, title, content):
        # добавление новой заметки
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
                            (title, content))
        self.conn.commit()
        print("Заметка добавлена в базу данных.")

    def display_all_notes(self):
        # Вывод списка всех заметок
        self.cursor.execute("SELECT * FROM notes")
        notes = self.cursor.fetchall()

        if not notes:
            print("Список заметок пуст.")
        else:
            print("Список заметок:")
            for note in notes:
                print("ID:", note[0])
                print("Заголовок:", note[1])
                print("---------------------------")

    def search_notes(self, keyword):
        # поиск заметок по ключевому слову
        self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR"
                            " content LIKE ?",
                            ('%' + keyword + '%', '%' + keyword + '%'))
        notes = self.cursor.fetchall()

        if not notes:
            print("Заметки не найдены.")
        else:
            print("Результаты поиска:")
            for note in notes:
                print("ID:", note[0])
                print("Заголовок:", note[1])
                print("---------------------------")

    def delete_note(self, note_id):
        # удаление заметки по ID
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()
        print("Заметка удалена из базы данных.")

    def close_connection(self):
        # закрытие соединения с базой данных
        self.conn.close()
        print("Соединение с базой данных закрыто.")
