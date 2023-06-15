from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

sbis_website = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
driver = webdriver.Chrome()
try:
    driver.get(sbis_website)
    driver.maximize_window()
    sleep(2)
    assert driver.current_url == sbis_website, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок'

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('бохохо', Keys.ENTER)
    assert login.get_attribute('value') == 'бохохо'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('Бохохо1', Keys.ENTER)

    sleep(10)

    assert driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"]').is_displayed()

    driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"]').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"] .NavigationPanels-SubMenu__headTitle').click()

    sleep(10)

    contact_person = driver.find_element(By.CSS_SELECTOR, '[title="Иванов Иван"]')
    assert contact_person.text == 'Иванов Иван'
    assert contact_person.is_displayed()
    contact_person.click()
    sleep(3)

    search_line = driver.find_element(By.CSS_SELECTOR, '[data-slate-node="element"]')
    assert search_line.is_displayed()
    search_line.click()
    search_line.send_keys('Привет')
    sleep(3)

    new_dialogue = driver.find_element(By.CSS_SELECTOR, '[title="Создать новый диалог"]')
    assert new_dialogue.is_displayed()
    new_dialogue.click()
    sleep(3)
    sms = driver.find_element(By.CSS_SELECTOR, '.msg-entity-expander p')
    assert sms.text == 'Привет'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sms)
    action_chains.context_click(sms)
    action_chains.perform()
    sleep(3)

    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_del"]')
    assert delete_button.text == 'Удалить'
    assert delete_button.is_displayed()
    delete_button.click()
    sleep(3)

    assert len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander p')) == 0

finally:
    driver.quit()
