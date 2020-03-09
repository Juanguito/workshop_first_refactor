from unittest import TestCase

import utils

class TestUtils(TestCase):
    def setUp(self):
        self.utils = utils.Utils()

    def test_format_label(self):
        to_capitalize = {
            'artist': ' artist',
            'song': 'sOng',
        }

        capitalized = self.utils.capitalize(to_capitalize)

        assert capitalized == {
            'artist': 'Artist',
            'song': 'Song',
        }
