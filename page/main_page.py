from page.prescription_center_page import PrescriptionCenterPage
from page.base_page_web import BasePage

class MainPage(BasePage):

    def goto_prescription_center(self):
        '''处方中心'''
        self.steps('./yml_casedatas/main_page.yml','goto_prescription_center')
        return PrescriptionCenterPage(self._driver)

if __name__ == '__main__':
    pass