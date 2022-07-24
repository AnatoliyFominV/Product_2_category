from fasttext import load_model
import streamlit as st
import os
from gensim.utils import simple_preprocess
import wget


@st.cache(allow_output_mutation=True)
def download_model():
    # Download model
    model_name = "model.bin"
    model_url = "https://drive.google.com/file/d/1-7ZNbPdwBifcKFScNjb1GEop4gTyVEkc/view?usp=sharing"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_model = wget.download(model_url, out=model_name)

    # Import model to FastText
    path = dir_path + "/" + model_name
    model = load_model(model_name)

    # Decrypto prediction to category name
    category_file_name = "/path_to_end_category.txt"
    path_to_end_category = {}
    with open(dir_path + category_file_name, encoding='utf8') as file:
        for line in file:
            key, value = line.split("_/_")
            path_to_end_category[int(key)] = value


download_model()


def make_prediction(corpus):
    corpus = simple_preprocess(corpus)
    res = model.predict(corpus)
    if res in path_to_end_category.keys():
        ans = path_to_end_category[res[0]]
    else:
        ans = "Категория для товара отстутвует"

    return ans


# _______________________Web________________________________________ #
# _______________________Title_____________________________________ #
st.title("Предскажем категорию товара по его названию и описанию")
st.write(
    """ 
    **Автор** Фомин Анатолий Витальевич   
    **Контактные данные** +7(926)4395526, kmno4.172@gmail.com   
    **Цель** Помочь продавцам сориентироваться среди тысяч категорий   
    ***
    """)

# _______________________Page_Layout______________________________ #
col2, col3 = st.columns((10, 1))

st.text_input(
    label="Введи название и описание товара",
    value=""

)

# Предсказать КИН по данным:
pred = predict_1(dist=federal_distr, pvt=pvt, carbonate=is_carbonate, por=por, perm=perm, visc=visc)
# print("Предсказанный КИН:", pred)

st.write(
    f""" ## Предсказанный КИН на основании месторождений аналогов: {pred:.2f}
    """
)
