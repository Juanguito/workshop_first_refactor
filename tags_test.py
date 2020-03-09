from pathlib import Path
from unittest import TestCase
from unittest.mock import (
    Mock,
    MagicMock,
)

import tags


class TestTags(TestCase):
    def setUp(self):
        self.tags = tags.Tags()

    def test_cant_open_file_as_mp3(self):
        not_mp3_file_path = Path('./files/file.txt')

        with self.assertRaises(Exception):  # MP3OpenFileError
            self.tags.open_mp3_file(not_mp3_file_path)

    def test_can_open_file_as_mp3(self):
        mp3_file_source_path = Path('./files/jax-jones-years-years-play.mp3')

        assert self.tags.open_mp3_file(str(mp3_file_source_path))

    def test_return_right_mp3_tags(self):
        mock_file = Mock(artist='artist', song='song')

        tags = self.tags.read_tags(mock_file)

        self.assertEqual('artist', tags['artist'])
        self.assertEqual('song', tags['song'])

    def test_get_artist_and_song_from_not_valid_file_name(self):
        mock_file = MagicMock()
        mock_file.name = 'not_valid_name.txt'

        assert not self.tags.get_artist_and_song_from_file_name(mock_file)

    def test_get_artist_and_song_from_valid_file_name(self):
        mock_file = MagicMock()
        mock_file.name = 'artist_name-song_tittle.txt'

        tags = self.tags.get_artist_and_song_from_file_name(mock_file)

        assert len(tags) == 2
        assert tags['artist'] == 'artist name'
        assert tags['song'] == 'song tittle'

    def test_write_tags(self):
        mp3_file = Mock(artist='foo', song='bar')

        mp3_file = self.tags.write_artist_and_song_tags(
            mp3_file,
            {
                'artist': 'artist',
                'song': 'song'
            }
        )

        assert mp3_file.artist == 'artist'
        assert mp3_file.song == 'song'

    def tearDown(self):
        pass