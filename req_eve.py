import requests as r
import random

auth=('volkov.denis.vad@yandex.ru','hgJH768Cv23')
collection='http://rest.test.ivi.ru/v2/character'

json_schema={'education': {'type': str, 'min_len': 3, 'max_len': 340, 'may': []},
            'height': {'type': int, 'min': 76, 'max': 1827, 'may': []},
            'identity': {'type': str, 'min_len': 4, 'max_len': 350, 'may': []},
            'name': {'type': str, 'min_len': 3, 'max_len': 350, 'may': [],'required':True},
            'other_aliases': {'type': str, 'min_len': 3, 'max_len': 350, 'may': []},
            'universe': {'type': str, 'min_len': 9, 'max_len': 350, 'may': []},
            'weight': {'type':float, 'min': 0.45, 'max': 855.0, 'may': [{'type': str, 'value': 'Unrevealed'}]}}

limit="Collection can't contain more than 500 items"

data_positive_create_characters={}

data_negative_create_characters={
    'education': [{'value': 494, 'data': 'nmnn is already exists'}],
    'height': [{'value': 2568, 'data': 'mmee is already exists'}],
    'identity': [{'value': 546, 'data': "identity: ['Length must be between 1 and 350.']"}],
    'name': [{'value': 654, 'data': "name: ['Length must be between 1 and 350.']"}],
    'other_aliases': [{'value': 389, 'data': "other_aliases: ['Length must be between 1 and 350.']"}],
    'universe': [{'value': 658, 'data': "universe: ['Length must be between 1 and 350.']"}],
    'weight': []}

def len_all_collection():
    url='http://rest.test.ivi.ru/v2/characters'
    req=r.get(url,auth=auth)
    result=len(req.json()['result'])
    return result


def parse(url):
    result=r.get(url,auth=auth)
    return result

def handler_form(parse):
    results=[el for el in parse.json()['result']]
    for hero in results:
        for property in hero:
            if property not in json_schema:
                json_schema[property]={}
                if type(hero[property])==str:
                    json_schema[property]['type']=str
                    json_schema[property]['min_len']= len(hero[property])
                    json_schema[property]['max_len'] = len(hero[property])
                else:
                    json_schema[property]['type']=type(hero[property])
                    json_schema[property]['min'] = hero[property]
                    json_schema[property]['max'] = hero[property]
                json_schema[property]['may'] = []
            else:
                if type(hero[property])!=json_schema[property]['type']:
                    may={'type':type(hero[property]),'value':hero[property]}
                    if may not in json_schema[property]['may']:
                        json_schema[property]['may'].append(may)
                elif type(hero[property])==str:
                    if len(hero[property])>json_schema[property]['max_len']:
                        json_schema[property]['max_len']=len(hero[property])
                    if len(hero[property])<json_schema[property]['min_len']:
                        json_schema[property]['min_len']=len(hero[property])
                else:
                    if hero[property]>json_schema[property]['max']:
                        json_schema[property]['max']=hero[property]
                    if hero[property]<json_schema[property]['min']:
                        json_schema[property]['min']=hero[property]

def random_data_characters():
    json={}
    for i in json_schema:
        if json_schema[i]['type']==str:
            json[i]=''.join([random.choice(i) for _ in range(random.randint(json_schema[i]['min_len'],json_schema[i]['max_len']))])
        elif json_schema[i]['type']==int:
            json[i]=random.randint(json_schema[i]['min'],json_schema[i]['max'])
        else:
            json[i]=json_schema[i]['min']
    return json

def create_characters(data=None):
    headers={
        'Content-type': 'application/json'
    }
    if data is None:
        data=random_data_characters()
    result=r.post(collection,json=data,auth=auth,headers=headers)
    return result

def reset_db():
    url='http://rest.test.ivi.ru/v2/reset'
    result=r.post(url,auth=auth)
    return result


def write_result(data):
    file='result.txt'
    with open(file,mode='w',encoding='utf-8') as f:
        f.write(data)
    return

