import os
# import nltk
# import textblob
from django.shortcuts import render
# from textblob import TextBlob
from collections import Counter
from .functions import get_discipline, get_discipline_ngram, get_category
from main.models import (Main, BI_PE, LAW, POLIT, M, E, HIST, Main_ngram, BI_PE_ngram, LAW_ngram, POLIT_ngram,
                         M_ngram, E_ngram, HIST_ngram, Main_pecase, school_pecase, uni_pecase, uni_pecase_fem,
                         uni_pecase_man, uni_pecase_mf, school_pecase_man, school_pecase_fem)
# import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import gutenberg, PlaintextCorpusReader
from nltk.text import Text
# from nltk import ngrams
# import django_filters
from .filters import WordFilter, NgramFilter, WordFilterPecase
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('gutenberg')

# Все дисциплины
url = 'C:/Users/Admin/HSE_CORPORA/main/static/PECLAP'
wordlists_all = PlaintextCorpusReader(url, '.*', encoding='cp1251')  # Все дисциплины
words_all = wordlists_all.words(fileids=wordlists_all.fileids())  # Все слова
raw_text_all = wordlists_all.raw()  # Весь текст
discipline = 'All'
category_pecase = 'All'

# Все полы pecase
url_pecase = 'C:/Users/Admin/HSE_CORPORA/main/static/PECASE'
wordlists_all_pecase = PlaintextCorpusReader(url_pecase, '.*', encoding='cp1251')  # Все полы и виды
words_all_pecase = wordlists_all_pecase.words(fileids=wordlists_all_pecase.fileids())  # Все слова
raw_text_all_pecase = wordlists_all_pecase.raw()  # Весь текст


# School
wordlists_pecase_sch = PlaintextCorpusReader(url_pecase, 'SCH.*', encoding='cp1251')  # SCH
words_pecase_sch = wordlists_pecase_sch.words(fileids=wordlists_pecase_sch.fileids())  # Все слова
raw_text_pecase_sch = wordlists_pecase_sch.raw()  # Весь текст

# School fem
wordlists_pecase_sch_fem = PlaintextCorpusReader(url_pecase, 'SCH-F.*', encoding='cp1251')  # SCH-F
words_pecase_sch_fem = wordlists_pecase_sch_fem.words(fileids=wordlists_pecase_sch_fem.fileids())  # Все слова
raw_text_pecase_sch_fem = wordlists_pecase_sch_fem.raw()  # Весь текст

# School man
wordlists_pecase_sch_man = PlaintextCorpusReader(url_pecase, 'SCH-M.*', encoding='cp1251')  # SCH-M
words_pecase_sch_man = wordlists_pecase_sch_man.words(fileids=wordlists_pecase_sch_man.fileids())  # Все слова
raw_text_pecase_sch_man = wordlists_pecase_sch_man.raw()  # Весь текст

# UNI
wordlists_pecase_uni = PlaintextCorpusReader(url_pecase, 'UNI.*', encoding='cp1251')  # UNI
words_pecase_uni = wordlists_pecase_uni.words(fileids=wordlists_pecase_uni.fileids())  # Все слова
raw_text_pecase_uni = wordlists_pecase_uni.raw()  # Весь текст

# UNI fem
wordlists_pecase_uni_fem = PlaintextCorpusReader(url_pecase, 'UNI-F.*', encoding='cp1251')  # SCH-F
words_pecase_uni_fem = wordlists_pecase_uni_fem.words(fileids=wordlists_pecase_uni_fem.fileids())  # Все слова
raw_text_pecase_uni_fem = wordlists_pecase_uni_fem.raw()  # Весь текст

# UNI man
wordlists_pecase_uni_man = PlaintextCorpusReader(url_pecase, 'UNI-M.*', encoding='cp1251')  # UNI-M
words_pecase_uni_man = wordlists_pecase_uni_man.words(fileids=wordlists_pecase_uni_man.fileids())  # Все слова
raw_text_pecase_uni_man = wordlists_pecase_uni_man.raw()  # Весь текст

