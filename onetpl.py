import asyncio
import random
import threading
import time

from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, ElementNotSelectableException, \
    NoSuchElementException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import file_path


def registration(current_proxy):
    for _ in range(0, 10):
        options = Options()
        options.add_argument('--proxy-server=%s' % current_proxy)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=options, executable_path=file_path.chromedriver_path)
        browser.set_page_load_timeout(60)
        try:
            print(current_proxy)

            browser.get('https://konto.onet.pl/register?client_id=poczta.onet.pl.front.onetapi.pl')

            try:
                elem = WebDriverWait(browser, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div[4]/button[2]')))
                confirm_password_button = browser.find_element_by_xpath(
                    '/html/body/div[5]/div[1]/div[2]/div/div[4]/button[2]')
                confirm_password_button.click()

            except:
                pass

            elem = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[1]/input')))
            email_address = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[1]/input')
            name_of_chel = random.choices(names_list)[0]
            surname_of_chel = random.choices(surnames_list)[0]
            additional_number = str(random.randint(1, 2021))
            full_name_email_look = f'{name_of_chel}_{surname_of_chel}{additional_number}'
            email_address.send_keys(full_name_email_look)
            email_plus_domian_look = full_name_email_look + '@op.pl'

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/button')))
            registration_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/button')
            registration_button.click()

            elem = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/div[1]/div[1]/input')))
            password_place = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/div[1]/div[1]/input')
            second_password_place = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/div[3]/div/div[1]/input')
            password = 'Ds@#2'
            for _ in range(0, 5):
                password += random.choices(password_symbols)[0]
            for _ in range(0, 5):
                password = random.choices(password_symbols)[0] + password
            password_place.send_keys(password)
            second_password_place.send_keys(password)

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/button')))
            confirm_password_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/button')
            confirm_password_button.click()

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/div/div[1]/label/span')))
            pani_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/div/div[1]/label/span')
            pani_button.click()

            name_input = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/div[1]/input')
            name_input.send_keys(f'{name_of_chel} {surname_of_chel}')

            date_of_birthday = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[1]/div/div/input')
            date_of_birthday.send_keys(random.randint(1, 25))

            month_of_birthday_selector = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/select')
            month_of_birthday_selector.click()

            elem = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/select/option[2]')))
            month_of_birthday = random.randint(2, 13)
            month_of_birthday_elem = browser.find_element_by_xpath(
                f'/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/select/option[{month_of_birthday}]')
            month_of_birthday_elem.click()

            year_of_birthday = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[3]/div/div/input')
            year_of_birthday.send_keys(str(random.randint(1970, 2001)))

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[5]/button')))
            confirm_registration = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[5]/button')
            confirm_registration.click()

            elem = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[3]/button')))
            free_plan_button = browser.find_element_by_xpath(
                f'/html/body/div[1]/div[1]/div[2]/div/div/div/div[3]/button')
            free_plan_button.click()

            elem = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/button')))
            ok_i_want_get_shit_emails = browser.find_element_by_xpath(
                f'/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/button')
            ok_i_want_get_shit_emails.click()

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/button')))
            confirm_of_shit_emails = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/button')
            confirm_of_shit_emails.click()

            try:
                elem = WebDriverWait(browser, 30).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/p')))

            except TimeoutException:
                pass
            except NoSuchElementException:
                pass
            else:
                browser.close()
                print(f'прокси {current_proxy} пизда')
                break

            elem = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/a')))
            with open(file_path.data_path + f'/results/{name_of_chel}_{surname_of_chel}.txt',
                      'w') as file_with_ready_emails:
                file_with_ready_emails.write(f'{email_plus_domian_look}:{password}\n')

            browser.close()
        except TimeoutException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break
        except NoSuchElementException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break
        except ElementNotInteractableException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break
        except ElementNotSelectableException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break
        except ElementClickInterceptedException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break
        except WebDriverException:
            browser.close()
            print(f'прокси {current_proxy} пизда')
            break

names_list = []
with open(f'{str(file_path.data_path)}/name.txt', 'r') as file_with_names:
    for line in file_with_names:
        names_list.append(line[:-1])
surnames_list = []
with open(str(file_path.data_path) + '/surnames.txt', 'r') as file_with_names:
    for line in file_with_names:
        surnames_list.append(line[:-1])
proxy_list = []
with open(file_path.data_path + '/proxy_list.txt', 'r') as proxy_file:
    for line in proxy_file:
        proxy_list.append(line[:-1])

password_symbols = '!@#$%^&*()_+{}"|?></123456787890rveafbyipAUBDFGOFDSKVMNsadfbuo\FDABNdfbvolas'

mini_list = []
current_try = [0]

for proxy in proxy_list:
    current_try[0] += 1
    print('текущая попытка - ', current_try)
    if len(mini_list) < 10:
        mini_list.append(proxy)
    else:
        my_threads = []
        for mini_list_proxy in mini_list:
            thread = threading.Thread(target=registration, args=(mini_list_proxy,))
            thread.start()
        time.sleep(80)
        mini_list = []

