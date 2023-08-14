from django import template

register = template.Library()

censu = ['редиска', 'дурак', 'дура', 'боль']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError()

    for word in value.split():
        if word in censu:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 2)}{word[-1]}")
    return value
