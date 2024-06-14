import os
import textblob as tb
from django.shortcuts import render
from textblob import TextBlob
from collections import Counter
from .models import Main
import nltk
import pymorphy3
# nltk.download('wordnet')
# nltk.download('punkt')

# Create your views here.

url = 'C:/Users/Admin/HSE_CORPORA/main/static/PECLAP'
info = ''
raw_info = []

for filename in os.listdir(url):
    folder_url = os.path.join(url, filename)
    count = 0
    if filename == 'BI_PE':
        count = 58
    elif filename == 'E':
        count = 68
    elif filename == 'HIST':
        count = 43
    elif filename == 'LAW':
        count = 77
    elif filename == 'M':
        count = 58
    elif filename == 'POLIT':
        count = 29
    for i in range(1, count + 1):
        file = os.path.join(folder_url, filename)
        name = file + ' (' + str(i) + ').txt'
        # print(name)
        with open(name, 'r') as f:
            lines = f.readlines()
            # print(lines)
            lines = ' '.join(lines)
            raw_info.append(lines)
            info += lines
info = info.lower()
tokens = 676301
proportion = 1000000/676301



def word_frequencies(words):
    return Counter(words)



def home(request):
    current_info = Main.objects.all()
    # info_info = []
    # words = TextBlob(info)
    # words = words.words
    # current_info = word_frequencies(words)
    # sorted_keys = sorted(current_info.keys(), key=current_info.get, reverse=True)
    # for key in sorted_keys:
    #     # print(key + ': ' + str(current_info[key]))
    #     info_info.append(str(key)+' '+str(current_info[key]))
    #
    # current_info = info_info
    # # print(current_info)
    # number = 1
    # rank = 1
    # count = 0
    # frequency = 0
    # for i in range(len(current_info)):
    #     prev = frequency
    #     word = current_info[i]
    #     curr_word = word.split(' ')[0]
    #     if curr_word.isalpha():
    #         for text in raw_info:
    #             text = text.lower()
    #             if curr_word in text:
    #                 count += 1
    #                 continue
    #
    #         word += ' '+str(count)
    #         current_info[i] = word
    #         frequency = word.split(' ')[1]
    #         if prev == frequency:
    #             rank = rank
    #         else:
    #             rank = number
    #         number += 1
    #
    #         if count>int(frequency):
    #             count = frequency
    #         word_obj = Main.objects.create(word = curr_word, rank = rank, frequency = frequency, range = count,
    #                                        normalized_freq=proportion*int(frequency),normalized_range=proportion*int(count))
    #         word_obj.save()
    #     count = 0
    return render(request, 'home.html', context={'current_info': current_info})

def peclap(request):
    current_info = Main.objects.all()
    return render(request, 'peclap.html', context={'current_info': current_info})