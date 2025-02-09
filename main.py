from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS

model = Russian()

text = model("Фильм понравился, хорошие актёры, интересный сюжет, отличные спецэффекты.")

text_list = [i for i in text]
filter_stop_words = [i for i in text_list if i not in STOP_WORDS]
print(filter_stop_words)