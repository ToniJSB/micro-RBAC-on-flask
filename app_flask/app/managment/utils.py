

def getattrs_from_form(form):
    """
    Coge los atributos del modelo que están en el formulario

    Parametro
    -
    FlasKForm

    Return
    -
    dict
    
    """
    form_constructor = dict()
    for atr in form.__dict__.items():
        if atr[0] == 'meta':
            continue
        elif atr[0] == '_prefix':
            continue
        elif atr[0] == '_fields':
            continue
        elif atr[0] == '_csrf':
            continue
        elif atr[0] == 'csrf_token':
            continue
        else:
            form_constructor[atr[0]] = atr[1]
    return form_constructor