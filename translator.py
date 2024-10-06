# translator.py

import re

arabic_to_python = {
    'متغير': '',
    'إذا': 'if',
    'آخر': 'else',
    'لكل': 'for',
    'بينما': 'while',
    'دالة': 'def',
    'عائد': 'return',
    'طباعة': 'print',
    'صحيح': 'True',
    'خطأ': 'False',
    'و': 'and',
    'أو': 'or',
    'ليس': 'not',
    'إضافة': 'append',
    'طول': 'len',
    'في': 'in',
    'تابع': 'def',
    'إلى': 'to',
    'إلا': 'except',
    'جرب': 'try',
    'أخيرا': 'finally',
    'افتح': 'open',
    'أغلق': 'close'
}

def translate_to_python(code):
    for arabic_word, python_word in arabic_to_python.items():
        code = re.sub(rf'\b{arabic_word}\b', python_word, code)
    return code

def run_arabic_code(arabic_code):
    python_code = translate_to_python(arabic_code)
    exec(python_code)
