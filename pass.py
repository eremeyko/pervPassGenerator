print((lambda w: (''.join(w))[:int(input('Какой длины пароль: '))])(__import__('random').sample(__import__('string').ascii_letters + __import__('string').digits + __import__('string').punctuation, 94)))
