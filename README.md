# "Perverted" Password Generator ("Извращенный" генератор паролей)
## EN
Flipping through the github repository, I came across password generators more and more often. And I wondered: **why are there so many lines?!**
In general, I present to your attention (if anyone is watching at all)...

**A "perverted" password generator**

-----------
> Q: Why "Perverted"?
> > A: And you look at the number of lines... ONE concise, absurdly shortened line

> Q: Asshole?
> > A: Why not if I can?

> Q: What would a normal code look like?
> > A: A normal code would look like this:

[True C0de](https://github.com/eremeyko/pervPassGenerator#True%20C0de)

## RU
Листая репозитории гитхаба, я всё чаще и чаще натыкался на генераторы паролей. И удивлялся: **почему так много строк?!**
В общем, представляю Вашему вниманию (если это кто-то вообще смотрит)...

**"Извращенный" генератор паролей**

-----------
> Q: Почему "Извращенный"?
> > A: А ты взгляни на количество строк... ОДНА лаконичная, до абсурда сокращенная строка

> Q: Мудак?
> > A: Почему нет, если могу?

> Q: Как бы выглядел нормальный код?
> > A: Нормальный код выглядел бы так:

## True C0de
```python
import random
import string

password_length = int(input('Какой длины пароль: '))
all_characters = string.ascii_letters + string.digits + string.punctuation
password_chars = random.sample(all_characters, password_length)
password = ''.join(password_chars)

print(password
```
