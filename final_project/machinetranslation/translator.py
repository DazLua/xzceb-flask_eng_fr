import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', 
authenticator=authenticator)

language_translator.set_service_url(url)

englishText = None
Frenchtext = None

def englishToFrench(englishText):
    
    frenchText = language_translator.translate(englishText, model_id='en-fr').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))

    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(frenchText, model_id='fr-en').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))

    return englishText
    