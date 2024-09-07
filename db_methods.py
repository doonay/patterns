# метод добавления списка словарей в базу данных с помощью executemany (одна страница айтемов при парсинге)
def insert_creators(api_json_creators):
  connection = sqlite3.connect("coomer.db")
  cursor = connection.cursor()

  cursor.executemany("""
    INSERT OR IGNORE INTO Creators(
      creator_id,
      creator_name,
      creator_service
    ) VALUES (?, ?, ?)""",
    [(creator['id'], creator['name'], creator['service']) for creator in api_json_creators]
  )

  connection.commit()
  connection.close()
