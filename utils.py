import string


class Utils():
    def capitalize(self, to_capitalize):
        capitalized_dict = {}

        for key, value in to_capitalize.items():
            capitalized_dict[key] = string.capwords(value.strip())

        return capitalized_dict

