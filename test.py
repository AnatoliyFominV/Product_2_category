from fasttext import load_model
import streamlit as st
import os
from gensim.utils import simple_preprocess
import wget


# Download model
model_name = "model.bin"
model_url = "https://drive.google.com/file/d/1-7ZNbPdwBifcKFScNjb1GEop4gTyVEkc/view?usp=sharing"
dir_path = os.path.dirname(os.path.realpath(__file__))
# file_model = wget.download(model_url, out=model_name)

# Import model to FastText
path = dir_path + "\\" + model_name
# model = load_model(path)
model = load_model(model_name)
# Decrypto prediction to category name
category_file_name = "\\path_to_end_category.txt"
path_to_end_category = {}
with open(dir_path + category_file_name, encoding='utf8') as file:
    for line in file:
        key, value = line.split("_/_")
        path_to_end_category[int(key)] = value


def make_prediction(corpus):
    corpus = " ".join(simple_preprocess(corpus))
    res = int(model.predict(corpus)[0][0][9:])
    if res in path_to_end_category.keys():
        ans = path_to_end_category[res]
    else:
        ans = "Категория для товара отстутвует"

    return ans


print(make_prediction("Кальсоны"))

