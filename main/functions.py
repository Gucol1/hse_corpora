from main.models import (Main, BI_PE, LAW, POLIT, M, E, HIST, Main_ngram, BI_PE_ngram, LAW_ngram, POLIT_ngram,
                         M_ngram, E_ngram, HIST_ngram, school_pecase_fem, school_pecase_man,school_pecase, uni_pecase,
                         uni_pecase_fem, uni_pecase_man, uni_pecase_mf, Main_pecase, uni_pecase_ngram,
                         school_pecase_ngram, school_pecase_fem_ngram, school_pecase_man_ngram, uni_pecase_mf_ngram,
                         uni_pecase_fem_ngram, uni_pecase_man_ngram, Main_pecase_ngram)

def get_discipline(discipline):
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
        current_info = Main.objects.all()
    return current_info


def get_category(category):
    if category == 'School/College Students':
        current_info = school_pecase.objects.all()
    elif category == 'School/College Females':
        current_info = school_pecase_fem.objects.all()
    elif category == 'School/College Males':
        current_info = school_pecase_man.objects.all()
    elif category == 'Undergraduate Students':
        current_info = uni_pecase.objects.all()
    elif category == 'Undergraduate Females':
        current_info = uni_pecase_fem.objects.all()
    elif category == 'Undergraduate Males':
        current_info = uni_pecase_man.objects.all()
    elif category == 'Undergraduate Males&Females':
        current_info = uni_pecase_mf.objects.all()
    else:
        current_info = Main_pecase.objects.all()
    return current_info


def get_discipline_ngram(discipline, ngrams):
    if discipline == 'Computer Science':
        current_info = BI_PE_ngram.objects.all().filter(ngram=ngrams)
    elif discipline == 'Economics':
        current_info = E_ngram.objects.all().filter(ngram=ngrams)
    elif discipline == 'Management':
        current_info = M_ngram.objects.all().filter(ngram=ngrams)
    elif discipline == 'History':
        current_info = HIST_ngram.objects.all().filter(ngram=ngrams)
    elif discipline == 'Law':
        current_info = LAW_ngram.objects.all().filter(ngram=ngrams)
    elif discipline == 'Political Science':
        current_info = POLIT_ngram.objects.all().filter(ngram=ngrams)
    else:
        current_info = Main_ngram.objects.all().filter(ngram=ngrams)
    return current_info

def get_category_ngram(category, ngrams):
    if category == 'School/College Students':
        current_info = school_pecase_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'School/College Females':
        current_info = school_pecase_fem_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'School/College Males':
        current_info = school_pecase_man_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'Undergraduate Students':
        current_info = uni_pecase_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'Undergraduate Females':
        current_info = uni_pecase_fem_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'Undergraduate Males':
        current_info = uni_pecase_man_ngram.objects.all().filter(ngram=ngrams)
    elif category == 'Undergraduate Males&Females':
        current_info = uni_pecase_mf_ngram.objects.all().filter(ngram=ngrams)
    else:
        current_info = Main_pecase_ngram.objects.all().filter(ngram=ngrams)
    return current_info

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

# #Пропорция для подсчёта нормализованного интервала и частотности
# proportion = 1000000/tokens_all_len
# proportion_BI = 1000000/len(tokens_BI)
# proportion_M = 1000000/len(tokens_M)
# proportion_E = 1000000/len(tokens_E)
# proportion_HIST = 1000000/len(tokens_HIST)
# proportion_POLIT = 1000000/len(tokens_POLIT)
# proportion_LAW = 1000000/len(tokens_LAW)


# n-грамы

    # n = 6 # ТУТ МЕНЯТЬ
    # n_grams = ngrams(raw_text_pecase_uni_mf.split(), n) # ТУТ МЕНЯТЬ
    # new_n_grams = []
    # for grams in n_grams:
    #     if (('.' or ',' or '?' or '!' or ':' or ';' or '-' or '' not in grams[0]) and
    #     ('.' or ',' or '?' or '!' or ':' or ';' or '-' or '' not in grams[1])
    #     and ('.' or ',' or '?' or '!' or ':' or ';' or '-' or '' not in grams[2])
    #     and ('.' or ',' or '?' or '!' or ':' or ';' or '-' or '' not in grams[3])
    #     and ('.' or ',' or '?' or '!' or ':' or ';' or '-' or '' not in grams[4])):
    #         grams = list(grams)
    #         raw = " ".join(grams)
    #         grams[0] = (grams[0].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!','')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams[1] = (grams[1].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!','')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams[2] = (grams[2].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!','')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams[3] = (grams[3].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!','')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams[4] = (grams[4].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!','')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams[5] = (grams[5].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!', '')
    #                     .replace('(', '').replace(')', '').replace('"', '').replace(':', '').replace('-', ''))
    #         grams = ' '.join(grams)
    #         grams = grams.lower()
    #         new_n_grams.append(grams)
    #
    # frequency_list = Counter(new_n_grams)
    # number, rank, count, frequency = 1, 1, 0, 0
    # sorted_frequency = sorted(frequency_list.items(), key=lambda item: item[1], reverse=True)
    #
    #
    # ngram_proportion = 1000000/len(tokens_pecase_uni_mf)  # Тут менять
    #
    # for elem in sorted_frequency:
    #     prev = frequency
    #     word = elem[0]
    #     frequency = elem[1]
    #     wordlist = wordlists_pecase_uni_mf.fileids()  # ТУТ МЕНЯТЬ
    #     for filename in wordlist:
    #         file = open(os.path.join(url_pecase, filename), 'r', encoding='cp1251')
    #         text = file.read().lower().replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!',
    #                                                                                                       '').replace(
    #             '(', '').replace(')', '').replace('"', '').replace(':', '').replace(
    #             '-', '')
    #
    #         if word in text:
    #             count += 1
    #             continue
    #
    #
    #     if prev == frequency:
    #         rank = rank
    #     else:
    #         rank = number
    #     number += 1
    #
    #     if count>int(frequency):
    #         count = frequency
    #
    #     word_obj = uni_pecase_mf_ngram.objects.create(text = word, rank = rank, frequency = frequency,  # ТУТ МЕНЯТЬ
    #                                                       range = count,
    #                                                       normalized_freq=(ngram_proportion*float(frequency)).__round__(2),
    #                                                       normalized_range=(float(count)/len(wordlist)).__round__(2),
    #                                                       ngram=n)
    #     word_obj.save()
    #
    #
    #     count = 0