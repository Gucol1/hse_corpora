from .models import Main, BI_PE, E, M, HIST, LAW, POLIT

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