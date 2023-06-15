from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_website = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()
try:
    driver.get(sbis_website)
    assert driver.current_url == sbis_website, 'Не верный адрес сайта'
    assert driver.title == sbis_title, 'Не верный заголовок'
    contact_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/contacts"]')
    assert contact_button.text == 'Контакты'
    assert contact_button.is_displayed()
    contact_button.click()

    banner_tensor = driver.find_element(By.CSS_SELECTOR, '#contacts_clients a[title="tensor.ru"]')
    assert banner_tensor.is_displayed()
    banner_tensor.click()

    driver.switch_to.window(driver.window_handles[1])
    line = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close')
    assert line.is_displayed()
    line.click()

    news_banner = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    assert news_banner.is_displayed()
    string_details = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content a[href="/about"]')
    assert string_details.is_displayed()
    string_details.click()
    
    url_about = 'https://tensor.ru/about'
    assert driver.current_url == url_about
finally:
    driver.quit()
