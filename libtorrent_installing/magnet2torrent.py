import os
import sys
import libtorrent as lt
import time
from urllib.parse import unquote


def create_clean_torrent(magnet_link, output_torrent_path):
    """Создает чистый .torrent файл из магнет-ссылки"""
    
    # Создаем временную директорию, если ее нет
    #os.makedirs(temp_dir, exist_ok=True)
    
    # Инициализация сессии
    ses = lt.session()

    
    # Парсинг магнет-ссылки и настройка параметров
    params = {
        "save_path": output_torrent_path,  # Обязательный параметр!
        "storage_mode": lt.storage_mode_t.storage_mode_sparse,
        "url": magnet_link
    }
    
    # Добавляем торрент
    handle = ses.add_torrent(params)
    

    print("⏳ Получаем метаданные... (это может занять несколько минут)")
    while not handle.status().has_metadata:
        time.sleep(1)
        print(".", end="", flush=True)
    
    print("\n✅ Метаданные получены!")
    
    # Создаем торрент-файл
    torrent_info = handle.get_torrent_info()
    

    torrent = lt.create_torrent(torrent_info)
    
    # Удаляем идентифицирующую информацию
    torrent.set_creator('')  # Удаляем информацию о создателе
    torrent.set_comment('')  # Удаляем комментарии
    #torrent.set_modification_time(0)  # Обнуляем время модификации
    
    # Сохраняем торрент-файл
    with open(output_torrent_path, 'wb') as f:
        f.write(lt.bencode(torrent.generate()))
    
    print(f"✅ Чистый торрент-файл сохранен: {output_torrent_path}")

if __name__ == "__main__":
    # Настройки
    MAGNET_LINK = "magnet:?xt=urn:btih:C2858D2293157E5DD029945FA64215B8E5E581FF&tr=http%3A%2F%2Fbt.t-ru.org%2Fann%3Fmagnet&dn=%5BDL%5D%20Rage%202%20%5BP%5D%20%5BRUS%20%2B%20ENG%20%2F%20RUS%20%2B%20ENG%5D%20(2019%2C%20FPS)%20(1.09u4%20%2B%202%20DLC)%20%5BP2P%5D"
    OUTPUT_FILE = f"{unquote(MAGNET_LINK) \
        .replace("[", "(") \
        .replace("\\", "-") \
        .replace("/", "-") \
        .replace(":", "-") \
        .replace("*", "") \
        .replace("?", "") \
        .replace("\"", "") \
        .replace("<", "(") \
        .replace(">", ")") \
        .replace("|", "-") \
        .replace("]", ")") \
        .split("&dn=")[-1]}.torrent"

        

    create_clean_torrent(MAGNET_LINK, OUTPUT_FILE)