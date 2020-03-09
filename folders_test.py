from pathlib import Path
import shutil
from unittest import TestCase
import os

from folders import Folders


class TestFolders(TestCase):
    destination_folder = Path('./result/')
    empty_folder = Path('./foo')
    mp3_file_destination_path = Path('./result/Play.mp3')
    mp3_file_source_path = Path('./files/jax-jones-years-years-play.mp3')

    def setUp(self):
        self.folders = Folders()

    def test_access_to_not_existing_path(self):
        with self.assertRaises(FileNotFoundError):
            self.folders.retrieve_mp3_files('./path')

    def test_not_retrieve_files_from_empty_directory(self):
        if not os.path.exists(self.empty_folder):
            os.mkdir(self.empty_folder)

        entries = self.folders.retrieve_mp3_files(str(self.empty_folder))

        self.assertTrue(len(list(entries)) == 0)

    def test_retrieve_only_mp3_files_from_path(self):
        source_folder = Path('./files')
        entries = self.folders.retrieve_mp3_files(str(source_folder))

        self.assertTrue(len(list(entries)) > 0)

    def test_try_to_copy_non_existing_file(self):
        assert not self.folders.copy_file(
            './foo',
            self.mp3_file_destination_path,
            'bar.mp3',
        )

    def test_try_to_copy_to_non_existing_directory(self):
        newPath = self.folders.copy_file(
            self.mp3_file_source_path,
            self.destination_folder,
            'Play.mp3',
        )

        assert  newPath == str(self.mp3_file_destination_path)

    def test_copy_file_to_other_directory(self):
        if not os.path.exists(self.destination_folder):
            os.mkdir(self.destination_folder)

        newPath = self.folders.copy_file(
            self.mp3_file_source_path,
            self.destination_folder,
            'Play.mp3',
        )

        assert newPath
        assert newPath == str(self.mp3_file_destination_path)

    def test_join_path_with_file_name(self):
        file_path = Path('./file')
        file_name = 'file_name.mp3'

        file_path = self.folders.join(file_path, file_name)

        assert file_path == str(Path('./file/file_name.mp3'))

    def tearDown(self):
        if os.path.exists(self.empty_folder):
            shutil.rmtree(self.empty_folder, ignore_errors=True)
