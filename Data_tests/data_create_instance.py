
"""
Файл для хранения тест-кейсов по созданию экземпляров.

1.Структура positive тест-кейса:

    "Название тестируемого свойства" :[ {"value": "Значение для тестируемого свойства"}]

    Ожидаемый результат : Результат запроса с данными имеет код ответа - 200.

2.Структура negative тест-кейса:

    "Название тестируемого свойства" :[ {"value": "Значение для тестируемого свойства",
                                        "error": "Значение ожидаемого хеддера"}]

    Ожидаемый результат :  Результат запроса с данными имеет код ответа - 400 ,
                             error в body ответа  равен значению error в тест-кейсе.

3.Структура duplicate тест-кейса:

    "Название тестируемого свойства" :[ {case1 (Первый экземпляр):
                                        {"value": "Значение для тестируемого свойства"}]},

                                        case2 (Второй экземпляр, дублирующий):
                                        {"value": "Значение для тестируемого свойства"}]}

    Ожидаемый результат: Результат запроса с данными первого экземпляра - код ответа 200 , Результат запроса с данными
                        второго промокода - код ответа 400


Добавление дополнительных атрибутов в тест-кейс:

    "add":[
            {"attribute":"Название дополнительного атрибута",
             "value": "Значение дополнительного атрибута"},
             {"attribute":"Название 2-го доп. атрибута,"value":"Значение 2-го доп. атрибута и тд.}]


    Вставить add в тест-кейс:
            "Название тестируемого свойства" :[ {
            "value": "Значение для тестируемого свойства",
            "add":[
                {
                "attribute":"Название дополнительного атрибута",
                "value": "Значение дополнительного атрибута"
            },{
                "attribute":"Название 2-го доп. атрибута,
                "value":"Значение 2-го доп. атрибута и тд.
                }]}]


"""

data_negative_create = {
    'data': [{
        'value': [],
        'error':"_schema: ['Invalid input type.']"
    }, {
        'value': None,
        'error': "Payload must be a valid json"
    }],
    'name': [{
        'value': '',
        'error': "name: ['Length must be between 1 and 350.']"
    }, {
        'value': [],
        'error':"name: ['Not a valid string.']"
    }, {
        'value': 'miss',
        'error': "name: ['Missing data for required field.']"
    }, {
        'value': 's'*351,
        'error': "name: ['Length must be between 1 and 350.']"
    }, {
        'value': ' ',
        'error': "name: ['Not a valid string.']"
    }, {
        'value': None,
        'error': "name: ['Field may not be null.']"
    }],
    'education': [{
        'value': '',
        'error': "education: ['Length must be between 1 and 350.']"
    }, {
        'value': [],
        'error': "education: ['Not a valid string.']"
    }, {
        'value': 's'*351,
        'error': "education: ['Length must be between 1 and 350.']"
    }, {
        'value': ' ',
        'error': "education: ['Not a valid string.']"
    }, {
        'value': None,
        'error': "education: ['Field may not be null.']"
    }],
    'identity': [{
        'value': '',
        'error': "identity: ['Length must be between 1 and 350.']"
    }, {
        'value': [],
        'error': "identity: ['Not a valid string.']"
    }, {
        'value': 's'*351,
        'error': "identity: ['Length must be between 1 and 350.']"
    }, {
        'value': ' ',
        'error': "identity: ['Not a valid string.']"
    }, {
        'value': None,
        'error': "identity: ['Field may not be null.']"
    }],
    'other_aliases': [{
        'value': '',
        'error': "other_aliases: ['Length must be between 1 and 350.']"
    }, {
        'value': [],
        'error':"other_aliases: ['Not a valid string.']"
    }, {
        'value': 's'*351,
        'error': "other_aliases: ['Length must be between 1 and 350.']"
    }, {
        'value': ' ',
        'error': "other_aliases: ['Not a valid string.']"
    }, {
        'value': None,
        'error': "other_aliases: ['Field may not be null.']"
    }],
    'universe': [{
        'value': '',
        'error': "universe: ['Length must be between 1 and 350.']"
    }, {
        'value': [],
        'error': "universe: ['Not a valid string.']"
    }, {
        'value': 's'*351,
        'error': "universe: ['Length must be between 1 and 350.']"
    }, {
        'value': ' ',
        'error': "universe: ['Not a valid string.']"
    }, {
        'value': None,
        'error': "universe: ['Field may not be null.']"
    }],
    'weight': [{
        'value': '',
        'error': "weight: ['Not a valid number.']"
    }, {
        'value': None,
        'error': "weight: ['Field may not be null.']"
    }],
    'height': [{
        'value': -1,
        'error': "height: ['Not a valid number.']"
    }, {
        'value': '',
        'error': "height: ['Not a valid number.']"
    }, {
        'value': None,
        'error': "height: ['Field may not be null.']"
    }]
}

data_positive_create = {
    'name': [{
        'value': 'r'
    }, {
        'value': 'r'*350
    }, {
        'value': 'r'*349
    }, {
        'value': '"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'education': [{
        'value': 'r'
    }, {
        'value': 'r'*350
    }, {
        'value': 'r'*349
    }, {
        'value': '"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'identity': [{
        'value': 'r'
    }, {
        'value': 'r'*350
    }, {
        'value': 'r'*349
    }, {
        'value': '"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'other_aliases': [{
        'value': 'r'
    }, {
        'value': 'r'*350
    }, {
        'value': 'r'*349
    }, {
        'value': '"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'universe': [{
        'value': 'r'
    }, {
        'value': 'r'*350
    }, {
        'value': 'r'*349
    }, {
        'value': '"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'weight': [{
        'value': 1
    }, {
        'value': 1.55
    }, {
        'value': 0
    }, {
        'value': -1
    }],
    'height': [{
        'value': 0
    }, {
        'value': 0.55
    },{
        'value': 1
    }]
}

data_duplicate_create = {
    'name': [{
        'case_create': {
            'value': 'Test duplicate name'
        },
        'case_duplicate': {
            'value': 'Test duplicate name'
        }
    }]
}