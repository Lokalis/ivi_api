
date_negative_search_instance={
    'name':[{
        'value':'miss',
        'error':'name parameter is required'
    },{
        'value':'not+find+name',
        'error':'No such name',
    },{
        'value':'not allowed without plus',
        'add_instance':{
            'value':'not allowed without plus'
        },
        'error':'No such name'
    }]
}

data_positive_search_instance={
    'name':[{
        'value':'find+space',
        'add_instance':{
            'value':'find space'}
    },{
        'value':'find',
        'add_instance':{
            'value':'find'}
    }]
}