from mp3_tagger import MP3File
from mp3_tagger.exceptions import MP3OpenFileError

from pathlib import Path
import os
import shutil
from unittest import TestCase

from main import MainProgram


class TestMain(TestCase):
    destination_folder = Path('./result/')

    def test_main_generates_right_mp3_file(self):
        
        main = MainProgram()
        main.retag_files()

        # print('\ndestination_folder: {}\n'.format(self.destination_folder))
        self.assertTrue(os.path.exists(self.destination_folder))
        complete_path = os.path.join(self.destination_folder, 'Play.mp3')
        # print('\ncomplete_path: {}\n'.format(complete_path))
        self.assertTrue(os.path.exists(complete_path))

        mp3_file = MP3File(complete_path)
        self.assertEqual('Jax-jones-years-years', mp3_file.artist)
        self.assertEqual('Play', mp3_file.song)

    def tearDown(self):
        self.destination_folder = Path('./result/')
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder, ignore_errors=True)
