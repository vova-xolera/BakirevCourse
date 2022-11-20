def get_data_fig(*args, **kwargs):
    per = sum([i for i in args])
    result = per,
    kwparams = []
    if "type" in kwargs.keys():
        kwparams.append(kwargs.get("type"))
    if "color" in kwargs.keys():
        kwparams.append(kwargs.get("color"))
    if "closed" in  kwargs.keys():
        kwparams.append(kwargs.get("closed"))
    if "width" in kwargs.keys():
        kwparams.append(kwargs.get("width"))
    for i in kwparams:
        result += (i,)
    return result

print(get_data_fig(5, 4, color='Yellow',  type=False, closed=True))