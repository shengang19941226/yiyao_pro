import time
import pytest,allure
from page.main_page import MainPage
from page.base_page_web import BasePage

@allure.feature('测试医药cms端类')
class TestYiYao:

    def setup(self):
        # self.main = MainPage(types='debug')
        # self.main.write_cookie_for_json('../datas/cookie.json')
        loc1 = ("xpath","//*[contains(text(),'登 录')]")
        loc2 = ("xpath","//span[contains(text(),'处方中心')]")
        self.main = MainPage(url='http://partner.zhyf.sfrog.cn/#/workbench/index',userhadless='true')
        print('植入cookie前')
        print(f'检测未登录页面元素：{self.main.is_visibility_of_element_located(loc1)}')
        print(f'检测已登录页面元素：{self.main.is_visibility_of_element_located(loc2)}')
        self.main.add_cookie('../datas/cookie.json')
        self.main.refresh()
        self.main.max_size()

        print('植入cookie后')
        print(f'检测未登录页面元素：{self.main.is_visibility_of_element_located(loc1)}')
        print(f'检测已登录页面元素：{self.main.is_visibility_of_element_located(loc2)}')


    def teardown(self):
        self.main.quit()

    @allure.story('测试用例：创建处方成功')
    def test_add_prescription_success(self):
        pass


if __name__ == '__main__':
    pytest.main(['test_yiyao.py','-sq'])
