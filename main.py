def f_dict(dicts,d={},keys=''):
    for key in dicts:
        if isinstance(dicts.get(key),dict):
            if keys == '':
                keys = f'{key}' + f'.{keys}'
            else:
                keys = keys + f'{key}.'
            f_dict(dicts.get(key),d,keys)
            if  len(keys) == 2:
                keys=''
        else:
            d.setdefault(f'{keys}'+key,dicts.get(key))
    return d