from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md

model = ru_core_news_md.load()

text = model("авось Фильм понравился, хорошие актёры, интересный сюжет, отличные спецэффекты. казались")

text_list = [i.lemma_ for i in text]


filter_stop_words = [i for i in text_list if i not in STOP_WORDS]