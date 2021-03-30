from googletrans import Translator
import pandas as pd

#print(googletrans.LANGUAGES)

translator = Translator()

#print(translator.translate('bom dia', src='pt', dest='en').text)
#print(translator.detect('good morning'))
#print(translator.detect('buenos dias'))

def translate_to_english(text):
  return translator.translate(text, dest='en').text


headlines = pd.read_csv('news.csv', index_col=None)
headlines['Translation'] = headlines['Headlines'].apply(translate_to_english)

headlines.to_csv('news_translated.csv')

print(headlines)