# translations.py
import json
from typing import Dict
from string import Template

_translations = {}


def load_translations(language):
    """
    Loads the translations for the given language from a JSON file.

    Args:
        language (str): The language code (e.g., 'en', 'fr') for the desired translations.
    """
    global _translations
    try:
        file_path = f".\\i18n\\{language}.json"
        with open(file_path, "r", encoding="utf-8") as file:
            _translations[language] = json.load(file)
    except FileNotFoundError:
        _translations[language] = {}


def get_translations(language) -> Dict[str, str]:
    """
    Returns the translations for the given language.

    Args:
        language (str): The language code (e.g., 'en', 'fr') for the desired translations.

    Returns:
        dict: A dictionary containing the translations for the specified language.
    """
    if language not in _translations:
        load_translations(language)
    return _translations[language]


def translate(language, key) -> str:
    """
    Translates the given key based on the specified language.

    Args:
        language (str): The language code (e.g., 'en', 'fr') for the desired translation.
        key (str): The key to be translated.

    Returns:
        str: The translated value for the given key, or the key itself if no translation is found.
    """
    translations = get_translations(language)
    return translations.get(key, key)

def translate_parameterized(language, key, kwargs: Dict) -> str:
    """
    Translates the given key based on the specified language.

    Args:
        language (str): The language code (e.g., 'en', 'fr') for the desired translation.
        key (str): The key to be translated.

    Returns:
        str: The translated value for the given key, or the key itself if no translation is found.
    """
    translations = get_translations(language)
    template = Template(translations.get(key, key))
    return template.substitute(**kwargs)