import os
import toml


def read_config_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = toml.load(file)
    return data


def write_config_file(data, file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, "w", encoding="utf-8") as file:
        toml.dump(data, file)
