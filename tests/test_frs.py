# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time
# count = 0
#
# def test_1(driver):
#     driver.get('https://www.onliner.by/')
#
#     locator = '.b-news-layer'
#     element = None
#     for i in range(10):
#         try:
#             time.sleep(1)
#             print('Try element')
#             element = driver.find_element(By.CSS_SELECTOR, locator)
#             if element is not None:
#                 break
#         except NoSuchElementException:
#             print('Element not found')
#
#     assert element
from tests.conftest import driver

# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# count = 0
#
#
# def test_1(driver):
#     driver.get('https://www.onliner.by/')
#
#     locator = '.b-news-layer'
#     element = None
#
#     while element == None:
#         try:
#             time.sleep(1)
#             print('Try element')
#             element = driver.find_element(By.CSS_SELECTOR, locator)
#             if element is not None:
#                 break
#         except NoSuchElementException:
#             print('Element not found')
#
#         assert element
#
#     assert element
#
#
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_1(driver):
#     driver.get('https://www.onliner.by/')
#
#     locator = '.b-top-navigation-age'
#
#     element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)),
#                                         "Element not clicable")
#
#     assert element
#
#     from selenium.webdriver.support.wait import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#
#     def wait_for_clicable(driver, locator):
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator),
#                                         "Element not clicable")
#
#     def add_cookie(driver, name, value):
#         driver.add_cookie({'name': name, 'value': value})
#         driver.refresh()
#
#     def delete_cookies(driver):
#         driver.delete_cookies()
#         driver.refresh()


driver