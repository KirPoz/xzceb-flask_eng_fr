"""
This modul Use Watson APIs to create functions that translates English to French
and function that translates French to English.
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

APIKEY_LT = os.environ.get('APIKEY_LT_ENV', "not found")
URL_LT = os.environ.get('URL_LT_ENV', "not found")
VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT,
    authenticator=authenticator
)

language_translator.set_service_url(URL_LT)


def english_to_french(english_text = None):
    """
    This function translates English to French
    """
    try:
        translation_response = language_translator.translate(text=english_text, model_id='en-fr')
        translation = translation_response.get_result()
        french_text = translation['translations'][0]['translation']
    except:
        french_text = ''
    return french_text


def french_to_english(french_text  = None):
    """
    This function translates French to English
    """
    try:
        translation_response = language_translator.translate(text=french_text, model_id='fr-en')
        translation = translation_response.get_result()
        english_text = translation['translations'][0]['translation']
    except:
        english_text = ''
    return english_text
