#install translate
from translate import Translator

languages = ['fr','it','es','ru','de']

text = input('What text would you like to translate?')

for language in languages:
    translator = Translator(provider='libre',from_lang='en',to_lang=language)
    translation = translator.translate(text)
    print(f'{language}:{translation}')
