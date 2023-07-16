
def sorted_mans(ids):
    '''TASK_1'''
    s_id = []
    for id in ids.values():
        s_id.extend(id)
    return sorted(list(set(s_id)))

def length_of_searches(query):
    '''TASK_2'''
    #получаем длины запросов (в словах)
    measure_queries = [len(x.split(" ")) for x in query]
    #список уникальных длин запросов
    list_of_measures = list(set(measure_queries))
    #список, содержащий строки со сведениями о частоте введенных запросов (в процентах) разной длины
    result_list = [f'Поисковых запросов из {y} слов {round(measure_queries.count(y) / len(measure_queries) * 100, 2)} %' for y in list_of_measures]
    return '\n'.join(result_list)

def max_popular_market_channel(ts):
    '''TASK_3'''
    try:
        max_value = 0
        for val in ts.values():
            if val > max_value:
                max_value = val
#потенциально может быть несколько рекламных каналов с одинаковым (максимальным) объемом продаж
        res = [id for id, val in ts.items() if val == max_value]
    except:
        return 'Ошибка исполнения!'
    return ', '.join(res)

