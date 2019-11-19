

data_negative_post={
    'data':[{
        'value':[],
        'error':"_schema: ['Invalid input type.']"
    },{
        'value':None,
        'error':"Payload must be a valid json"
    }],
    'name':[{
        'value':'',
        'error':"name: ['Length must be between 1 and 350.']"
    },{
        'value':[],
        'error':"name: ['Not a valid string.']"
    },{
        'value':'miss',
        'error':"name: ['Missing data for required field.']"
    },{
        'value':'s'*351,
        'error':"name: ['Length must be between 1 and 350.']"
    },{
        'value':' ',
        'error':"name: ['Not a valid string.']"
    },{
        'value':None,
        'error':"name: ['Field may not be null.']"
    },{
        'value':None,
        'add':[{
            'attribute':'education',
            'value':None
        },{
            'attribute':'universe',
            'value':None
        },{
            'attribute':'identity',
            'value':None
        },{
            'attribute':'height',
            'value':None
        },{
            'attribute':'weight',
            'value':None
        },{
            'attribute':'other_aliases',
            'value':None
        }],
        'error':"identity: ['Field may not be null.'], weight: ['Field may not be null.'], height: ['Field may not be null.'], education: ['Field may not be null.'], name: ['Field may not be null.'], universe: ['Field may not be null.'], other_aliases: ['Field may not be null.']"
    }],
    'education':[{
        'value':'',
        'error':"education: ['Length must be between 1 and 350.']"
    },{
        'value':[],
        'error':"education: ['Not a valid string.']"
    },{
        'value':'s'*351,
        'error':"education: ['Length must be between 1 and 350.']"
    },{
        'value':' ',
        'error':"education: ['Not a valid string.']"
    },{
        'value':None,
        'error':"education: ['Field may not be null.']"
    }],
    'identity':[{
        'value':'',
        'error':"identity: ['Length must be between 1 and 350.']"
    },{
        'value':[],
        'error':"identity: ['Not a valid string.']"
    },{
        'value':'s'*351,
        'error':"identity: ['Length must be between 1 and 350.']"
    },{
        'value':' ',
        'error':"identity: ['Not a valid string.']"
    },{
        'value':None,
        'error':"identity: ['Field may not be null.']"
    }],
    'other_aliases':[{
        'value':'',
        'error':"other_aliases: ['Length must be between 1 and 350.']"
    },{
        'value':[],
        'error':"other_aliases: ['Not a valid string.']"
    },{
        'value':'s'*351,
        'error':"other_aliases: ['Length must be between 1 and 350.']"
    },{
        'value':' ',
        'error':"other_aliases: ['Not a valid string.']"
    },{
        'value':None,
        'error':"other_aliases: ['Field may not be null.']"
    }],
    'universe':[{
        'value':'',
        'error':"universe: ['Length must be between 1 and 350.']"
    },{
        'value':[],
        'error':"universe: ['Not a valid string.']"
    },{
        'value':'s'*351,
        'error':"universe: ['Length must be between 1 and 350.']"
    },{
        'value':' ',
        'error':"universe: ['Not a valid string.']"
    },{
        'value':None,
        'error':"universe: ['Field may not be null.']"
    }],
    'weight':[{
        'value':'',
        'error':"weight: ['Not a valid number.']"
    },{
        'value':None,
        'error':"weight: ['Field may not be null.']"
    }],
    'height':[{
        'value':-1,
        'error':"height: ['Not a valid number.']"
    },{
        'value':'',
        'error':"height: ['Not a valid number.']"
    },{
        'value':None,
        'error':"height: ['Field may not be null.']"
    }]
}

data_positive_post={
    'name':[{
        'value':'r'
    },{
        'value':'r'*350
    },{
        'value':'r'*349
    },{
        'value':'"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'education':[{
        'value':'r'
    },{
        'value':'r'*350
    },{
        'value':'r'*349
    },{
        'value':'"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'identity':[{
        'value':'r'
    },{
        'value':'r'*350
    },{
        'value':'r'*349
    },{
        'value':'"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'other_aliases':[{
        'value':'r'
    },{
        'value':'r'*350
    },{
        'value':'r'*349
    },{
        'value':'"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'universe':[{
        'value':'r'
    },{
        'value':'r'*350
    },{
        'value':'r'*349
    },{
        'value':'"! # $ % & ‘ * + — / = ? ^ _ ` { | } ~"'
    }],
    'weight':[{
        'value':100
    },{
        'value':100.5
    },{
        'value':0
    },{
        'value':-1
    }],
    'height':[{
        'value':0
    },{
        'value':0.5
    }]
}


data_duplicate_post={

}