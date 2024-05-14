# Шпаргалка по хранению секретных данных в .env

1. Устанавливаем библиотеку:
pip install python-dotenv

2. Создаём файл .env в корневой директории вашего проекта:
USER=your_username
PASSWORD=your_password
API_KEY=your_api_key

3. Добавляем файл .env в .gitignore.

4. Загружаем переменные окружения из файла .env в вашем скрипте:
import os
from dotenv import load_dotenv

load_dotenv()

5. Получаем значения переменных
user = os.getenv("USER")
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")

Пример использования:
print(f"Привет, {user}! Твой API ключ: {api_key}")

Вы можете указать путь к файлу .env, если он не находится в корне проекта: load_dotenv(dotenv_path='path/to/.env').
Можно использовать переменные окружения, определённые в системе, если они не найдены в файле .env: override=True.
