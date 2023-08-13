import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver.exe")
#Функция принимает путь до изображения и отправляет изображение в API rucaptcha, после получения разагаднной капчи, функция возвращает код который находился на капче

def solver(path):
    solver = TwoCaptcha('XXXXXXXXXXX')
    print('2) Изображение отправленно для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ: ', result)
    return result['code']


time.sleep(5)
with webdriver.Chrome(service=s) as browser:
    browser.get('XXXXXXXXX')

    #используем неявное ожидание для полной загрузки страницы и появляется всех элементов.
    browser.implicitly_wait(10)
    #Это условие if проверит в исходном коде ключевую фразу для определения на странице капчи.
    if 'Подтвердите, что вы не робот' in browser.page_source:
        #Находим элемент где располагается изображение капчи и делаем его скриншот, .screenshot('img.png') сохрнаняет скриншот в папке с проектом,
        #но можно написать и полный путь, тогда его необходимо будет передать в solver()

        browser.find_element(By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(By.TAG_NAME,'img').screenshot('img.png')
        print('1) Скриншот области успешно сделан')
        #Находим текстовое поле и вставляем код который возвращает функция solver(),
        inputing_code = browser.find_element(By.ID, 'field-:r0:').send_keys(solver('img.png'))
        #Находим кнопку "Подтвердить" и кликаем по ней.
        browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()
        height = browser.execute_script("return document.body.scrollHeight")
        # выполняем скрол страницы
        print(height)
        for i in range(0, height, 100):
            browser.execute_script(f'window.scrollBy(0,{i})')
            time.sleep(0.1)
        time.sleep(5)
    #Собираем список наименований всех товарных позиций на странице
    name_card = [x.text for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]
    time.sleep(5)
    print('4)',name_card)