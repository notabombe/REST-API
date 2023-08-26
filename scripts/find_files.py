"""
find docker-compose.yml files
"""

import fnmatch
import os

def find_yml_files(path):
    """
    find docker-compose.yml files in path
    """
    matches = {}
    for root, _, filenames in os.walk(path):
        for _ in fnmatch.filter(filenames, 'docker-compose.yml'):
            key = root.split('/')[-1]
            matches[key] = os.path.join(os.getcwd(), root)
    return matches


def get_readme_file(path):
    """
    find case insensitive readme.md in path and return the contents
    """

    readme = None

    for file in os.listdir(path):
        if file.lower() == "readme.md" and os.path.isfile(os.path.join(path, file)):
            with open(os.path.join(path, file)) as file:
                readme = file.read()
            break

    return readme

def get_logo_file(path):
    """
    find case insensitive logo.png in path and return the contents
    """

    logo = None

    for file in os.listdir(path):
        if file.lower() == "logo.png" and os.path.isfile(os.path.join(path, file)):
            with open(os.path.join(path, file)) as file:
                logo = file.read()
            break

    return logo
