import os
import nltk
import textblob
from django.shortcuts import render
from textblob import TextBlob
from collections import Counter
from .functions import fill_peclap_info
from .models import Main, BI_PE, LAW, POLIT, M, E, HIST
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import gutenberg, PlaintextCorpusReader
from nltk.text import Text
import django_filters
from .filters import WordFilter
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('gutenberg')

# Create your views here.

#Все дисциплины
url = 'C:/Users/Admin/HSE_CORPORA/main/static/PECLAP'
wordlists_all = PlaintextCorpusReader(url, '.*', encoding='cp1251') # Все дисциплины
words_all = wordlists_all.words(fileids=wordlists_all.fileids()) # Все слова
raw_text_all = wordlists_all.raw() # Весь текст
discipline = 'All'

#БИ_ПИ
wordlists_BI = PlaintextCorpusReader(url, 'BI.*', encoding='cp1251') # БИ_ПИ
words_BI = wordlists_BI.words(fileids=wordlists_BI.fileids()) # СЛОВА БИ_ПИ
raw_text_BI = wordlists_BI.raw() # ТЕКСТ БИ_ПИ

#Эконом
wordlists_E = PlaintextCorpusReader(url, 'E.*', encoding='cp1251') # Эконом
words_E = wordlists_E.words(fileids=wordlists_E.fileids()) # СЛОВА Эконом
raw_text_E = wordlists_E.raw() # ТЕКСТ Эконом

#История
wordlists_HIST = PlaintextCorpusReader(url, 'HIST.*', encoding='cp1251') # История
words_HIST = wordlists_HIST.words(fileids=wordlists_HIST.fileids()) # СЛОВА История
raw_text_HIST = wordlists_HIST.raw() # ТЕКСТ История

#Юрист
wordlists_LAW = PlaintextCorpusReader(url, 'LAW.*', encoding='cp1251') # Юрист
words_LAW = wordlists_LAW.words(fileids=wordlists_HIST.fileids()) # СЛОВА Юрист
raw_text_LAW = wordlists_LAW.raw() # ТЕКСТ Юрист

#Менеджмент
wordlists_M = PlaintextCorpusReader(url, 'M.*', encoding='cp1251') # Менеджмент
words_M = wordlists_M.words(fileids=wordlists_HIST.fileids()) # СЛОВА Менеджмент
raw_text_M = wordlists_M.raw() # ТЕКСТ Менеджмент

#Политология
wordlists_POLIT = PlaintextCorpusReader(url, 'POLIT.*', encoding='cp1251') # Политология
words_POLIT = wordlists_POLIT.words(fileids=wordlists_POLIT.fileids()) # СЛОВА Политология
raw_text_POLIT = wordlists_POLIT.raw() # ТЕКСТ Политология

#Количество токенов и создание токенов
tokenizer = RegexpTokenizer(r'\w+') # Токенизатор

tokens_all = tokenizer.tokenize(raw_text_all.lower()) # Все токены
tokens_BI = tokenizer.tokenize(raw_text_BI.lower()) # ПИ_БИ токены
tokens_E = tokenizer.tokenize(raw_text_E.lower()) # Эконом токены
tokens_HIST = tokenizer.tokenize(raw_text_HIST.lower()) # История токены
tokens_LAW = tokenizer.tokenize(raw_text_LAW.lower()) # Юрист токены
tokens_M = tokenizer.tokenize(raw_text_M.lower()) # Менеджмент токены
tokens_POLIT = tokenizer.tokenize(raw_text_POLIT.lower()) # Политология токены

#Словарь с информацией о токенах
tokens_dict = dict()
tokens_dict['A'] = {'Name':'Computer Science','Files':59,'Tokens':len(tokens_BI)}
tokens_dict['B'] = {'Name':'Law','Files':77,'Tokens':len(tokens_LAW)}
tokens_dict['C'] = {'Name':'Political Science','Files':29,'Tokens':len(tokens_POLIT)}
tokens_dict['D'] = {'Name':'Management','Files':58,'Tokens':len(tokens_M)}
tokens_dict['E'] = {'Name':'Economics','Files':68,'Tokens':len(tokens_E)}
tokens_dict['F'] = {'Name':'History','Files':43,'Tokens':len(tokens_HIST)}

