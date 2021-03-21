from page.base_page_web import BasePage


class QueryPrescriptionPage(BasePage):
    '''处方中心'''
    def query_prescription(self,name):
        '''处方查询'''
        self._params['name'] = name
        depart_list = self.steps('./yml_casedatas/query_prescription_page.yml','query_prescription')
        return depart_list[0][0]

if __name__ == '__main__':
    pass