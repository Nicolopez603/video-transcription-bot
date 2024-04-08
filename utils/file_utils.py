import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)