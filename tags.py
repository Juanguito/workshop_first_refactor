from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os


class Tags():
    def open_mp3_file(self, path):
        return MP3File(path)

    def read_tags(self, mp3_file):
        mp3_file.set_version(VERSION_2)
        tags = {
            'artist': mp3_file.artist,
            'song': mp3_file.song,
        }

        if not tags.get('artist', False) or not tags.get('song', False):
            mp3_file.set_version(VERSION_1)
            tags = {
                'artist': mp3_file.artist,
                'song': mp3_file.song,
            }

        return tags

    def get_artist_and_song_from_file_name(self, file):
        file_name = os.path.splitext(file.name)[0]
        clear_file_name = file_name.replace('_', ' ')
        tags = clear_file_name.split('-')

        return {
            'artist': tags[0],
            'song': tags[1],
        } if len(tags) == 2 else None

    def write_artist_and_song_tags(self, file, tags):
        file.artist = tags['artist']
        file.song = tags['song']
        file.save()

        return file
