import pytest,os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from todo_page_obj import TodoPage
@pytest.fixture
def driver():
    driver_path = os.path.join(os.path.dirname(__file__),'msedgedriver.exe')
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()

TODO_URL = 'file:///D:/python学习/第三个项目/todo_page.html'
def test_add_todo(driver):
    """验证添加待办事项功能"""
    page = TodoPage(driver)
    page.open(TODO_URL)

    page.add_task('学习Python')
    page.add_task('玩游戏')

    assert page.get_task_count() == 2
    assert '学习Python' in page.get_tasks()[0]
    assert '玩游戏' in page.get_tasks()[1]
def test_complete_todo(driver):
    """验证勾选待办事项功能"""
    page = TodoPage(driver)
    page.open(TODO_URL)
    page.add_task('任务一')
    page.add_task('任务er')
    page.complete_task(0)
    page.complete_task(1)
    assert page.get_task_count() == 0
def test_delete_todo(driver):
    """验证删除待办事项功能"""
    page = TodoPage(driver)
    page.open(TODO_URL)
    page.add_task('待删除的任务')
    page.delete_task(0)
    assert page.get_tasks() == []
def test_delete_one_of_many(driver):
    page = TodoPage(driver)
    page.open(TODO_URL)
    add_tasks = ['任务A','任务B','任务C']
    for i in add_tasks:
        page.add_task(i)
    page.delete_task(0)
    assert page.get_task_count() == 2
    tasks = page.get_tasks()
    assert '任务A' not in tasks
    assert '任务B' in tasks and '任务C' in tasks
