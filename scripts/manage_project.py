"""
docker compose project management
"""

from os import rename, makedirs
from time import time

def manage(directory, yml, is_update):
    """
    create or update docker compose project
    """

    file_path = f"{directory}/docker-compose.yml"

    if is_update:
        rename(file_path, f"{file_path}.{int(round(time()))}")
    else:
        makedirs(directory)

    with open(file_path, "w") as out_file:
        out_file.write(yml)
    return file_path
