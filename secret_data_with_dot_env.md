# Шпаргалка по хранению секретных данных в .env

1. Устанавливаем библиотеку:<br>
```python
pip install python-dotenv
```
2. Создаём файл .env в корневой директории вашего проекта:<br>
USER=your_username<br>
PASSWORD=your_password<br>
API_KEY=your_api_key<br>

3. Добавляем файл .env в .gitignore.

4. Загружаем переменные окружения из файла .env в вашем скрипте:<br>
import os<br>
from dotenv import load_dotenv<br>
<br>
load_dotenv()

5. Получаем значения переменных<br>
user = os.getenv("USER")<br>
password = os.getenv("PASSWORD")<br>
api_key = os.getenv("API_KEY")<br>

Пример использования:<br>
print(f"Привет, {user}! Твой API ключ: {api_key}")

Вы можете указать путь к файлу .env, если он не находится в корне проекта: load_dotenv(dotenv_path='path/to/.env').
Можно использовать переменные окружения, определённые в системе, если они не найдены в файле .env: override=True.
