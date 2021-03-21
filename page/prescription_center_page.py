from add_prescription_page import AddPrescriptionPage
from base_page_web import BasePage
from query_prescription_page import QueryPrescriptionPage


class PrescriptionCenterPage(BasePage):
    '''处方中心'''
    def goto_prescription_create(self):
        '''去处方创建'''
        self.steps('./yml_casedatas/prescription_center_page.yml','goto_prescription_create')
        return AddPrescriptionPage(self._driver)

    def goto_prescription_query(self):
        '''去处方查询'''
        depart_list = self.steps('./yml_casedatas/prescription_center_page.yml', 'goto_prescription_query')
        return  QueryPrescriptionPage(self._driver)

if __name__ == '__main__':
    pass