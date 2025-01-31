#A script to organize files in a directory based on their extensions.
import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            if not os.path.exists(os.path.join(directory, file_extension)):
                os.makedirs(os.path.join(directory, file_extension))
            shutil.move(os.path.join(directory, filename), os.path.join(directory, file_extension, filename))

directory = input("Enter directory path to organize: ")
organize_files(directory)
print("Files organized successfully.")
