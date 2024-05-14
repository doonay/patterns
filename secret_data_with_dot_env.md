# Этот файл поможет вам быстро вспомнить, как использовать .env для хранения секретных данных.

1. Установите библиотеку:
pip install python-dotenv

2. Создайте файл .env в корневой директории вашего проекта:
USER=your_username
PASSWORD=your_password
API_KEY=your_api_key

3. Добавьте файл .env в .gitignore.

4. Загрузите переменные окружения из файла .env в вашем скрипте:
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем значения переменных
user = os.getenv("USER")
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")

Пример использования:
print(f"Привет, {user}! Твой API ключ: {api_key}")

Вы можете указать путь к файлу .env, если он не находится в корне проекта: load_dotenv(dotenv_path='path/to/.env').
Можно использовать переменные окружения, определённые в системе, если они не найдены в файле .env: override=True.
