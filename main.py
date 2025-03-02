from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
from translate import Translator

model = ru_core_news_md.load()

text = model("авось Фильм понравился, хорошие актёры, интересный сюжет, отличные спецэффекты. казались")

text_list = [i.lemma_ for i in text]

filter_stop_words = [i for i in text_list if i not in STOP_WORDS]

translator = Translator(from_lang="ru", to_lang="en")  # Объект для перевода
translate_text = translator.translate(str(filter_stop_words))  # Переводим текст

analysis = TextBlob(translate_text)  # Анализируем текст
print(analysis)
sentiment = analysis.sentiment.polarity  # -1 - отрицательный, 0 - нейтральный, 1 - положительный
print(sentiment)

if sentiment > 0:
    print("положительный")
elif sentiment < 0:
    print("отрицательный")
else:
    print("нейтральный")