# UNI mf
wordlists_pecase_uni_mf = PlaintextCorpusReader(url_pecase, 'UNI-B.*', encoding='cp1251')  # UNI-B
words_pecase_uni_mf = wordlists_pecase_uni_mf.words(fileids=wordlists_pecase_uni_mf.fileids())  # Все слова
raw_text_pecase_uni_mf = wordlists_pecase_uni_mf.raw()  # Весь текст


# БИ_ПИ
wordlists_BI = PlaintextCorpusReader(url, 'BI.*', encoding='cp1251')  # БИ_ПИ
words_BI = wordlists_BI.words(fileids=wordlists_BI.fileids())  # СЛОВА БИ_ПИ
raw_text_BI = wordlists_BI.raw()  # ТЕКСТ БИ_ПИ

# Эконом
wordlists_E = PlaintextCorpusReader(url, 'E.*', encoding='cp1251')  # Эконом
words_E = wordlists_E.words(fileids=wordlists_E.fileids())  # СЛОВА Эконом
raw_text_E = wordlists_E.raw()  # ТЕКСТ Эконом

# История
wordlists_HIST = PlaintextCorpusReader(url, 'HIST.*', encoding='cp1251')  # История
words_HIST = wordlists_HIST.words(fileids=wordlists_HIST.fileids())  # СЛОВА История
raw_text_HIST = wordlists_HIST.raw()  # ТЕКСТ История

# Юрист
wordlists_LAW = PlaintextCorpusReader(url, 'LAW.*', encoding='cp1251')  # Юрист
words_LAW = wordlists_LAW.words(fileids=wordlists_HIST.fileids())  # СЛОВА Юрист
raw_text_LAW = wordlists_LAW.raw()  # ТЕКСТ Юрист

# Менеджмент
wordlists_M = PlaintextCorpusReader(url, 'M.*', encoding='cp1251')  # Менеджмент
words_M = wordlists_M.words(fileids=wordlists_HIST.fileids())  # СЛОВА Менеджмент
raw_text_M = wordlists_M.raw()  # ТЕКСТ Менеджмент

# Политология
wordlists_POLIT = PlaintextCorpusReader(url, 'POLIT.*', encoding='cp1251')  # Политология
words_POLIT = wordlists_POLIT.words(fileids=wordlists_POLIT.fileids())  # СЛОВА Политология
raw_text_POLIT = wordlists_POLIT.raw()  # ТЕКСТ Политология

# Количество токенов и создание токенов
tokenizer = RegexpTokenizer(r'\w+')  # Токенизатор

tokens_all_pecase = tokenizer.tokenize(raw_text_all_pecase.lower())  # Все токены pecase
tokens_pecase_sch = tokenizer.tokenize(raw_text_pecase_sch.lower())
tokens_pecase_sch_fem = tokenizer.tokenize(raw_text_pecase_sch_fem.lower())
tokens_pecase_sch_man = tokenizer.tokenize(raw_text_pecase_sch_man.lower())
tokens_pecase_uni = tokenizer.tokenize(raw_text_pecase_uni.lower())
tokens_pecase_uni_fem = tokenizer.tokenize(raw_text_pecase_uni_fem.lower())
tokens_pecase_uni_man = tokenizer.tokenize(raw_text_pecase_uni_man.lower())
tokens_pecase_uni_mf = tokenizer.tokenize(raw_text_pecase_uni_mf.lower())

tokens_all = tokenizer.tokenize(raw_text_all.lower())  # Все токены
tokens_BI = tokenizer.tokenize(raw_text_BI.lower())  # ПИ_БИ токены
tokens_E = tokenizer.tokenize(raw_text_E.lower())  # Эконом токены
tokens_HIST = tokenizer.tokenize(raw_text_HIST.lower())  # История токены
tokens_LAW = tokenizer.tokenize(raw_text_LAW.lower())  # Юрист токены
tokens_M = tokenizer.tokenize(raw_text_M.lower())  # Менеджмент токены
tokens_POLIT = tokenizer.tokenize(raw_text_POLIT.lower())  # Политология токены

