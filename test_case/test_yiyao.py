import time
import pytest,allure
from page.main_page import MainPage
from page.base_page_web import BasePage

@allure.feature('测试医药cms端类')
class TestYiYao:

    def setup(self):
        # self.main = MainPage(types='debug')
        # self.main.write_cookie_for_json('../datas/cookie.json')
        self.main = MainPage(url='http://partner.zhyf.sfrog.cn/#/workbench/index')
        self.main.add_cookie('../datas/cookie.json')
        self.main.refresh()
        self.main.max_size()

    def teardown(self):
        self.main.quit()

    @allure.story('测试用例：创建处方成功')
    def test_add_prescription_success(self):
        name = 'shen'
        res = self.main.goto_prescription_center().goto_prescription_create().add_prescription_success(
            patient_name=name, age='18', phone='17365372296', birthday='2011-03-08', detail_address='天台',
        medicinal_name='c', medicinal_num='2'
        ).query_prescription(name)
        pytest.assume(res == name)

if __name__ == '__main__':
    pytest.main(['test_yiyao.py','-sq'])
