# Что?
# Телеграм-бот, с которым можно играть в игру "Угадай число"

# Чтобы что?
# Чтобы можно было сыграть в простую игру с ботом

# Что бот должен уметь?
# Генерировать случайное число от 1 до 100
# Хранить состояние ("в игре", "не в игре")
# Считать количество попыток, оставшихся у пользователя
# Сравнивать ответы пользователя с загаданным числом
# Дополнительный функционал
# Бот может показывать статистику игр пользователя по запросу
# Описание взаимодействия с ботом
# Пользователь отправляет команду /start боту (или стартует его, найдя в поиске)
# Бот приветствует пользователя и предлагает сыграть в игру "Угадай число", также предлагает пользователю прочитать подробные правила, отправив команду /help
# На этом этапе пользователь может совершить 5 действий:
# Согласиться поиграть с ботом в игру, отправив в чат "Да" или "Давай", или "Сыграем" и т.п.
# Не согласиться играть, отправив в чат "Нет" или "Не хочу", или "В другой раз" и т.п.
# Отправить в чат команду /help
# Отправить в чат команду /stat
# Отправить в чат любое другое сообщение
# Пользователь отправляет в чат согласие играть в игру:
# Бот сообщает пользователю, что очень рад поиграть и сохраняет рандомное число от 1 до 100
# Бот сохраняет информацию о том, что пользователь находится в состоянии "Игра"
# Бот устанавливает счетчик попыток пользователя в значение по умолчанию
# Пользователь на этом этапе может совершить 3 действия:
# Прислать в чат число от 1 до 100
# Прислать в чат команду /cancel
# Прислать что-то отличное от этих 2-х пунктов
# Пользователь присылает в чат число от 1 до 100:
# Бот сравнивает число, присланное пользователем, с загаданным
# Если числа совпадают:
# Бот поздравляет пользователя с победой
# Бот переводит состояние из "Игра" в "Не игра"
# Бот присылает пользователю сообщение с предложением сыграть еще раз
# Бот увеличивает счетчик игр пользователя на 1
# Бот увеличивает счетчик побед пользователя на 1
# Если число пользователя меньше загаданного:
# Бот уменьшает количество попыток пользователя на одну
# Бот сообщает пользователю, что загаданное число больше
# Если число пользователя больше загаданного:
# Бот уменьшает количество попыток пользователя на одну
# Бот сообщает пользователю, что загаданное число меньше
# Пользователь присылает в чат команду /cancel:
# Бот переводит состояние из "Игра" в "Не игра"
# Бот отправляет в чат сообщение о том, что игра закончилась
# Бот отправляет в чат сообщение о том, что если пользователь захочет снова сыграть, то пусть отправит сообщение "Игра" или "Сыграть", или "Давай сыграем" и т.п.
# Пользователь в состоянии "Игра" присылает в чат что-то отличное от числа от 1 до 100 или команды /cancel:
# Бот отправляет пользователю сообщение о том, что по правилам игры пользователь может присылать в чат только числа от 1 до 100 или команду /cancel
# Если у пользователя заканчивается количество попыток:
# Бот сообщает пользователю, что тот проиграл
# Бот сообщает пользователю, что загаданное число было таким-то
# Бот меняет состояние "Игра" на "Не игра"
# Бот увеличивает счетчик игр пользователя на 1
# Бот оправляет пользователю сообщение с предложением сыграть еще раз
# Пользователь отправляет в чат отказ играть в игру:
# Бот отправляет пользователю сообщение, типа, "Жаль :(" и инструкцию что нужно сделать пользователю, если он все-таки захочет поиграть
# Пользователь отправляет в чат команду /help:
# Бот присылает пользователю правила игры и описание команд
# Пользователь отправляет в чат команду /stat:
# Бот присылает пользователю статистику по играм (сколько всего было игр и в скольких из них пользователь выиграл)
# Бот присылает пользователю сообщение с предложением сыграть
# Пользователь отправляет в чат любое другое сообщение:
# Бот сообщает, что не понимает пользователя и снова предлагает сыграть в игру