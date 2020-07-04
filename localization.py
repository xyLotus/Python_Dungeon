"""
Localization controller
"""
import json


class Localization:
    """
    Used for translating ItemIDs into the selected language.
    If translation fails, it will fallback to the ItemID instead.
    """
    def __init__(self, lang='default'):
        """ Opens the lang file and saves the content to self.data """
        with open('lang/' + lang + '.json') as lang_file:
            self.data = json.loads(lang_file.read())

    def translate(self, category, iid) -> str:
        """
        Looks through the self.data dictionary for the ItemID
        in the selected category and returns a str from the
        lang file. If it does not find the selected ItemID in
        the category, it will fallback to the ItemID itself
        and return that as the name.
        (Also raises a LocalizationError warning if fails)
        """
        try:
            return self.data[category][iid]
        except KeyError:
            print(f"[!] LocalizationError: "
                  f"'{iid}' is not specified, fallback to ItemID")
            return iid
