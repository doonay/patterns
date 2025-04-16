import bencodepy
from pprint import pprint

def print_torrent_structure(data, indent=0, skip_keys={b'pieces'}):
    """Рекурсивно печатает структуру торрент-файла, пропуская указанные ключи"""
    prefix = ' ' * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key in skip_keys:
                print(f"{prefix}{key.decode('utf-8')}: <skipped binary data>")
                continue
                
            decoded_key = key.decode('utf-8') if isinstance(key, bytes) else str(key)
            print(f"{prefix}{decoded_key}: ", end='')
            
            if isinstance(value, (dict, list)):
                print()
                print_torrent_structure(value, indent + 4, skip_keys)
            else:
                if isinstance(value, bytes) and len(value) > 50:  # Сокращаем длинные бинарные данные
                    print(f"<binary data {len(value)} bytes>")
                else:
                    try:
                        print(value.decode('utf-8') if isinstance(value, bytes) else value)
                    except UnicodeDecodeError:
                        print(f"<binary data {len(value)} bytes>")
    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print(f"{prefix}[{i}]: ", end='')
            if isinstance(item, (dict, list)):
                print()
                print_torrent_structure(item, indent + 4, skip_keys)
            else:
                try:
                    print(item.decode('utf-8') if isinstance(item, bytes) else item)
                except UnicodeDecodeError:
                    print(f"<binary data {len(item)} bytes>")

# Загрузка и анализ торрент-файла
with open("Rage_2.torrent", "rb") as f:
    torrent_data = bencodepy.decode(f.read())

print("Полная структура торрент-файла (без pieces):")
print_torrent_structure(torrent_data)