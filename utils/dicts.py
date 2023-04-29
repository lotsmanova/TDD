def get_val(collection, key, default="git"):
    '''
    Функция возвращает значение из словаря по переданному ключу
    :param collection: передаваемый словарь
    :param key: заданный ключ
    :param default: если ключ не существует, значение default
    :return: значение из словаря
    '''
    if len(collection) > 0:
        for k in collection:
            if k == key:
                return collection[key]
            return default
    return default