# Словарь с информацией о токенах
tokens_dict = dict()
tokens_dict['A'] = {'Name': 'Computer Science', 'Files': 59, 'Tokens': len(tokens_BI)}
tokens_dict['B'] = {'Name': 'Law', 'Files': 77, 'Tokens': len(tokens_LAW)}
tokens_dict['C'] = {'Name': 'Political Science', 'Files': 29, 'Tokens': len(tokens_POLIT)}
tokens_dict['D'] = {'Name': 'Management', 'Files': 58, 'Tokens': len(tokens_M)}
tokens_dict['E'] = {'Name': 'Economics', 'Files': 68, 'Tokens': len(tokens_E)}
tokens_dict['F'] = {'Name': 'History', 'Files': 43, 'Tokens': len(tokens_HIST)}

tokens_pecase_dict = dict()
tokens_pecase_dict['A'] = {'Name': 'School/College students', 'Files': 38, 'Tokens': len(tokens_pecase_sch), 'Male_files': 4,
                    'Male_tokens': len(tokens_pecase_sch_man), 'Female_files': 34,
                    'Female_tokens': len(tokens_pecase_sch_fem), "MF_files": 0, "MF_tokens": 0}
tokens_pecase_dict['B'] = {'Name': 'Undergraduate students', 'Files': 59, 'Tokens': len(tokens_pecase_uni), 'Male_files': 15,
                    'Male_tokens': len(tokens_pecase_uni_man), 'Female_files': 43,
                    'Female_tokens': len(tokens_pecase_uni_fem), "MF_files": 1, "MF_tokens": len(tokens_pecase_uni_mf)}
tokens_pecase_dict['C'] = {'Name': 'Total ', 'Files': 97, 'Tokens': len(tokens_all_pecase), 'Male_files': 19,
                    'Male_tokens': len(tokens_pecase_uni_man)+len(tokens_pecase_sch_man), 'Female_files': 77,
                    'Female_tokens': len(tokens_pecase_sch_fem)+len(tokens_pecase_uni_fem), "MF_files": 1,
                    "MF_tokens": len(tokens_pecase_uni_mf)}


# Количество токенов
tokens_all_len = len(tokens_all)
tokens_all_len_pecase = len(tokens_all_pecase)


# Словарь с информацией о текстах
raw_texts = dict()
raw_texts['All'] = raw_text_all.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')
raw_texts['Computer Science'] = raw_text_BI.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')
raw_texts['Law'] = raw_text_LAW.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' "').replace(':',' : ').replace('-', ' - ')
raw_texts['Political Science'] = raw_text_POLIT.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')
raw_texts['Management'] = raw_text_M.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')
raw_texts['Economics'] = raw_text_E.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')
raw_texts['History'] = raw_text_HIST.replace(',',' ,').replace('.',' .').replace(';',' ;').replace('?',' ?').replace('!',' !').replace('(',' ( ').replace(')',' )').replace("'"," '").replace('’',' ’').replace('"',' " ').replace(':',' : ').replace('-', ' - ')

# Main.objects.all().delete()
# Main_ngram.objects.all().delete()
# Main_pecase.objects.all().delete()

def home(request):
    return render(request, 'home.html')


