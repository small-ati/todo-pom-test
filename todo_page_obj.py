from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class TodoPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.input_box = (By.ID,'new-todo')
        self.add_btn = (By.ID,'add-btn')
        self.todo_list = (By.ID,'todo-list')
        self.count = (By.ID,'count')
    def open(self,url):
        self.driver.get(url)
    def add_task(self,text):
        element = self.wait.until(EC.presence_of_element_located(self.input_box))
        element.clear()
        element.send_keys(text)
        self.driver.find_element(*self.add_btn).click()
    def get_task_count(self):
        element = self.wait.until(EC.presence_of_element_located(self.count))
        return int(element.text)
    def get_tasks(self):
        items = self.driver.find_elements(By.CSS_SELECTOR,'#todo-list li span')
        return [item.text for item in items]
    def complete_task(self,index):
        checkbox = self.driver.find_element(By.CSS_SELECTOR,f'#todo-{index} input[type="checkbox"]')
        checkbox.click()
    def delete_task(self,index):
        del_btn = self.driver.find_element(By.CSS_SELECTOR,f'#todo-{index} button')
        del_btn.click()
