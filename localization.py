"""
Localization controller
"""
import json


class Localization:
    def __init__(self, lang):
        with open('lang/' + lang + '.json') as lang_file:
            self.data = json.loads(lang_file.read())

    def loc(self, category, namespace):
        return self.data[category][namespace]
