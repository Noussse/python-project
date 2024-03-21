import os
import shutil

path =os.path.join(os.path.expanduser('~'), 'Downloads')

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        root, extension = os.path.splitext(file)
        extension = extension[1:].lower()

        if extension == "mp4":
            destination_folder = "Video"
        elif extension in ("jpg", "jpeg"):
            destination_folder = "Images"
        elif extension in ("txt", "docx", "xlsx", "pptx"):
            destination_folder = "Documents"
        elif extension == "mp3":  # Check for mp3 files
            destination_folder = "Music"
        else:
            destination_folder = "Other"

        destination_directory = os.path.join(path, destination_folder)

        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        shutil.move(os.path.join(path, file), destination_directory)

print("Files organized successfully!")
