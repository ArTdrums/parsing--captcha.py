# parsing--captcha.py
Используемые библиотеки: selenium, time, twocaptcha.
Краткое описание работы программы.
1.	Создаю функцию. Которая принимает путь для изображения капчи, далее это путь передается в API rucaptcha , в ответ приходит код для разгадывания.
2.	При создании функции создается переменная, которая с помощью библиотеки twocaptcha и модуля Twocaptcha принимает в себя полученный при регистрации API ключ и служит своеобразным мостиком между нашем кодом и API rucaptcha
3.	Для открытия сайта используя менеджер контекста with и webdriver, далее для загрузки страницу выставляю не явные ожидания используя библиотеку time. 
4.	C помощью условной конструкции делает поиск на фразу ‘Подтвердите, что вы не робот 
5.	Если данная строка  присутствует на странице, то с помощью библиотеки selenium и метода find_element() делает поиск элемента через CSS_SELECTOR ( указываю класс в котором лежит изображение и тэг). 
6.	После поиска делает скришот (используя метод screenshot())данной области и отправка ее в API. 
7.	После получению ключа, происходит поиск поля ввода (аналогичный образом через библиотеку selenium) и с помощью метода send_keys() передаётся ключ в данное поле. 
8.	Далее находится элемент (кнопка для подтверждения) и с помощью метода click() происходит нажатие на кнопку и финальный этап для отправки( подтверждения капчи)
9.	Далее делается парсинг страницы с поиском нужных элементов с помощью selenium и сохранением информации в csv файл.
10.	Сложности: в процессе работы столкнулся с тем, что для загрузки всех элементов на странице требовалось сделать скрол страницы.