def peclap_kwic(response):  # Concordance
    if response.method == 'GET':
        discipline = response.GET.get('disciplines')
        if discipline is None:
            discipline = 'All'
        text = Text(list(raw_texts[discipline].split(' ')))
        query_word = response.GET.get('word')  # Слово для поиска конкорданса
        if query_word is None:
            query_word = ''
    else:
        text = Text(list(raw_text_all.split(' ')))
        query_word = ''
        discipline = 'All'
    query_word = list(query_word.split(' '))
    concordances = text.concordance_list(query_word, lines=100000, )
    result = len(concordances)
    print(result)
    query_word = ' '.join(query_word)
    return render(response, 'peclap_kwic.html', context={'concordances': concordances, 'result': result,
                                                         'discipline': discipline, 'query_word': query_word})

def peclap_info(request):
    return render(request, 'peclap_info.html', context={'tokens': tokens_all_len,
                                                        'tokens_dict': tokens_dict})


def peclap_word(response):
    current_info = Main.objects.all()
    if response.method == "GET":
        discipline = response.GET.get('disciplines')
        current_info = get_discipline(discipline)
    else:
        discipline = 'All'
    words = current_info
    myFilter = WordFilter(response.GET, queryset=words)
    words = myFilter.qs
    return render(response, 'peclap_word.html', context={'results':len(words),'discipline':discipline,
                                                                        'words':words, 'myFilter': myFilter })


def peclap_ngram(response):
    current_info = Main_ngram.objects.filter(ngram=3)
    if response.method == "GET":
        discipline = response.GET.get('disciplines')
        ngrams = response.GET.get('n_gram_size')
        if ngrams is None:
            ngrams = 3
        current_info = get_discipline_ngram(discipline, int(ngrams))
    else:
        discipline = 'All'
        ngrams = 3
    words = current_info
    myFilter = NgramFilter(response.GET, queryset=words)
    words = myFilter.qs

    return render(response, 'peclap_ngram.html', context={'results':len(words),'discipline':discipline,
                                                                        'words':words, 'myFilter': myFilter, 'size': ngrams })


def pecase_kwic(response): # Concordance
    if response.method == 'GET':
        discipline = response.GET.get('disciplines')
        if discipline is None:
            discipline = 'All'
        text = Text(list(raw_texts[discipline].split(' ')))
        query_word = response.GET.get('word')  # Слово для поиска конкорданса
        if query_word is None:
            query_word = ''
    else:
        text = Text(list(raw_text_all.split(' ')))
        query_word = ''
        discipline = 'All'
    query_word = list(query_word.split(' '))
    concordances = text.concordance_list(query_word, lines=100000, )
    result = len(concordances)
    print(result)
    query_word = ' '.join(query_word)
    return render(response, 'pecase_kwic.html', context={'concordances': concordances, 'result': result,
                                                         'discipline': discipline, 'query_word': query_word})


def pecase_info(request):
    return render(request, 'pecase_info.html', context={'tokens': tokens_all_len_pecase,
                                                        'tokens_dict': tokens_pecase_dict})


def pecase_word(response):
    current_info = Main_pecase.objects.all()
    if response.method == "GET":
        category_pecase = response.GET.get('category')
        current_info = get_category(category_pecase)
    else:
        category_pecase = 'All'
    words = current_info
    myFilter_pecase = WordFilterPecase(response.GET, queryset=words)
    words = myFilter_pecase.qs
    return render(response, 'pecase_word.html', context={'results': len(words), 'category': category_pecase,
                                                                        'words': words, 'myFilter': myFilter_pecase})


def pecase_ngram(response):
    current_info = Main_ngram.objects.filter(ngram=3)
    ngrams = 3
    if response.method == "GET":
        discipline = response.GET.get('disciplines')
        ngrams = response.GET.get('n_gram_size')
        if ngrams is None:
            ngrams = 3
        current_info = get_discipline_ngram(discipline, int(ngrams))
    else:
        discipline = 'All'
        ngrams = 3
    words = current_info
    myFilter = NgramFilter(response.GET, queryset=words)
    words = myFilter.qs

    return render(response, 'pecase_ngram.html', context={'results':len(words),'discipline':discipline,
                                                                        'words':words, 'myFilter': myFilter, 'size': ngrams })