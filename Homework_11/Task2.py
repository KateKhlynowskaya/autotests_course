from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

sbis_website = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
driver = webdriver.Chrome()


def wait(selector):
    return WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selector)))

try:
    driver.get(sbis_website)
    driver.maximize_window()
    sleep(1)
    assert driver.current_url == sbis_website, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок'

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('бохохо', Keys.ENTER)
    assert login.get_attribute('value') == 'бохохо'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('Бохохо1', Keys.ENTER)

    sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"]').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"] .NavigationPanels-SubMenu__headTitle').click()
    sleep(1)
    contact_person = driver.find_element(By.CSS_SELECTOR, '[title="Иванов Иван"]')
    assert contact_person.text == 'Иванов Иван'
    contact_person.click()
    sleep(1)
    search_line = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    search_line.click()
    search_line.send_keys('Привет')

    new_dialogue = driver.find_element(By.CSS_SELECTOR, '[title="Создать новый диалог"]')
    new_dialogue.click()
    sleep(1)

    sms = driver.find_element(By.CSS_SELECTOR, '.msg-entity-expander p')
    assert sms.text == 'Привет'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sms)
    action_chains.context_click(sms)
    action_chains.perform()

    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_del"]')
    assert delete_button.text == 'Удалить'
    assert delete_button.is_displayed()
    delete_button.click()
    sleep(1)
    assert len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander p')) == 0
finally:
    driver.quit()
