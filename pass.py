from random import sample
print((''.join(sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*\';?()[]{}', 78)))[:int(input('Какой длины пароль: '))])