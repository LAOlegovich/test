
from main import  sorted_mans, length_of_searches, max_popular_market_channel

import pytest

@pytest.mark.parametrize (
        "input, testing_output",
        [
        ({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]},
       [15,35,54,98,119,213]
       ) ,
       ({'user1': [12,12,15,17],
       'user2': [21,24,25,25],
       'user3': [34,56,33]},
       [12,15,17,21,24,25,33,34,56]
       )
        ]
)
def test_sorted_mans(input, testing_output):
    res = sorted_mans(input)
    assert res == testing_output



@pytest.mark.parametrize (
    "input, testing_output",
    [
       ([
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
],
'Поисковых запросов из 2 слов 42.86 %\
\nПоисковых запросов из 3 слов 57.14 %'),
 ([
     'футбол',
     'программирование в VS Code',
     'тестирование с помощью pytest',
     'гонка ф-1',
     'телепрограмма'
 ],
'Поисковых запросов из 1 слов 40.0 %\
\nПоисковых запросов из 2 слов 20.0 %\
\nПоисковых запросов из 4 слов 40.0 %'
 )
    ]
)
def test_length_of_searches(input,testing_output):
    res = length_of_searches(input)
    assert res == testing_output




@pytest.mark.parametrize (
    "input, testing_output",
    [
        ({
    'facebook': 55,
    'yandex': 120,
    'vk' : 115,
    'google' : 99,
    'email' : 42,
    'ok' : 98   
}, 
'yandex'),
    (
      {
    'facebook': 55,
    'yandex': 120,
    'tik-tok':120,
    'vk' : 115,
    'google' : 99,
    'email' : 42,
    'ok' : 98   
},  
  'yandex, tik-tok'),
  (
      {
    'facebook': 55,
    'yandex': 35,
    'vk' : 115,
    'google' : 99,
    'email' : 42,
    'ok' : 98   
},
 'vk' )
    ]
)
def test_max_popular_market_channel(input,testing_output):
    res = max_popular_market_channel(input)
    assert res == testing_output

 
    
@pytest.mark.xfail
def test_failed_max_popular_market_channel(input = ['facebook',55,'vk',15]):
    res = max_popular_market_channel(input)
    testing_output = 'facebook'
    assert res == testing_output


