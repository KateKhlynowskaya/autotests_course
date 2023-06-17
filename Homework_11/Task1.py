from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_website = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()
try:
    driver.get(sbis_website)
    assert driver.current_url == sbis_website, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок'
    contact_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/contacts"]')
    assert contact_button.text == 'Контакты'
    contact_button.click()

    banner_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner_tensor.click()

    driver.switch_to.window(driver.window_handles[1])
    line = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close')
    line.click()

    news_list = driver.find_elements(By.CSS_SELECTOR, '.tensor_ru-Index__card')
    power_people = news_list[1]
    assert power_people.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-title').text == 'Сила в людях'

    string_details = power_people.find_element(By.CSS_SELECTOR, '.tensor_ru-link')
    string_details.click()
    url_about = 'https://tensor.ru/about'
    assert driver.current_url == url_about
finally:
    driver.quit()
