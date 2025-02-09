from spacy.lang.ru import Russian

model = Russian()

text = model("Фильм понравился, хорошие актёры, интересный сюжет, отличные спецэффекты.")

text_list = [i for i in text]
