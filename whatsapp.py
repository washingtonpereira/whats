from selenium import webdriver
import time

driver =  webdriver.Chrome(executable_path=r'C://Users/Python/PycharmProjects/whats/Chromedriver.exe')

driver.get('https://odia.ig.com.br/')

time.sleep(10)
auxilio = driver.find_element_by_css_selector('figure').click()
time.sleep(60)
novos_dados = driver.find_element_by_class_name('chamada').click()


