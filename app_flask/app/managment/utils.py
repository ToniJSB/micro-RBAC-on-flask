from flask import current_app

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
        else:
            form_constructor[atr[0]] = atr[1]
    return form_constructor

def get_languages():
    languages = current_app.config['LANGUAGES']
    locale = languages[current_app.config['BABEL_DEFAULT_LOCALE']]

    lang = {
        "languages": languages,
        "locale": locale
    }
    return lang