def construct_test_case():
    for property in json_schema:
        if property not in data_negative_create_characters:
            data_negative_create_characters[property]=[]
        if json_schema[property]['type']==str:
            for len in ['max_len','min_len']:
                    if len=='max_len':
                        for i in range(1000):
                            test_property='t'*(json_schema[property][len]+i)
                            data=random_data_characters()
                            data[property]=test_property
                            result=create_characters(data)
                            if result.status_code != 200:
                                if result.json()['error'] == limit:
                                    reset_db()
                                else:
                                    json_schema[property][len]=json_schema[property][len]+i-1
                                    test_case={
                                            'value':json_schema[property][len]+i,
                                            'data':result.json()['error']
                                        }
                                    data_negative_create_characters[property].append(test_case)
                                    print(
                                            f'Добавлен негативный тест-кейс для {property} значение {json_schema[property][len] + i}')
                                    print(f'Схема : {json_schema}')
                                    print(f'Тест кейсы: {data_negative_create_characters}')
                                    break
                    if len == 'min_len':
                        for i in range(json_schema[property][len]):
                            test_property = 't' * (json_schema[property][len] - i)
                            data = random_data_characters()
                            data[property] = test_property
                            result = create_characters(data)
                            if result.status_code != 200:
                                if result.json()['error'] == limit:
                                    reset_db()
                                else:
                                    json_schema[property][len] = json_schema[property][len] - i + 1
                                    test_case = {
                                            'value': json_schema[property][len] + i,
                                            'data': result.json()['error']
                                        }
                                    data_negative_create_characters[property].append(test_case)
                                    print(
                                            f'Добавлен негативный тест-кейс для {property} значение {json_schema[property][len] - i}')
                                    print(f'Схема : {json_schema}')
                                    print(f'Тест кейсы: {data_negative_create_characters}')
                                    break
        elif json_schema[property]['type']==int:
            for len in ['max','min']:
                    if len=='max':
                        for i in range(1000):
                            test_property=json_schema[property][len]+i
                            data=random_data_characters()
                            data[property]=test_property
                            result=create_characters(data)
                            if result.status_code != 200:
                                if result.json()['error'] == limit:
                                    reset_db()
                                else:
                                    json_schema[property][len]=json_schema[property][len]+i-1
                                    test_case={
                                            'value':json_schema[property][len]+i,
                                            'data':result.json()['error']
                                        }
                                    data_negative_create_characters[property].append(test_case)
                                    print(f'Добавлен негативный тест-кейс для {property} значение {json_schema[property]["max"]+i}')
                                    print(f'Схема : {json_schema}')
                                    print(f'Тест кейсы: {data_negative_create_characters}')
                                    break
                    if len == 'min_len':
                        for i in range(json_schema[property][len]):
                            test_property = json_schema[property][len] - i
                            data = random_data_characters()
                            data[property] = test_property
                            result = create_characters(data)
                            if result.status_code != 200:
                                if result.json()['error'] == limit:
                                    reset_db()
                                else:
                                    json_schema[property][len] = json_schema[property][len] - i + 1
                                    test_case = {
                                            'value': json_schema[property][len] + i,
                                            'data': result.json()['error']
                                        }
                                    data_negative_create_characters[property].append(test_case)
                                    print(
                                            f'Добавлен негативный тест-кейс для {property} значение {json_schema[property]["min"] - i}')
                                    print(f'Схема : {json_schema}')
                                    print(f'Тест кейсы: {data_negative_create_characters}')
                                    break
        else:
            for len in ['max','min']:
                    if len=='max':
                        for i in range(1000):
                            test_property=json_schema[property][len]+i
                            data=random_data_characters()
                            data[property]=test_property
                            result=create_characters(data)
                            if result.status_code != 200:
                                if result.json()['error'] == limit:
                                    reset_db()
                                else:
                                    json_schema[property][len]=json_schema[property][len]+i-1
                                    test_case={
                                        'value':json_schema[property][len]+i,
                                        'data':result.json()['error']
                                    }
                                    data_negative_create_characters[property].append(test_case)
                                    print(f'Добавлен негативный тест-кейс для {property} значение {json_schema[property]["max"]+i}')
                                    print(f'Схема : {json_schema}')
                                    print(f'Тест кейсы: {data_negative_create_characters}')
                                    break


print(len_all_collection())

