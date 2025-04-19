import pandas as pd
import random

def load_data_from_excel():
    file_path = "database//words.xlsx"
    data = pd.read_excel(file_path)
    return data

def data_size():
    return len(load_data_from_excel())

def get_random_number():
    size = data_size()
    return random.randint(0, size - 1)

def get_english_word(ID):
    data = load_data_from_excel()
    eng_word = data.loc[data['ID'] == ID, "ENGLISH"]
    return ''.join(eng_word.to_list())
    
def get_czech_word(ID):
    data = load_data_from_excel()
    czech_word = data.loc[data['ID'] == ID, "CZECH"]
    return ''.join(czech_word.to_list())