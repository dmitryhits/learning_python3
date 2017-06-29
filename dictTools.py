def copyDict(Dict):
    return {key:Dict[key] for key in Dict.keys()}


def addDict(arg1, arg2):
    """
    computes a union of two dictionaries or concatenates two lists

    the dict1 values of the keys identical to dict2 keys
    will be overwritten with dict2 values

    :param arg1: dictionary or list
    :param arg2: dictionary or list
    :return: union of dict or sum of lists
    """
    res = arg1
    if type(arg1)==dict and type(arg2)==dict:
        for key in arg2.keys():
            res[key] = arg2[key]
    if type(arg1) == list and type(arg2) == list:
        res.extend(arg2)
    return res