#Количество токенов
tokens_all_len = len(tokens_all)

#Пропорция для подсчёта нормализованного интервала и частотности
proportion = 1000000/tokens_all_len
proportion_BI = 1000000/len(tokens_BI)
proportion_M = 1000000/len(tokens_M)
proportion_E = 1000000/len(tokens_E)
proportion_HIST = 1000000/len(tokens_HIST)
proportion_POLIT = 1000000/len(tokens_POLIT)
proportion_LAW = 1000000/len(tokens_LAW)

# Main.objects.all().delete()

def home(request):
    # frequency_list = Counter(tokens_LAW) # Частоты слов ТУТ МЕНЯТЬ
    # # print(frequency_list)
    # current_info = frequency_list
    # number, rank, count, frequency = 1, 1, 0, 0
    # sorted_frequency = sorted(frequency_list.items(), key=lambda item: item[1], reverse=True)
    #
    # # print(sorted_frequency) # Частоты
    # # print(wordlists_all.fileids()) # Названия всех файлов
    #
    # for elem in sorted_frequency:
        # prev = frequency
        # word = elem[0]
        # frequency = elem[1]
        # for filename in wordlists_LAW.fileids(): # ТУТ МЕНЯТЬ
        #     file = open(os.path.join(url, filename), 'r', encoding='cp1251')
        #     text = file.read().lower()
        #     # print(tokens)
        #     if word in text:
        #         count += 1
        #         continue
        #
        # # print(word, count)
        #
        # if prev == frequency:
        #     rank = rank
        # else:
        #     rank = number
        # number += 1
        #
        # if count>int(frequency):
        #     count = frequency
        #
        # word_obj = LAW.objects.create(word = word, rank = rank, frequency = frequency, range = count, # ТУТ МЕНЯТЬ
        #                                normalized_freq=(proportion_LAW*float(frequency)).__round__(2), # ТУТ МЕНЯТЬ
        #                                 normalized_range=(float(count)/len(wordlists_LAW.fileids())).__round__(2)) # ТУТ МЕНЯТЬ
        # word_obj.save()
        #
        # count = 0

    return render(request, 'home.html')

def peclap(request): # Concordance
    text = Text(list(raw_text_all.split(' ')))
    query_word = 'puppets' # Слово для поиска конкорданса
    current_info = text.concordance_list(query_word, lines=100000)
    concordances_length = len(current_info) # Количество контекстов
    return render(request, 'peclap.html', context={'current_info': current_info,
                                                   'concordances_length':concordances_length})

def peclap_info(request):
    return render(request, 'peclap_info.html', context={'tokens': tokens_all_len,
                                                        'tokens_dict': tokens_dict})



def peclap_word(response):
    current_info = Main.objects.all()
    if response.method == "GET":
        discipline = response.GET.get('disciplines')
        if discipline == 'Computer Science':
            current_info = BI_PE.objects.all()
        elif discipline == 'Economics':
            current_info = E.objects.all()
        elif discipline == 'Management':
            current_info = M.objects.all()
        elif discipline == 'History':
            current_info = HIST.objects.all()
        elif discipline == 'Law':
            current_info = LAW.objects.all()
        elif discipline == 'Political Science':
            current_info = POLIT.objects.all()
    else:
        discipline = 'All'
    print(discipline)
    words = current_info
    myFilter = WordFilter(response.GET, queryset=words)
    words = myFilter.qs
    results = len(words)

    return render(response, 'peclap_word.html', context={'current_info': current_info,'results':results,
                                                         'discipline':discipline, 'words':words, 'myFilter': myFilter })