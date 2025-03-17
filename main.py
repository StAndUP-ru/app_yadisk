import sys
import yadisk
import posixpath
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('TOKEN', default='TOKEN')
APP_ID = os.getenv('APP_ID', default='TOKEN')
APP_SECRET = os.getenv('APP_SECRET', default='TOKEN')


def recursive_download(client: yadisk.Client, remote_dir: str, local_dir: str):
    # Создаем локальную директорию, если её нет
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Получаем содержимое удаленной директории
    entries = client.listdir(remote_dir)
    for entry in entries:
        remote_path = entry.path
        local_path = os.path.join(local_dir, entry.name)

        if entry.type == 'dir':
            # Если это директория, рекурсивно обрабатываем её
            recursive_download(client, remote_path, local_path)
        else:
            # Если это файл, загружаем его
            print(f"Скачиваем: {remote_path} в {local_path}")
            client.download(remote_path, local_path)

def main():
    with yadisk.Client(APP_ID, APP_SECRET, TOKEN) as client:
        remote_dir = "/"  # Указываем корневую директорию Яндекс.Диска
        local_dir = "/test"  # Локальная директория для загрузки файлов
        recursive_download(client, remote_dir, local_dir)

if __name__ == "__main__":
    main()