from django import template
import re

register = template.Library()

bad_words_file = open('bad_words.txt', 'r')  # файл в корне проекта NewsPaper
bad_words = set(line.strip('\n') for line in open('bad_words.txt', encoding = "utf8"))
exp = '(\\b%s\\b)' % '\\b|\\b'.join(bad_words)  # Делаем маску учитывая начало и окончание слова
r = re.compile(exp, re.IGNORECASE)  # компилируем маску игнорируя регистр


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError("censor применяется не к строке")

    def cen(val):
        return f'{val[0][:1]}{"*" * (len(val[0]) - 1)}'

    t = r.sub(cen, value)  # подмена с использованием функции cen()
    return f'{t}'


essence = {'N': 'news', 'A': 'articles'}


@register.filter()
def translate_essence(value):
    return essence.get(value)
