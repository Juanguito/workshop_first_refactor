from pathlib import Path

import folders
import tags
import utils


class MainProgram():
    SOURCE_PATH = Path('./files')
    DESTINATION_PATH = Path('./result/')

    def __init__(self):
        self.folders = folders.Folders()
        self.tags = tags.Tags()
        self.utils = utils.Utils()

    def retag_files(self):
        mp3_files = self.folders.retrieve_mp3_files(self.SOURCE_PATH)

        for mp3_file in mp3_files:
            complete_file_path = self.folders.join(self.SOURCE_PATH, mp3_file.name)

            mp3 = self.tags.open_mp3_file(complete_file_path)

            tags = self.tags.read_tags(mp3)
            if len(tags) != 2 or not tags.get('song', False):
                tags = self.tags.get_artist_and_song_from_file_name(mp3_file)
            tags = self.utils.capitalize(tags)

            source_file_path = self.folders.join(
                self.SOURCE_PATH,
                mp3_file.name,
            )

            new_path = self.folders.copy_file(
                source_file_path,
                self.DESTINATION_PATH,
                '{}.mp3'.format(tags.get('song', mp3_file.name)),
            )

            new_mp3_file = self.tags.open_mp3_file(new_path)
            self.tags.write_artist_and_song_tags(new_mp3_file, tags)


if __name__ == '__main__':
    main = MainProgram()
    main.retag_files()
