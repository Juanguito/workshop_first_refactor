import os
import shutil


class Folders():
    def retrieve_mp3_files(self, path):
        return set(
            entry for entry in os.scandir(path)
            if entry.is_file() and entry.name.endswith('.mp3')
        )

    def copy_file(self, source, destination, file_name):
        if not os.path.exists(source):
            return None

        if not os.path.exists(destination):
            os.mkdir(destination)

        destination_file_path = os.path.join(
                destination,
                file_name,
            )

        newPath = shutil.copy(source, destination_file_path)

        return newPath

    def join(self, path_1, path_2):
        return os.path.join(path_1, path_2)
